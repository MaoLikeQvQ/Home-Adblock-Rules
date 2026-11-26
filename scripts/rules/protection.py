"""Global policy and origin tracking. SPDX-License-Identifier: MIT."""
from dataclasses import dataclass, field
import hashlib
import ipaddress
import json
from .parsers import domain, classical_rule, parse_adguard, adguard_to_classical


@dataclass
class RuleIndex:
    origins: dict = field(default_factory=dict)

    def add(self, target, action, rule, origin):
        key = (target, action, rule)
        self.origins.setdefault(key, []).append(origin)

    def source(self, source, text):
        for line_number, raw in enumerate(text.splitlines(), 1):
            line = raw.strip()
            if not line or line.startswith(('!', '#', '[')) or line in ('payload:', 'payload: []'):
                continue
            if source['format'] == 'classical':
                item = line[2:].strip()
                if item[:1] in ('"', "'") and item[-1:] == item[:1]:
                    item = item[1:-1]
                blocked, allowed = {classical_rule(item)}, set()
            else:
                blocked, allowed = parse_adguard(line)
            origin = {'source_id': source['id'], 'file': f"sources/{source['id']}.txt",
                      'line': line_number, 'raw': raw}
            for target in source['targets']:
                for action, rules in [('block', blocked), ('allow', allowed)]:
                    if target == 'clash' and source['format'] == 'adguard':
                        rules = adguard_to_classical(rules)
                    for rule in rules:
                        self.add(target, action, rule, origin)

    def local(self, path, action):
        for line_number, raw in enumerate(path.read_text().splitlines(), 1):
            line = raw.split('#', 1)[0].strip()
            if not line:
                continue
            rule = classical_rule(line)
            origin = {'source_id': 'local-' + action, 'file': 'config/' + path.name,
                      'line': line_number, 'raw': raw}
            self.add('clash', action, rule, origin)
            kind, value, *_ = rule.split(',')
            if kind in ('DOMAIN', 'DOMAIN-SUFFIX'):
                dns_rule = ('|' if kind == 'DOMAIN' else '||') + value + '^'
                self.add('adguard', action, dns_rule, origin)

    def export(self):
        return [{'target': target, 'action': action, 'rule': rule,
                 'origins': sorted(origins, key=lambda x: (x['source_id'], x['line']))}
                for (target, action, rule), origins in sorted(self.origins.items())]


def fields(obj, required, optional=()):
    if not isinstance(obj, dict) or set(obj) - set(required) - set(optional) or set(required) - set(obj):
        raise ValueError('invalid configuration fields: ' + str(obj))


def spec(value):
    fields(value, ['domain', 'scope'])
    if value['scope'] not in ('exact', 'suffix'):
        raise ValueError('invalid policy scope')
    if domain(value['domain']) != value['domain']:
        raise ValueError('policy domains must be normalized')
    return value


def contains(outer, inner):
    if outer['scope'] == 'exact':
        return inner['scope'] == 'exact' and outer['domain'] == inner['domain']
    return inner['domain'] == outer['domain'] or inner['domain'].endswith('.' + outer['domain'])


def overlaps(a, b):
    return contains(a, b) or contains(b, a)


def rule_spec(target, rule):
    if target == 'adguard':
        if rule.startswith('||'):
            return {'domain': rule[2:-1], 'scope': 'suffix'}
        if rule.startswith('|'):
            return {'domain': rule[1:-1], 'scope': 'exact'}
    else:
        kind, value, *_ = rule.split(',')
        if kind in ('DOMAIN', 'DOMAIN-SUFFIX'):
            return {'domain': value, 'scope': 'exact' if kind == 'DOMAIN' else 'suffix'}
    return None


def load_policies(path):
    if not path.exists():
        return []
    config = json.loads(path.read_text())
    fields(config, ['schema_version', 'policies'])
    if config['schema_version'] != 1 or not isinstance(config['policies'], list):
        raise ValueError('invalid protection schema')
    ids, policies = set(), []
    for policy in config['policies']:
        fields(policy, ['id', 'enabled', 'domain', 'scope', 'permitted_block_rules',
                        'reason', 'evidence_level', 'evidence', 'reviewed_on'])
        if not isinstance(policy['id'], str) or not policy['id'] or policy['id'] in ids:
            raise ValueError('duplicate/invalid protection id')
        ids.add(policy['id'])
        spec({k: policy[k] for k in ('domain', 'scope')})
        if type(policy['enabled']) is not bool or not isinstance(policy['permitted_block_rules'], list):
            raise ValueError('invalid policy types')
        if policy['evidence_level'] not in ('upstream-reference', 'device-verified'):
            raise ValueError('invalid evidence level')
        if not isinstance(policy['reason'], str) or not policy['reason'].strip():
            raise ValueError('policy requires reason')
        if not isinstance(policy['evidence'], list) or not policy['evidence'] or not all(isinstance(x, str) and x for x in policy['evidence']):
            raise ValueError('policy requires evidence')
        import datetime
        datetime.date.fromisoformat(policy['reviewed_on'])
        for exception in policy['permitted_block_rules']:
            spec(exception)
            if not contains(policy, exception):
                raise ValueError('exception outside protection: ' + policy['id'])
        if policy['enabled']:
            if any(overlaps(policy, other) for other in policies):
                raise ValueError('overlapping protection policies')
            policies.append(policy)
    return config['policies']


def analyze_non_domain(target, rule, enabled):
    """Prove concrete domain intersections without claiming app-level harm."""
    literal = None
    if target == 'clash' and rule.startswith('DOMAIN-KEYWORD,'):
        literal = rule.split(',', 1)[1]
    elif target == 'adguard' and rule.startswith('*') and rule.endswith('*'):
        literal = rule[1:-1]
    if literal is not None:
        affected = []
        for policy in enabled:
            witness = None
            if literal in policy['domain']:
                witness = policy['domain']
            elif policy['scope'] == 'suffix':
                candidate = 'probe' + literal + '.' + policy['domain']
                try:
                    if domain(candidate) == candidate:
                        witness = candidate
                except (ValueError, UnicodeError):
                    pass
            if witness:
                affected.append({'policy_id': policy['id'], 'host': witness,
                                 'evidence': 'synthetic-match-witness',
                                 'business_impact': 'not-device-verified'})
            elif policy['scope'] == 'suffix':
                affected.append({'policy_id': policy['id'], 'host': None,
                                 'evidence': 'intersection-not-proven',
                                 'business_impact': 'unknown'})
        if not affected:
            return {'decision': 'keep', 'check_id': 'pattern-disjoint-exact-protection',
                    'reason': 'Literal pattern does not match any exact protected hostname',
                    'analysis': {'kind': 'literal-pattern', 'literal': literal, 'affected': []}}
        return {'decision': 'review', 'check_id': 'pattern-protection-intersection',
                'reason': 'Pattern can intersect protected suffixes; synthetic witnesses are not real app evidence',
                'analysis': {'kind': 'literal-pattern', 'literal': literal, 'affected': affected}}
    if target == 'clash' and rule.startswith(('IP-CIDR,', 'IP-CIDR6,')):
        parts = rule.split(',')
        network = ipaddress.ip_network(parts[1], strict=False)
        return {'decision': 'review', 'check_id': 'ip-protection-unknown',
                'reason': 'Destination IP can affect protected traffic; domain policy alone cannot prove separation',
                'analysis': {'kind': 'ip-network', 'network': str(network),
                             'no_resolve': 'no-resolve' in parts[2:],
                             'affected_policy_ids': [p['id'] for p in enabled],
                             'required_evidence': 'router destination IP and effective Mihomo route',
                             'dns_observation': 'not-performed; no live lookup is proof of permanent separation'}}
    return {'decision': 'review', 'check_id': 'non-domain-impact',
            'reason': 'Unsupported intersection analysis; manual review required'}


def witness_scenarios(directory, target):
    """Expected blocks demonstrate a protection limitation, not safety approval."""
    path = directory / 'decisions.json'
    if not path.exists():
        return []
    cases = []
    for decision in json.loads(path.read_text())['decisions']:
        if decision['target'] != target:
            continue
        for affected in decision.get('analysis', {}).get('affected', []):
            if not affected.get('host') or affected['evidence'] != 'synthetic-match-witness':
                continue
            identity = target + decision['rule'] + affected['policy_id']
            cases.append({'id': 'protection-witness-' + hashlib.sha256(identity.encode()).hexdigest()[:16],
                          'host': affected['host'], 'expected': 'block', 'targets': [target],
                          'query_types': ['A', 'AAAA'], 'policy_id': affected['policy_id'],
                          'rule': decision['rule'], 'reason': 'Demonstrate pattern intersection; remains review-required'})
    return cases


def apply_protection(target, blocked, allowed, policies, index):
    enabled = [p for p in policies if p['enabled']]
    result, decisions = set(blocked), []
    for rule in sorted(blocked):
        shape = rule_spec(target, rule)
        if shape is None:
            if enabled:
                decisions.append({'target': target, 'rule': rule,
                                  **analyze_non_domain(target, rule, enabled),
                                  'origins': index.origins.get((target, 'block', rule), [])})
            continue
        for policy in enabled:
            if not overlaps(policy, shape):
                continue
            if not contains(policy, shape):
                raise ValueError(f"protection boundary conflict: {target} {rule} vs {policy['id']}")
            exception = any(shape == item for item in policy['permitted_block_rules'])
            if exception:
                for allow in allowed:
                    allow_shape = rule_spec(target, allow)
                    if allow_shape and overlaps(shape, allow_shape):
                        raise ValueError(f'protected advertising exception conflicts with allow: {rule} / {allow}')
                decision = 'keep'
            else:
                origins = index.origins.get((target, 'block', rule), [])
                if any(o['source_id'] == 'local-block' for o in origins):
                    raise ValueError('local block violates protection: ' + rule)
                result.discard(rule)
                decision = 'drop'
            decisions.append({'target': target, 'rule': rule, 'decision': decision,
                              'policy_id': policy['id'], 'reason': policy['reason'],
                              'origins': index.origins.get((target, 'block', rule), [])})
    return result, decisions
