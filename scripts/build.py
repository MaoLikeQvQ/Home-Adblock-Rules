#!/usr/bin/env python3
"""Fetch native upstream lists and publish deterministic, attributed rule providers.

SPDX-License-Identifier: MIT
"""
from __future__ import annotations

import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import hashlib
import gzip
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

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.rules.parsers import (
    domain, classical_rule, parse_classical, parse_adguard,
    adguard_to_classical, classical_to_adguard, local_rules,
)

from scripts.rules.protection import RuleIndex, load_policies, apply_protection
from scripts.rules.allowlist import compile_allowlist

ROOT = Path(__file__).resolve().parent.parent
MAX_BYTES = 32 * 1024 * 1024


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
    index = RuleIndex()
    policies = load_policies(root / 'config/protection.json')
    source_rules = {}
    seen = {"clash": set(), "adguard": set()}
    for source, data in zip(sources, raw_sources):
        text = data.decode("utf-8-sig")
        index.source(source, text)
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

    index.local(root / 'config/blocklist.txt', 'block')
    index.local(root / 'config/allowlist.txt', 'allow')
    own_block = local_rules(root / "config/blocklist.txt")
    own_allow = local_rules(root / "config/allowlist.txt", allow=True)
    own_dns_block, omitted = classical_to_adguard(own_block)
    own_dns_allow, _ = classical_to_adguard(own_allow)
    clash_block.update(own_block)
    clash_allow.update(own_allow)
    dns_block.update(own_dns_block)
    dns_allow.update(own_dns_allow)
    clash_block, clash_decisions = apply_protection(
        'clash', clash_block, clash_allow, policies, index)
    dns_block, dns_decisions = apply_protection(
        'adguard', dns_block, dns_allow, policies, index)
    decisions = clash_decisions + dns_decisions
    # Remove identical conflicts, then compile remaining Mihomo exceptions.
    # AdGuard keeps native exceptions in its single subscription.
    clash_block.difference_update(clash_allow)
    dns_block.difference_update(dns_allow)
    uncompiled_clash = set(clash_block)
    clash_block, allow_decisions = compile_allowlist(clash_block, clash_allow, index)
    decisions.extend(allow_decisions)
    if not clash_block or not dns_block:
        raise ValueError("empty final subscription")
    retained_clash = uncompiled_clash - {d['rule'] for d in allow_decisions if d['decision'] == 'drop'}
    for target, final, local in [("clash", retained_clash, own_block), ("adguard", dns_block, own_dns_block)]:
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
    report = {"schema_version": 2, "mihomo_allow_mode": "compiled",
              "protection": {"policies": policies, "decisions": len(decisions)},
              "repository": repository, "sources": reports,
              "counts": {"clash_block": len(clash_block), "clash_allow": len(clash_allow),
                         "adguard_block": len(dns_block), "adguard_allow": len(dns_allow)},
              "local_clash_only_rules": omitted,
              "deduplication": "identical normalized rules; matching scope preserved"}
    base_url = f"https://raw.githubusercontent.com/{repository}/dist"
    example = f"""# 合并进现有 Mihomo 配置；这是规则片段，不是代理节点订阅。
rule-providers:
  home-adblock:
    type: http
    behavior: classical
    format: yaml
    url: {base_url}/clash.yaml
    path: ./ruleset/home-adblock.yaml
    interval: 28800
rules:
  # 白名单已在构建时处理；放在广泛匹配规则和 MATCH 前。
  - RULE-SET,home-adblock,REJECT
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
        (stage / "clash-allow.yaml").write_text(yaml_payload(
            clash_allow, header + '# Audit and legacy-client compatibility; not required by the compiled provider.\n'),
            encoding="utf-8")
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
        (stage / 'decisions.json').write_text(json.dumps(
            {'schema_version': 1, 'decisions': decisions}, ensure_ascii=False, indent=2) + chr(10), encoding='utf-8')
        with (stage / 'rules.jsonl.gz').open('wb') as raw_handle, gzip.GzipFile(
                filename='', mode='wb', fileobj=raw_handle, mtime=0) as handle:
            for record in index.export():
                handle.write((json.dumps(record, ensure_ascii=False, sort_keys=True) + chr(10)).encode('utf-8'))
        (stage / "sources").mkdir()
        for source, data in zip(sources, raw_sources):
            (stage / "sources" / (source["id"] + ".txt")).write_bytes(data)
        for source_file in ["LICENSE", "NOTICE.md", "licenses/AWAvenue-LICENSE", "licenses/217heidai-LICENSE", "licenses/home-dns-adblock-LICENSE", "config/sources.json", "config/blocklist.txt", "config/allowlist.txt", "scripts/build.py"]:
            destination = stage / "sources" / source_file
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(root / source_file, destination)
        for folder, pattern in [('scripts', '*.py'), ('config', '*.json'), ('tests', '*.json')]:
            for source_file in sorted((root / folder).rglob(pattern)):
                destination = stage / 'sources' / source_file.relative_to(root)
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source_file, destination)
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
