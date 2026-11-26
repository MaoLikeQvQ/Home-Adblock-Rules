"""Strict native rule parsing; SPDX-License-Identifier: MIT."""
from pathlib import Path
import ipaddress
import re

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
        return f"{kind},{domain(value, allow_ip_literal=True)}"
    if kind == "DOMAIN-KEYWORD" and len(parts) == 2 and re.fullmatch(r"[a-zA-Z0-9_.-]+", value):
        return f"{kind},{value.lower()}"
    if kind in {"IP-CIDR", "IP-CIDR6"} and (len(parts) == 2 or parts[2:] == ["no-resolve"]):
        net = ipaddress.ip_network(value, strict=False)
        if net.version != (6 if kind == "IP-CIDR6" else 4):
            raise ValueError(f"IP version mismatch: {line}")
        # Preserve no-resolve exactly as supplied by the source.
        return f"{kind},{net}" + (",no-resolve" if len(parts) == 3 else "")
    raise ValueError(f"unsupported classical rule: {line}")


def parse_classical(text: str, *, compiled: bool = False) -> set[str]:
    rules = set()
    payload = False
    for number, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line == 'payload: []' and not payload:
            payload = True
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
        if compiled:
            from .allowlist import parse_compiled_rule
            rules.add(parse_compiled_rule(item))
        else:
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
