#!/usr/bin/env python3
"""Fetch native upstream lists and publish deterministic, attributed rule providers.

SPDX-License-Identifier: MIT
"""
from __future__ import annotations

import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import hashlib
import ipaddress
import json
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile
import time
import urllib.request
import urllib.parse

ROOT = Path(__file__).resolve().parent.parent
MAX_BYTES = 32 * 1024 * 1024
DOMAIN_LABEL = re.compile(r"[a-z0-9_](?:[a-z0-9_-]{0,61}[a-z0-9_])?\Z")


def domain(value: str, allow_ip_literal: bool = False) -> str:
    value = value.lower().rstrip(".").encode("idna").decode("ascii")
    labels = value.split(".")
    if len(value) > 253 or len(labels) < 2 or not all(DOMAIN_LABEL.fullmatch(x) for x in labels):
        raise ValueError(f"invalid domain: {value!r}")
    try:
        ipaddress.ip_address(value)
    except ValueError:
        return value
    if allow_ip_literal:
        # A DNS-list hostname that looks like an IP stays a hostname mask. It
        # must not become an IP-CIDR rule with a broader network-layer effect.
        return value
    raise ValueError(f"IP address used as domain: {value}")


def classical_rule(line: str) -> str:
    parts = [part.strip() for part in line.split(",")]
    if len(parts) < 2:
        raise ValueError(f"invalid classical rule: {line}")
    kind, value = parts[:2]
    if kind in {"DOMAIN", "DOMAIN-SUFFIX"} and len(parts) == 2:
        return f"{kind},{domain(value)}"
    if kind == "DOMAIN-KEYWORD" and len(parts) == 2 and re.fullmatch(r"[a-zA-Z0-9_.-]+", value):
        return f"{kind},{value.lower()}"
    if kind in {"IP-CIDR", "IP-CIDR6"} and (len(parts) == 2 or parts[2:] == ["no-resolve"]):
        net = ipaddress.ip_network(value, strict=False)
        if net.version != (6 if kind == "IP-CIDR6" else 4):
            raise ValueError(f"IP version mismatch: {line}")
        # Preserve no-resolve exactly as supplied by the source.
        return f"{kind},{net}" + (",no-resolve" if len(parts) == 3 else "")
    raise ValueError(f"unsupported classical rule: {line}")


def parse_classical(text: str) -> set[str]:
    rules = set()
    payload = False
    for number, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line == "payload:":
            if payload:
                raise ValueError("duplicate payload")
            payload = True
            continue
        if not payload or not line.startswith("- "):
            raise ValueError(f"line {number}: expected a classical payload item")
        item = line[2:].strip()
        if len(item) >= 2 and item[0] == item[-1] and item[0] in "\"'":
            item = item[1:-1]
        rules.add(classical_rule(item))
    if not payload:
        raise ValueError("missing payload")
    return rules


def parse_adguard(text: str) -> tuple[set[str], set[str]]:
    blocked, allowed = set(), set()
    for number, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith(("!", "#")) or line == "[Adblock Plus 2.0]":
            continue
        exception = line.startswith("@@")
        body = line[2:] if exception else line
        match = re.fullmatch(r"(\|\||\|)([^|^]+)\^", body)
        if match:
            prefix, value = match.groups()
            rule = prefix + domain(value, allow_ip_literal=True) + "^"
        elif not exception and re.fullmatch(r"\*[a-zA-Z0-9_.-]+\*", body):
            # Native AWAvenue wildcard patterns are preserved only for AdGuard.
            rule = body.lower()
        else:
            raise ValueError(f"line {number}: unsupported AdGuard syntax: {line}")
        (allowed if exception else blocked).add(rule)
    return blocked, allowed


def adguard_to_classical(rules: set[str]) -> set[str]:
    result = set()
    for rule in rules:
        if rule.startswith("||"):
            result.add("DOMAIN-SUFFIX," + rule[2:-1])
        elif rule.startswith("|"):
            result.add("DOMAIN," + rule[1:-1])
        else:
            raise ValueError(f"cannot convert AdGuard pattern to Clash: {rule}")
    return result


def classical_to_adguard(rules: set[str]) -> tuple[set[str], list[str]]:
    result, skipped = set(), []
    for rule in sorted(rules):
        kind, value, *_ = rule.split(",")
        if kind == "DOMAIN":
            result.add(f"|{value}^")
        elif kind == "DOMAIN-SUFFIX":
            result.add(f"||{value}^")
        else:
            skipped.append(rule)
    return result, skipped


def local_rules(path: Path, allow: bool = False) -> set[str]:
    result = set()
    for number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        rule = classical_rule(line)
        if allow and not rule.startswith(("DOMAIN,", "DOMAIN-SUFFIX,")):
            raise ValueError(f"{path}:{number}: whitelist supports domain rules only")
        result.add(rule)
    return result


def fetch(url: str) -> bytes:
    if not url.startswith("https://"):
        raise ValueError(f"upstream requires HTTPS: {url}")
    for attempt in range(3):
        try:
            headers = {"User-Agent": "home-adblock-rules/1.0"}
            token = os.environ.get("GITHUB_TOKEN")
            if url.startswith("https://api.github.com/") and token:
                headers["Authorization"] = f"Bearer {token}"
            request = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(request, timeout=60) as response:
                if not response.url.startswith("https://"):
                    raise ValueError("upstream redirected to insecure HTTP")
                data = response.read(MAX_BYTES + 1)
            if len(data) > MAX_BYTES:
                raise ValueError("upstream exceeds 32 MiB limit")
            return data
        except (OSError, ValueError):
            if attempt == 2:
                raise
            time.sleep(attempt + 1)
    raise AssertionError("unreachable")


def yaml_payload(rules: set[str], header: str) -> str:
    if not rules:
        return header + "payload: []\n"
    return header + "payload:\n" + "".join(f"  - '{rule}'\n" for rule in sorted(rules))


def pin_sources(sources: list[dict]) -> dict[str, dict]:
    """Resolve GitHub branches once, then download immutable commit URLs."""
    revisions = {}
    evidence = {}
    for source in sources:
        url = source["url"]
        match = re.fullmatch(r"https://raw\.githubusercontent\.com/([^/]+)/([^/]+)/([^/]+)/(.+)", url)
        if not match:
            evidence[source["id"]] = {"resolved_url": url}
            continue
        owner, repo, ref, path = match.groups()
        if re.fullmatch(r"[0-9a-f]{40}", ref):
            commit = ref
        else:
            key = (owner, repo, ref)
            if key not in revisions:
                endpoint = f"https://api.github.com/repos/{owner}/{repo}/git/ref/heads/{urllib.parse.quote(ref, safe='')}"
                result = json.loads(fetch(endpoint))
                commit = result["object"]["sha"]
                if result["object"]["type"] != "commit" or not re.fullmatch(r"[0-9a-f]{40}", commit):
                    raise ValueError("GitHub branch did not resolve to a commit")
                revisions[key] = commit
            commit = revisions[key]
        evidence[source["id"]] = {
            "upstream_commit": commit,
            "resolved_url": f"https://raw.githubusercontent.com/{owner}/{repo}/{commit}/{path}",
        }
    return evidence


def build(root: Path, output: Path, repository: str, source_dir: Path | None = None) -> dict:
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository):
        raise ValueError("repository must be OWNER/REPO")
    sources = json.loads((root / "config/sources.json").read_text(encoding="utf-8"))["sources"]
    baseline_path = output / "report.json"
    baseline = json.loads(baseline_path.read_text(encoding="utf-8")) if baseline_path.exists() else {}
    previous_sources = {item["id"]: item for item in baseline.get("sources", [])}
    if not sources or len({s["id"] for s in sources}) != len(sources):
        raise ValueError("sources must be nonempty with unique ids")
    for source in sources:
        if not re.fullmatch(r"[a-z0-9-]+", source["id"]):
            raise ValueError("invalid source id")
        if source["format"] not in {"adguard", "classical"} or not source["targets"]:
            raise ValueError("unsupported source format or empty targets")
        if set(source["targets"]) - {"clash", "adguard"}:
            raise ValueError("unsupported target")
        if source["format"] == "classical" and "adguard" in source["targets"]:
            raise ValueError("use native AdGuard sources for DNS output")

    if source_dir:
        original_report = source_dir.parent / "report.json"
        original = json.loads(original_report.read_text(encoding="utf-8")) if original_report.exists() else {}
        saved_sources = {item["id"]: item for item in original.get("sources", [])}
        evidence = {}
        for source in sources:
            saved = saved_sources.get(source["id"], {})
            evidence[source["id"]] = {}
            if "upstream_commit" in saved:
                evidence[source["id"]]["upstream_commit"] = saved["upstream_commit"]
            evidence[source["id"]]["resolved_url"] = saved.get("resolved_url", source["url"])
    else:
        saved_sources = {}
        evidence = pin_sources(sources)

    def download(source: dict) -> bytes:
        if source_dir:
            data = (source_dir / (source["id"] + ".txt")).read_bytes()
            expected = saved_sources.get(source["id"], {}).get("sha256")
            if expected and hashlib.sha256(data).hexdigest() != expected:
                raise ValueError(f"{source['id']}: snapshot hash mismatch")
            return data
        return fetch(evidence[source["id"]]["resolved_url"])

    with ThreadPoolExecutor(max_workers=4) as pool:
        raw_sources = list(pool.map(download, sources))

    clash_block, clash_allow, dns_block, dns_allow = set(), set(), set(), set()
    reports = []
    source_rules = {}
    seen = {"clash": set(), "adguard": set()}
    for source, data in zip(sources, raw_sources):
        text = data.decode("utf-8-sig")
        if source["format"] == "classical":
            blocked, allowed = parse_classical(text), set()
        else:
            blocked, allowed = parse_adguard(text)
        if len(blocked) < source["min_rules"]:
            raise ValueError(f"{source['id']}: only {len(blocked)} rules; below min_rules")
        previous = previous_sources.get(source["id"])
        max_drop = source.get("max_drop_ratio", 0.35)
        if not 0 <= max_drop < 1:
            raise ValueError("max_drop_ratio must be in [0, 1)")
        if previous and previous["url"] == source["url"]:
            if len(blocked) < previous["block_rules"] * (1 - max_drop):
                raise ValueError(f"{source['id']}: rules dropped more than {max_drop:.0%}; review upstream before publishing")
        target_rules = {}
        if "clash" in source["targets"]:
            target_rules["clash"] = blocked if source["format"] == "classical" else adguard_to_classical(blocked)
            clash_block.update(target_rules["clash"])
            clash_allow.update(adguard_to_classical(allowed))
        if "adguard" in source["targets"]:
            target_rules["adguard"] = blocked
            dns_block.update(blocked)
            dns_allow.update(allowed)
        contribution = {}
        for target, rules in target_rules.items():
            contribution[target] = {"input_block_rules": len(rules),
                                    "added_after_previous_sources": len(rules - seen[target]),
                                    "duplicates_with_previous_sources": len(rules & seen[target])}
            seen[target].update(rules)
        source_rules[source["id"]] = target_rules
        reports.append({**source, **evidence[source["id"]],
                        "sha256": hashlib.sha256(data).hexdigest(),
                        "git_blob_sha1": hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest(),
                        "snapshot": f"sources/{source['id']}.txt",
                        "block_rules": len(blocked), "allow_rules": len(allowed),
                        "contribution": contribution})

    own_block = local_rules(root / "config/blocklist.txt")
    own_allow = local_rules(root / "config/allowlist.txt", allow=True)
    own_dns_block, omitted = classical_to_adguard(own_block)
    own_dns_allow, _ = classical_to_adguard(own_allow)
    clash_block.update(own_block)
    clash_allow.update(own_allow)
    dns_block.update(own_dns_block)
    dns_allow.update(own_dns_allow)
    # Remove identical conflicts. Parent/child exceptions are expressed by the
    # dedicated allow provider / native AdGuard exceptions, not by broadening rules.
    clash_block.difference_update(clash_allow)
    dns_block.difference_update(dns_allow)
    if not clash_block or not dns_block:
        raise ValueError("empty final subscription")
    for target, final, local in [("clash", clash_block, own_block), ("adguard", dns_block, own_dns_block)]:
        frequency = Counter(rule for entry in source_rules.values() for rule in entry.get(target, set()))
        for entry in reports:
            if target not in entry["contribution"]:
                continue
            rules = source_rules[entry["id"]][target]
            exclusive = sorted(rule for rule in rules & final if frequency[rule] == 1 and rule not in local)
            entry["contribution"][target].update({"retained_in_output": len(rules & final),
                                                   "exclusive_block_rules": len(exclusive),
                                                   "exclusive_examples": exclusive[:10]})

    repo_url = f"https://github.com/{repository}"
    header = ("# home-adblock-rules — generated; do not edit\n"
              "# SPDX-License-Identifier: GPL-3.0-only\n"
              f"# Project / source code: {repo_url}\n"
              "# Upstream: TG-Twilight/AWAvenue-Ads-Rule (GPLv3)\n"
              "# Upstream: 217heidai/adblockfilters (GPLv3)\n"
              "# Upstream: abclq/home-dns-adblock (MIT)\n"
              "# See sources/ for original inputs, notices and licenses.\n")
    report = {"repository": repository, "sources": reports,
              "counts": {"clash_block": len(clash_block), "clash_allow": len(clash_allow),
                         "adguard_block": len(dns_block), "adguard_allow": len(dns_allow)},
              "local_clash_only_rules": omitted,
              "deduplication": "identical normalized rules; matching scope preserved"}
    base_url = f"https://raw.githubusercontent.com/{repository}/dist"
    example = f"""# 合并进现有 Mihomo 配置；这是规则片段，不是代理节点订阅。
rule-providers:
  home-adblock-allow:
    type: http
    behavior: classical
    format: yaml
    url: {base_url}/clash-allow.yaml
    path: ./ruleset/home-adblock-allow.yaml
    interval: 28800
  home-adblock:
    type: http
    behavior: classical
    format: yaml
    url: {base_url}/clash.yaml
    path: ./ruleset/home-adblock.yaml
    interval: 28800
rules:
  # 仅拦截命中黑名单且不在白名单的连接；白名单继续走现有分流。
  # 放在其他广泛匹配规则和 MATCH 前。需要支持逻辑规则的 Mihomo。
  - AND,((RULE-SET,home-adblock),(NOT,((RULE-SET,home-adblock-allow)))),REJECT
"""
    # Fetching, parsing and rendering all happen before touching the current output.
    output = output.resolve()
    if output == root.resolve() or output in root.resolve().parents:
        raise ValueError("output must not replace project root or its ancestors")
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".build-", dir=output.parent) as temporary:
        stage = Path(temporary) / "dist"
        stage.mkdir()
        (stage / "clash.yaml").write_text(yaml_payload(clash_block, header), encoding="utf-8")
        (stage / "clash-allow.yaml").write_text(yaml_payload(clash_allow, header), encoding="utf-8")
        dns_text = header.replace("#", "!") + "! Expires: 8 hours\n"
        dns_text += "\n".join(sorted(dns_block)) + "\n"
        dns_text += "\n".join("@@" + rule for rule in sorted(dns_allow)) + "\n"
        (stage / "adguard.txt").write_text(dns_text, encoding="utf-8")
        (stage / "mihomo.example.yaml").write_text(example, encoding="utf-8")
        report["output_sha256"] = {name: hashlib.sha256((stage / name).read_bytes()).hexdigest()
                                   for name in ["clash.yaml", "clash-allow.yaml", "adguard.txt"]}
        (stage / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        audit = ["# 规则来源核对\n", "每个文件固定到构建时的上游提交。SHA-256 对原始字节计算，可自行下载复核。新增与独有数量按完全相同的规范化规则统计，不代表新增域名覆盖范围。\n"]
        for entry in reports:
            audit.extend([f"## {entry.get('name', entry['id'])}\n", f"- 项目：{entry.get('homepage', entry['url'])}",
                          f"- 实际下载：{entry['resolved_url']}", f"- 原始快照：[{entry['snapshot']}]({entry['snapshot']})",
                          f"- 上游提交：`{entry.get('upstream_commit', '未固定：离线输入或非 GitHub 来源')}`",
                          f"- SHA-256：`{entry['sha256']}`", f"- Git Blob SHA-1：`{entry['git_blob_sha1']}`",
                          f"- 解析结果：拦截 {entry['block_rules']} 条，放行 {entry['allow_rules']} 条。"])
            for target, summary in entry["contribution"].items():
                audit.append(f"- {target}：按来源顺序新增 {summary['added_after_previous_sources']} 条；与之前来源重复 {summary['duplicates_with_previous_sources']} 条；最终保留 {summary['retained_in_output']} 条；该来源独有 {summary['exclusive_block_rules']} 条。")
                if summary["exclusive_examples"]:
                    audit.extend(["\n独有规则示例：\n", "```text", *summary["exclusive_examples"], "```\n"])
            audit.append("")
        (stage / "SOURCES.md").write_text("\n".join(audit) + "\n", encoding="utf-8")
        (stage / "sources").mkdir()
        for source, data in zip(sources, raw_sources):
            (stage / "sources" / (source["id"] + ".txt")).write_bytes(data)
        for source_file in ["LICENSE", "NOTICE.md", "licenses/AWAvenue-LICENSE", "licenses/217heidai-LICENSE", "licenses/home-dns-adblock-LICENSE", "config/sources.json", "config/blocklist.txt", "config/allowlist.txt", "scripts/build.py"]:
            destination = stage / "sources" / source_file
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(root / source_file, destination)
        old = Path(temporary) / "previous"
        if output.exists():
            output.rename(old)
        try:
            stage.rename(output)
        except OSError:
            if old.exists():
                old.rename(output)
            raise
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "dist")
    parser.add_argument("--repository", default=os.environ.get("GITHUB_REPOSITORY", "YOUR_NAME/Home-Adblock-Rules"))
    parser.add_argument("--source-dir", type=Path, help="offline source snapshots: <source-id>.txt")
    args = parser.parse_args()
    try:
        report = build(ROOT, args.output, args.repository, args.source_dir)
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"Build failed; existing output preserved: {error}", file=sys.stderr)
        return 1
    print(json.dumps(report["counts"], ensure_ascii=False, indent=2))
    if report["local_clash_only_rules"]:
        print("Local Clash-only rules: see report.json", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
