#!/usr/bin/env python3
"""Publish verified snapshots without rebuilding; dry-run by default. MIT."""
import argparse
from contextlib import contextmanager
import json
import re
from pathlib import Path, PurePosixPath
import shutil
import subprocess
import sys
import tempfile

if __package__ in (None, ''):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts.validate import ROOT, digest, file_hashes, read_rules
from scripts.rules.protection import witness_scenarios

EXCLUDED = ('manifest.json', 'acceptance.json', 'release.json', 'mihomo.pinned.yaml')


def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args], stderr=subprocess.PIPE).decode().strip()


def safe_path(name):
    path = PurePosixPath(name)
    if not name or path.is_absolute() or '..' in path.parts or '.git' in path.parts or chr(92) in name or path.as_posix() != name:
        raise ValueError('unsafe artifact path: ' + name)
    return path


def verify(directory, implementation_root=None):
    manifest = json.loads((directory / 'manifest.json').read_text())
    if set(manifest) != {'schema_version', 'files', 'implementation', 'baseline_commit', 'candidate_id', 'source_commit'} or manifest['schema_version'] != 1:
        raise ValueError('invalid manifest')
    core = {k: v for k, v in manifest.items() if k not in ('candidate_id', 'source_commit')}
    expected_id = digest(json.dumps(core, sort_keys=True, separators=(',', ':')).encode())
    if manifest['candidate_id'] != expected_id:
        raise ValueError('candidate identity mismatch')
    for name in manifest['files']:
        safe_path(name)
    required = {'clash.yaml', 'clash-allow.yaml', 'adguard.txt', 'report.json',
                'validation.json', 'engines.json', 'decisions.json', 'rules.jsonl.gz', 'SOURCES.md'}
    if not required <= manifest['files'].keys():
        raise ValueError('missing required artifact')
    if file_hashes(directory, EXCLUDED) != manifest['files']:
        raise ValueError('artifact hash or file set mismatch')
    if implementation_root:
        current = {p.relative_to(implementation_root).as_posix(): digest(p.read_bytes())
                   for folder, pattern in [('scripts', '*.py'), ('config', '*'), ('tests', '*.json')]
                   for p in sorted((implementation_root / folder).rglob(pattern))
                   if p.is_file() and '__pycache__' not in p.parts}
        if current != manifest['implementation']:
            raise ValueError('implementation/configuration changed since candidate validation')
    for name, expected in manifest['implementation'].items():
        safe_path(name)
        snapshot = directory / 'sources' / name
        if not snapshot.is_file() or digest(snapshot.read_bytes()) != expected:
            raise ValueError('source snapshot does not match validated implementation: ' + name)
    validation = json.loads((directory / 'validation.json').read_text())
    engines = json.loads((directory / 'engines.json').read_text())
    if validation['status'] not in ('passed', 'review-required') or engines['status'] != 'passed':
        raise ValueError('candidate checks not complete')
    if set(engines.get('engines', {})) != {'mihomo', 'adguard'}:
        raise ValueError('missing engine verification')
    for result in engines['engines'].values():
        if result['status'] != 'passed' or not result.get('cases') or any(c['status'] != 'passed' for c in result['cases']):
            raise ValueError('incomplete engine cases')
        if not result.get('fixture_cases') or any(c['status'] != 'passed' for c in result['fixture_cases']):
            raise ValueError('incomplete engine boundary fixtures')
    report = json.loads((directory / 'report.json').read_text())
    if set(report['output_sha256']) != {'clash.yaml', 'clash-allow.yaml', 'adguard.txt'}:
        raise ValueError('incomplete tested output hash set')
    if validation.get('output_sha256') != report['output_sha256']:
        raise ValueError('validation report belongs to different outputs')
    config_path = directory / 'sources/config/validation.json'
    config_hash = digest(config_path.read_bytes())
    if validation.get('config_sha256') != config_hash or engines.get('validation_config_sha256') != config_hash:
        raise ValueError('validation or engine configuration fingerprint mismatch')
    protection_path = directory / 'sources/config/protection.json'
    protection_hash = digest(protection_path.read_bytes()) if protection_path.exists() else None
    if validation.get('protection_sha256') != protection_hash:
        raise ValueError('validation protection fingerprint mismatch')
    if report['counts'] != {key: len(rules) for key, rules in read_rules(directory).items()}:
        raise ValueError('output counts disagree with parsed rules')
    if engines.get('output_sha256') != report['output_sha256']:
        raise ValueError('engine tests belong to different outputs')
    for name, expected in report['output_sha256'].items():
        safe_path(name)
        if digest((directory / name).read_bytes()) != expected:
            raise ValueError('tested output changed')
    scenarios_path = directory / 'sources/tests/scenarios.json'
    if digest(scenarios_path.read_bytes()) != engines['scenarios_sha256']:
        raise ValueError('engine scenario fingerprint mismatch')
    scenarios = json.loads(scenarios_path.read_text())['cases']
    platform_pins = json.loads(config_path.read_text())['engines'].get(engines.get('platform'))
    if not platform_pins or set(platform_pins) != {'mihomo', 'adguard'}:
        raise ValueError('engine results refer to unconfigured platform')
    for engine, target in [('mihomo', 'clash'), ('adguard', 'adguard')]:
        engine_result = engines['engines'][engine]
        configured = platform_pins[engine]
        if engine_result.get('version') != configured['version'] or engine_result.get('archive_sha256') != configured['sha256']:
            raise ValueError('engine results do not match pinned version/checksum')
        actual = engines['engines'][engine]['cases']
        expected = {(case['id'], kind): case.get('expected') for case in scenarios if target in case['targets']
                    for kind in (case['query_types'] if engine == 'adguard' else [None])}
        if len(actual) != len(expected) or {(case['id'], case.get('query_type')): case.get('expected') for case in actual} != expected:
            raise ValueError('engine case coverage mismatch')
        witnesses = witness_scenarios(directory, target)
        expected_witnesses = {(case['id'], kind): case['expected'] for case in witnesses
                              for kind in (case['query_types'] if engine == 'adguard' else [None])}
        actual_witnesses = engine_result.get('protection_witness_cases', [])
        if len(actual_witnesses) != len(expected_witnesses) or {
                (case['id'], case.get('query_type')): case.get('expected') for case in actual_witnesses} != expected_witnesses:
            raise ValueError('protection intersection witness coverage mismatch')
        if any(case['status'] != 'passed' for case in actual_witnesses):
            raise ValueError('protection witness checks incomplete')
    verify_pinned_example(directory, report)
    return manifest, validation


def verify_pinned_example(directory, report):
    path = directory / 'mihomo.pinned.yaml'
    if not path.exists():
        return None
    pinned = path.read_text()
    prefix = f"https://raw.githubusercontent.com/{report['repository']}/"
    commits = set(re.findall(re.escape(prefix) + r'([0-9a-f]{40})/', pinned))
    if len(commits) != 1:
        raise ValueError('invalid paired provider commit')
    commit = commits.pop()
    expected = (directory / 'mihomo.example.yaml').read_text().replace(prefix + 'dist', prefix + commit)
    if pinned != expected:
        raise ValueError('pinned provider configuration changed outside immutable URL substitution')
    return commit


def verify_pinned_commit(repo, directory, report):
    commit = verify_pinned_example(directory, report)
    if commit:
        for name, expected in report['output_sha256'].items():
            content = subprocess.check_output(['git', '-C', str(repo), 'show', commit + ':' + name], stderr=subprocess.PIPE)
            if digest(content) != expected:
                raise ValueError('pinned provider commit contains different rules')


def verify_baseline_evidence(repo, manifest, validation):
    baseline = manifest['baseline_commit']
    if not isinstance(baseline, str) or not re.fullmatch('[0-9a-f]{40}', baseline):
        raise ValueError('promotion requires a fixed existing stable baseline')
    content = subprocess.check_output(['git', '-C', str(repo), 'show', baseline + ':report.json'], stderr=subprocess.PIPE)
    if digest(content) != validation.get('baseline_report_sha256'):
        raise ValueError('validation baseline evidence differs from sealed stable commit')


def verify_acceptance(record, manifest, validation):
    required = {'candidate_id', 'reviewer', 'reviewed_on', 'approved_findings', 'device', 'scenarios'}
    if set(record) != required or record['candidate_id'] != manifest['candidate_id']:
        raise ValueError('acceptance identity/schema mismatch')
    if not all(isinstance(record[k], str) and record[k].strip() for k in ('reviewer', 'reviewed_on', 'device')):
        raise ValueError('missing acceptance evidence')
    import datetime
    datetime.date.fromisoformat(record['reviewed_on'])
    findings = {x['id'] for x in validation['findings']}
    if set(record['approved_findings']) != findings:
        raise ValueError('risk review does not cover exact candidate findings')
    if set(record['scenarios']) != {'login', 'images', 'video', 'advertising'}:
        raise ValueError('missing device scenarios')
    for result in record['scenarios'].values():
        if result.get('status') != 'passed' or not result.get('evidence'):
            raise ValueError('device acceptance incomplete')


def export_commit(repo, commit, directory):
    if not re.fullmatch('[0-9a-f]{40}', commit):
        raise ValueError('full immutable commit SHA required')
    resolved = git(repo, 'rev-parse', '--verify', commit + '^{commit}')
    for line in git(repo, 'ls-tree', '-r', resolved).splitlines():
        metadata, name = line.split(chr(9), 1)
        mode, kind, sha = metadata.split()
        safe_path(name)
        if mode != '100644' or kind != 'blob':
            raise ValueError('non-regular file in release tree')
        path = directory / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(subprocess.check_output(['git', '-C', str(repo), 'cat-file', 'blob', sha]))
    return resolved


def publish(repo, directory, baseline, metadata, apply=False):
    # The workflow serializes all stable mutations; ordinary push also rejects
    # changes that race after this final baseline check. Never force-push.
    git(repo, 'fetch', 'origin', 'refs/heads/dist:refs/remotes/origin/dist')
    current = git(repo, 'rev-parse', 'refs/remotes/origin/dist')
    if current != baseline:
        raise ValueError('stable baseline changed; revalidate candidate')
    if not apply:
        return {'status': 'dry-run', 'baseline': current, **metadata}
    with tempfile.TemporaryDirectory(prefix='stable-publish-') as temp:
        checkout = Path(temp) / 'checkout'
        git(repo, 'worktree', 'add', '--detach', str(checkout), current)
        try:
            git(checkout, 'rm', '-r', '-f', '--ignore-unmatch', '.')
            for source in directory.rglob('*'):
                if source.is_file():
                    target = checkout / source.relative_to(directory)
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(source, target)
            (checkout / 'release.json').write_text(json.dumps(metadata, indent=2) + chr(10))
            git(checkout, 'config', 'user.name', 'github-actions[bot]')
            git(checkout, 'config', 'user.email', '41898282+github-actions[bot]@users.noreply.github.com')
            git(checkout, 'add', '-A')
            git(checkout, 'commit', '-m', 'chore: ' + metadata['action'] + ' verified rules')
            commit = git(checkout, 'rev-parse', 'HEAD')
            git(checkout, 'push', 'origin', 'HEAD:refs/heads/dist')
            return {'status': 'published', 'commit': commit, **metadata}
        finally:
            git(repo, 'worktree', 'remove', '--force', str(checkout))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['promote', 'rollback'])
    parser.add_argument('--repo', type=Path, default=ROOT)
    parser.add_argument('--candidate-commit')
    parser.add_argument('--release-commit')
    parser.add_argument('--acceptance', type=Path)
    parser.add_argument('--reason')
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    try:
        if args.apply and args.dry_run:
            raise ValueError('--apply conflicts with --dry-run')
        with tempfile.TemporaryDirectory(prefix='release-input-') as temp:
            directory = Path(temp)
            if args.action == 'promote':
                if not args.candidate_commit or not args.acceptance:
                    raise ValueError('candidate commit and acceptance required')
                commit = export_commit(args.repo, args.candidate_commit, directory)
                manifest, validation = verify(directory, args.repo)
                verify_baseline_evidence(args.repo, manifest, validation)
                verify_pinned_commit(args.repo, directory, json.loads((directory / 'report.json').read_text()))
                acceptance = json.loads(args.acceptance.read_text())
                verify_acceptance(acceptance, manifest, validation)
                (directory / 'acceptance.json').write_text(json.dumps(acceptance, indent=2) + chr(10))
                metadata = {'action': 'promote', 'candidate_commit': commit, 'candidate_id': manifest['candidate_id']}
                baseline = manifest['baseline_commit']
            else:
                if not args.release_commit or not args.reason:
                    raise ValueError('release commit and rollback reason required')
                git(args.repo, 'fetch', 'origin', 'refs/heads/dist:refs/remotes/origin/dist')
                baseline = git(args.repo, 'rev-parse', 'refs/remotes/origin/dist')
                subprocess.run(['git', '-C', str(args.repo), 'merge-base', '--is-ancestor',
                                args.release_commit, baseline], check=True, capture_output=True)
                commit = export_commit(args.repo, args.release_commit, directory)
                manifest, validation = verify(directory)
                verify_pinned_commit(args.repo, directory, json.loads((directory / 'report.json').read_text()))
                previous = json.loads((directory / 'release.json').read_text())
                if previous['candidate_id'] != manifest['candidate_id']:
                    raise ValueError('rollback target was not a published verified release')
                verify_acceptance(json.loads((directory / 'acceptance.json').read_text()), manifest, validation)
                metadata = {'action': 'rollback', 'target_commit': commit, 'candidate_id': manifest['candidate_id'], 'reason': args.reason}
            result = publish(args.repo, directory, baseline, metadata, args.apply)
            print(json.dumps(result, indent=2))
            if args.apply:
                from scripts.check_remote import check
                report = json.loads((directory / 'report.json').read_text())
                print(json.dumps(check(report['repository'], result['commit'], report['output_sha256']), indent=2))
        return 0
    except (OSError, ValueError, KeyError, RuntimeError, subprocess.CalledProcessError) as error:
        print(str(error), file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
