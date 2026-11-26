#!/usr/bin/env python3
"""Validate build artifacts and changes. SPDX-License-Identifier: MIT."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import subprocess

if __package__ in (None, ''):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts.rules.parsers import parse_classical, parse_adguard
from scripts.rules.protection import rule_spec, contains

ROOT = Path(__file__).resolve().parent.parent


def digest(data):
    return hashlib.sha256(data).hexdigest()


def file_hashes(directory, exclude=()):
    result = {}
    for path in sorted(directory.rglob('*')):
        if path.is_symlink():
            raise ValueError('symlink in artifact: ' + str(path))
        if path.is_file() and path.relative_to(directory).as_posix() not in exclude:
            result[path.relative_to(directory).as_posix()] = digest(path.read_bytes())
    return result


def read_rules(directory):
    blocked, allowed = parse_adguard((directory / 'adguard.txt').read_text())
    return {'clash_block': parse_classical((directory / 'clash.yaml').read_text(), compiled=True),
            'clash_allow': parse_classical((directory / 'clash-allow.yaml').read_text()),
            'adguard_block': blocked, 'adguard_allow': allowed}


def validate(candidate, baseline, config_path):
    config = json.loads(config_path.read_text())
    if set(config) != {'schema_version', 'added_ratio', 'removed_ratio', 'engines'} or config['schema_version'] != 1:
        raise ValueError('invalid validation config')
    for key in ('added_ratio', 'removed_ratio'):
        if type(config[key]) not in (float, int) or not 0 <= config[key] <= 1:
            raise ValueError('invalid validation ratio')
    report = json.loads((candidate / 'report.json').read_text())
    findings, changes = [], {}
    if set(report['output_sha256']) != {'clash.yaml', 'clash-allow.yaml', 'adguard.txt'}:
        raise ValueError('incomplete rule output hashes')
    for name, expected in report['output_sha256'].items():
        if digest((candidate / name).read_bytes()) != expected:
            raise ValueError('output hash mismatch: ' + name)
    for source in report['sources']:
        name = 'sources/' + source['id'] + '.txt'
        if source['snapshot'] != name or '/' in source['id'] or '..' in source['id']:
            raise ValueError('invalid source snapshot path')
        if digest((candidate / name).read_bytes()) != source['sha256']:
            raise ValueError('source hash mismatch: ' + name)
    current = read_rules(candidate)
    if baseline and (baseline / 'report.json').exists():
        previous_report = json.loads((baseline / 'report.json').read_text())
        previous = read_rules(baseline)
        baseline_hash = digest((baseline / 'report.json').read_bytes())
        for target, rules in current.items():
            added = sorted(rules - previous[target])
            removed = sorted(previous[target] - rules)
            changes[target] = {'added': added, 'removed': removed}
            if target.endswith('allow') and (added or removed):
                findings.append({'id': 'allow-change-' + target, 'reason': 'Allow scope changed'})
            if target.endswith('block'):
                for rule in added:
                    if rule.startswith(('DOMAIN-KEYWORD,', 'IP-CIDR', '*', 'AND,')):
                        findings.append({'id': 'broad-' + digest((target + rule).encode())[:16],
                                         'target': target, 'rule': rule, 'reason': 'New pattern, IP or compiled exception rule'})
                    target_format = 'clash' if target.startswith('clash') else 'adguard'
                    shape = rule_spec(target_format, rule)
                    if shape and shape['scope'] == 'suffix':
                        previous_shapes = [rule_spec(target_format, old) for old in removed]
                        if any(old and contains(shape, old) and old != shape for old in previous_shapes):
                            findings.append({'id': 'scope-' + digest(rule.encode())[:16],
                                             'rule': rule, 'reason': 'Broader suffix replaced exact/subdomain'})
        old_sources = {s['id']: s for s in previous_report['sources']}
        if set(old_sources) != {s['id'] for s in report['sources']}:
            findings.append({'id': 'sources-changed', 'reason': 'Source set changed'})
        for source in report['sources']:
            old = old_sources.get(source['id'])
            if old is None:
                continue
            if any(old.get(k) != source.get(k) for k in ('url', 'format', 'targets')):
                findings.append({'id': 'source-config-' + source['id'], 'reason': 'Source configuration changed'})
                continue
            old_text = (baseline / old['snapshot']).read_text()
            new_text = (candidate / source['snapshot']).read_text()
            parse = parse_classical if source['format'] == 'classical' else lambda text: parse_adguard(text)[0]
            before, after = parse(old_text), parse(new_text)
            added, removed = len(after - before), len(before - after)
            if added / max(len(before), 1) > config['added_ratio'] or removed / max(len(before), 1) > config['removed_ratio']:
                findings.append({'id': 'volume-' + source['id'], 'reason': 'Source change exceeds threshold',
                                 'added': added, 'removed': removed, 'previous': len(before)})
    else:
        baseline_hash = None
        findings.append({'id': 'bootstrap-required', 'reason': 'Stable baseline review required'})
    for policy in report.get('protection', {}).get('policies', []):
        if not policy['enabled']:
            findings.append({'id': 'disabled-policy-' + policy['id'], 'reason': 'Proposed protection is not enabled'})
    for item in json.loads((candidate / 'decisions.json').read_text())['decisions']:
        if item['decision'] == 'review':
            findings.append({'id': 'impact-' + digest((item['target'] + item['rule']).encode())[:16],
                             'target': item['target'], 'rule': item['rule'], 'reason': item['reason'],
                             'check_id': item['check_id'], 'analysis': item.get('analysis'),
                             'origins': item['origins']})
    result = {'schema_version': 1, 'status': 'review-required' if findings else 'passed',
              'baseline_report_sha256': baseline_hash, 'findings': findings, 'changes': changes,
              'output_sha256': report['output_sha256'],
              'config_sha256': digest(config_path.read_bytes()),
              'protection_sha256': digest((candidate / 'sources/config/protection.json').read_bytes())
                  if (candidate / 'sources/config/protection.json').exists() else None,
              'device_acceptance': 'incomplete'}
    (candidate / 'validation.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + chr(10))
    lines = ['# 候选验证报告', '', '状态：' + result['status'], '',
             '设备验收：未完成。实际内核结果见 engines.json。', '', '## 审核项', '']
    for item in findings:
        lines += ['### ' + item['id'], '', item['reason']]
        if item.get('rule'):
            lines += ['', '- 目标：' + item.get('target', 'unknown'), '- 规则：`' + item['rule'] + '`']
        for origin in item.get('origins', []):
            lines.append(f"- 来源：{origin['source_id']}，{origin['file']}:{origin['line']}")
        analysis = item.get('analysis') or {}
        for affected in analysis.get('affected', []):
            lines.append(f"- {affected['policy_id']}：`{affected['host'] or '交集未确定'}`（合成样例，不是实机请求）")
        if analysis.get('kind') == 'ip-network':
            lines.append('- 待核对：路由器连接目标 IP 与实际命中规则；no-resolve 不代表绝不会影响域名连接。')
        lines.append('')
    lines += ['', '完整变更见 validation.json，处理与原文位置见 decisions.json、rules.jsonl.gz。']
    (candidate / 'VALIDATION.md').write_text(chr(10).join(lines) + chr(10))
    return result


def seal(candidate, root=ROOT, baseline_commit=None):
    excluded = ('manifest.json', 'acceptance.json', 'release.json', 'mihomo.pinned.yaml')
    files = file_hashes(candidate, excluded)
    inputs = {p.relative_to(root).as_posix(): digest(p.read_bytes())
              for folder, pattern in [('scripts', '*.py'), ('config', '*'), ('tests', '*.json')]
              for p in sorted((root / folder).rglob(pattern)) if p.is_file() and '__pycache__' not in p.parts}
    core = {'schema_version': 1, 'files': files, 'implementation': inputs, 'baseline_commit': baseline_commit}
    identifier = digest(json.dumps(core, sort_keys=True, separators=(',', ':')).encode())
    source_commit = None
    try:
        dirty = subprocess.check_output(['git', '-C', str(root), 'status', '--porcelain', '--',
                                         'scripts', 'config', 'tests/scenarios.json'], stderr=subprocess.DEVNULL)
        if not dirty:
            source_commit = subprocess.check_output(['git', '-C', str(root), 'rev-parse', 'HEAD'],
                                                    stderr=subprocess.DEVNULL).decode().strip()
    except subprocess.CalledProcessError:
        pass
    manifest = {**core, 'candidate_id': identifier, 'source_commit': source_commit}
    (candidate / 'manifest.json').write_text(json.dumps(manifest, sort_keys=True, indent=2) + chr(10))
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--candidate', type=Path, required=True)
    parser.add_argument('--baseline', type=Path)
    parser.add_argument('--config', type=Path, default=ROOT / 'config/validation.json')
    parser.add_argument('--baseline-commit')
    parser.add_argument('--seal', action='store_true')
    args = parser.parse_args()
    try:
        if args.seal:
            print(seal(args.candidate, baseline_commit=args.baseline_commit)['candidate_id'])
            return 0
        result = validate(args.candidate, args.baseline, args.config)
        print(result['status'], len(result['findings']), 'review items')
        return 2 if result['findings'] else 0
    except (OSError, ValueError, KeyError) as error:
        print(str(error), file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
