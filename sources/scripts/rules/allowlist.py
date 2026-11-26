"""Compile allow exceptions into a self-contained Mihomo provider. MIT."""
import re
import hashlib

from .parsers import classical_rule
from .parsers import parse_classical


def exclude(block, allowed):
    items = sorted(allowed)
    exception = items[0] if len(items) == 1 else 'OR,(' + ','.join(f'({item})' for item in items) + ')'
    return f'AND,(({block}),(NOT,(({exception}))))'


def parse_compiled_rule(rule):
    """Accept only the exact logical grammar emitted by this compiler."""
    if not rule.startswith('AND,'):
        return classical_rule(rule)
    match = re.fullmatch(r'AND,\(\(([^()]+)\),\(NOT,\(\((.+)\)\)\)\)', rule)
    if not match:
        raise ValueError('invalid compiled allow exception: ' + rule)
    block, exception = match.groups()
    block = classical_rule(block)
    if exception.startswith('OR,(') and exception.endswith(')'):
        items = re.findall(r'\(([^()]+)\)', exception[4:-1])
    else:
        items = [exception]
    allowed = {classical_rule(item) for item in items}
    if not allowed or any(not item.startswith(('DOMAIN,', 'DOMAIN-SUFFIX,')) for item in allowed):
        raise ValueError('compiled exception requires domain allow rules')
    if exclude(block, allowed) != rule:
        raise ValueError('noncanonical compiled allow exception: ' + rule)
    return rule


def compile_allowlist(blocked, allowed, index=None):
    """Drop covered blocks; subtract partial intersections without widening."""
    exact, suffix, within = set(), set(), {}
    for item in allowed:
        kind, value = classical_rule(item).split(',', 1)
        if kind not in ('DOMAIN', 'DOMAIN-SUFFIX'):
            raise ValueError('allowlist requires domain rules')
        (exact if kind == 'DOMAIN' else suffix).add(value)
        labels = value.split('.')
        for i in range(len(labels)):
            within.setdefault('.'.join(labels[i:]), set()).add(item)
    result, decisions = set(), []
    for rule in sorted(blocked):
        parts = rule.split(',')
        kind, value = parts[:2]
        overlaps = set()
        covered = False
        if kind in ('DOMAIN', 'DOMAIN-SUFFIX'):
            labels = value.split('.')
            overlaps = {'DOMAIN-SUFFIX,' + '.'.join(labels[i:]) for i in range(len(labels))
                        if '.'.join(labels[i:]) in suffix}
            if kind == 'DOMAIN' and value in exact:
                overlaps.add('DOMAIN,' + value)
            covered = bool(overlaps)
            if not covered and kind == 'DOMAIN-SUFFIX':
                # A whitelist descendant is only a hole in the parent block.
                overlaps = within.get(value, set())
        elif kind == 'DOMAIN-KEYWORD':
            overlaps = {'DOMAIN,' + name for name in exact if value in name}
            # Any suffix can have a descendant containing the keyword.
            overlaps.update('DOMAIN-SUFFIX,' + name for name in suffix)
        elif kind in ('IP-CIDR', 'IP-CIDR6'):
            # A domain may connect to any destination in this network.
            overlaps = set(allowed)
        else:
            raise ValueError('unsupported allowlist compilation: ' + rule)
        rendered = None if covered else exclude(rule, overlaps) if overlaps else rule
        if rendered is not None:
            result.add(rendered)
        if rendered != rule:
            origins = index.origins.get(('clash', 'block', rule), []) if index else []
            decisions.append({'target': 'clash', 'rule': rule, 'output_rule': rendered,
                              'decision': 'drop' if covered else 'compile',
                              'reason': 'Apply allowlist before publishing the single provider',
                              'origins': origins, 'allow_rules': sorted(overlaps),
                              'allow_origins': [origin for allow in sorted(overlaps)
                                                for origin in (index.origins.get(('clash', 'allow', allow), []) if index else [])],
                              'check_id': 'compiled-allowlist'})
            if rendered and index:
                for origin in origins:
                    index.add('clash', 'block', rendered, origin)
    return result, decisions


def allow_scenarios(directory):
    """Exercise every original exception against the single provider."""
    allowed = parse_classical((directory / 'clash-allow.yaml').read_text())
    hosts = set()
    for rule in allowed:
        kind, name = rule.split(',', 1)
        hosts.add(name)
        if kind == 'DOMAIN-SUFFIX':
            child = 'allow-check.' + name
            from .parsers import domain
            try:
                domain(child, allow_ip_literal=True)
            except ValueError:
                continue
            hosts.add(child)
    return [{'id': 'allow-' + hashlib.sha256(host.encode()).hexdigest()[:16],
             'host': host, 'expected': 'pass', 'targets': ['clash'], 'query_types': ['A']}
            for host in sorted(hosts)]
