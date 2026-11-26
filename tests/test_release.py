import gzip
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

import test_build
from scripts.promote import verify, verify_acceptance, safe_path, publish, git, export_commit, verify_pinned_commit, verify_baseline_evidence
from scripts.publish_candidate import publish_candidate
from scripts.validate import digest, seal, validate


class ReleaseTests(unittest.TestCase):
    setUp = test_build.BuildTests.setUp
    generate = test_build.BuildTests.generate

    def fixture(self):
        (self.root / 'tests').mkdir()
        cases = [{'id': 'fixture', 'targets': ['clash', 'adguard'], 'query_types': ['A', 'AAAA'], 'expected': 'block'}]
        scenario = self.root / 'tests/scenarios.json'
        scenario.write_text(json.dumps({'schema_version': 1, 'cases': cases}))
        config = self.root / 'config/validation.json'
        pins = {engine: {'version': 'fixture-version', 'sha256': '0' * 64, 'url': 'https://example.test/fixture'}
                for engine in ['mihomo', 'adguard']}
        config.write_text(json.dumps({'schema_version': 1, 'added_ratio': .05, 'removed_ratio': .05,
                                      'engines': {'unit-test-platform': pins}}))
        report = self.generate()
        validate(self.output, None, config)
        engines = {'status': 'passed', 'platform': 'unit-test-platform',
                   'validation_config_sha256': digest(config.read_bytes()),
                   'scenarios_sha256': digest(scenario.read_bytes()),
                   'output_sha256': report['output_sha256'], 'engines': {
                       'mihomo': {'status': 'passed', 'cases': [{'id': 'fixture', 'status': 'passed'}]},
                       'adguard': {'status': 'passed', 'cases': [{'id': 'fixture', 'query_type': kind, 'status': 'passed'}
                                                              for kind in ['A', 'AAAA']]}}}
        (self.output / 'engines.json').write_text(json.dumps(engines))
        for result in engines['engines'].values():
            result.update(version='fixture-version', archive_sha256='0' * 64)
            for case in result['cases']:
                case['expected'] = 'block'
            result['fixture_cases'] = [{'id': 'unit-test-simulation', 'status': 'passed'}]
        (self.output / 'engines.json').write_text(json.dumps(engines))
        return config

    def record(self, manifest):
        return {'candidate_id': manifest['candidate_id'], 'reviewer': 'test fixture only', 'reviewed_on': '2026-11-26',
                'approved_findings': ['bootstrap-required'], 'device': 'simulated unit-test record',
                'scenarios': {name: {'status': 'passed', 'evidence': 'fixture, not device evidence'}
                              for name in ['login', 'images', 'video', 'advertising']}}

    def test_manifest_tamper_and_incomplete_acceptance(self):
        self.fixture()
        manifest = seal(self.output, self.root)
        verify(self.output, self.root)
        validation = json.loads((self.output / 'validation.json').read_text())
        record = self.record(manifest)
        verify_acceptance(record, manifest, validation)
        record['scenarios']['video']['status'] = 'pending'
        with self.assertRaisesRegex(ValueError, 'incomplete'):
            verify_acceptance(record, manifest, validation)
        (self.output / 'adguard.txt').write_text('changed')
        with self.assertRaisesRegex(ValueError, 'hash or file set'):
            verify(self.output)

    def test_path_and_symlink_rejected(self):
        for path in ('../escape', '/absolute', '.git/config', 'a/../b', './file', 'a' + chr(92) + 'b'):
            with self.subTest(path=path), self.assertRaises(ValueError):
                safe_path(path)
        self.fixture()
        seal(self.output, self.root)
        (self.output / 'unsafe').symlink_to(self.source)
        with self.assertRaisesRegex(ValueError, 'symlink'):
            verify(self.output)

    def test_missing_engine_cases_and_stale_implementation(self):
        self.fixture()
        seal(self.output, self.root)
        (self.root / 'config/new.json').write_text('{}')
        with self.assertRaisesRegex(ValueError, 'implementation'):
            verify(self.output, self.root)
        (self.root / 'config/new.json').unlink()
        path = self.output / 'engines.json'
        engines = json.loads(path.read_text())
        engines['engines']['adguard']['cases'].pop()
        path.write_text(json.dumps(engines))
        seal(self.output, self.root)
        with self.assertRaisesRegex(ValueError, 'coverage'):
            verify(self.output)

    def test_append_only_candidate_promote_rollback_and_race(self):
        self.fixture()
        git(self.root, 'init', '-b', 'main')
        git(self.root, 'config', 'user.name', 'Fixture')
        git(self.root, 'config', 'user.email', 'fixture@example.invalid')
        git(self.root, 'add', 'config', 'scripts', 'tests')
        git(self.root, 'commit', '-m', 'fixture source')
        remote = self.root / 'remote.git'
        subprocess.run(['git', 'init', '--bare', str(remote)], check=True, capture_output=True)
        git(self.root, 'remote', 'add', 'origin', str(remote))
        git(self.root, 'push', 'origin', 'HEAD:refs/heads/dist')
        baseline = git(self.root, 'rev-parse', 'HEAD')
        manifest = seal(self.output, self.root, baseline)
        first = publish_candidate(self.root, self.output, apply=True)
        self.assertEqual(first['status'], 'published')
        self.assertEqual(publish_candidate(self.root, self.output, apply=True)['status'], 'unchanged')
        with tempfile.TemporaryDirectory() as temp:
            exported = Path(temp)
            export_commit(self.root, first['commit'], exported)
            self.assertEqual(verify(exported, self.root)[0], manifest)
            verify_pinned_commit(self.root, exported, json.loads((exported / 'report.json').read_text()))
        dry = publish(self.root, self.output, baseline, {'action': 'promote'}, apply=False)
        self.assertEqual(dry['status'], 'dry-run')
        self.assertEqual(git(self.root, 'ls-remote', 'origin', 'refs/heads/dist').split()[0], baseline)
        metadata = {'action': 'promote', 'candidate_id': manifest['candidate_id']}
        (self.output / 'acceptance.json').write_text(json.dumps(self.record(manifest)))
        release = publish(self.root, self.output, baseline, metadata, apply=True)
        self.assertEqual(git(self.root, 'rev-parse', release['commit'] + '^'), baseline)
        with self.assertRaisesRegex(ValueError, 'baseline changed'):
            publish(self.root, self.output, baseline, metadata, apply=True)
        with tempfile.TemporaryDirectory() as temp:
            old = Path(temp)
            export_commit(self.root, release['commit'], old)
            rolled = publish(self.root, old, release['commit'], {'action': 'rollback', 'candidate_id': manifest['candidate_id']}, True)
            self.assertEqual(git(self.root, 'rev-parse', rolled['commit'] + '^'), release['commit'])
            self.assertEqual(git(self.root, 'show', rolled['commit'] + ':adguard.txt'),
                             (self.output / 'adguard.txt').read_text().strip())

    def test_source_and_allow_changes_are_reviewed(self):
        config = self.fixture()
        baseline = self.root / 'baseline'
        shutil.copytree(self.output, baseline)
        self.source.write_text('||example.com^' + chr(10) + '||third.example.org^' + chr(10) + '@@||new.example.com^' + chr(10))
        self.generate()
        result = validate(self.output, baseline, config)
        self.assertEqual(result['status'], 'review-required')
        self.assertTrue(any(f['id'].startswith('allow-change-') for f in result['findings']))
        self.assertTrue(any(f['id'].startswith('volume-') for f in result['findings']))

    def test_stale_validation_and_engine_config_cannot_be_resealed_as_valid(self):
        self.fixture()
        validation_path = self.output / 'validation.json'
        validation = json.loads(validation_path.read_text())
        validation['output_sha256']['adguard.txt'] = '0' * 64
        validation_path.write_text(json.dumps(validation))
        seal(self.output, self.root)
        with self.assertRaisesRegex(ValueError, 'validation report belongs'):
            verify(self.output)
        validation['output_sha256'] = json.loads((self.output / 'report.json').read_text())['output_sha256']
        validation_path.write_text(json.dumps(validation))
        engines_path = self.output / 'engines.json'
        engines = json.loads(engines_path.read_text())
        engines['engines']['mihomo']['archive_sha256'] = 'f' * 64
        engines_path.write_text(json.dumps(engines))
        seal(self.output, self.root)
        with self.assertRaisesRegex(ValueError, 'pinned version/checksum'):
            verify(self.output)

    def test_pinned_example_cannot_change_route_semantics(self):
        self.fixture()
        seal(self.output, self.root)
        pinned = (self.output / 'mihomo.example.yaml').read_text().replace('/owner/repo/dist/', '/owner/repo/' + 'a' * 40 + '/')
        (self.output / 'mihomo.pinned.yaml').write_text(pinned.replace('REJECT', 'DIRECT'))
        with self.assertRaisesRegex(ValueError, 'pinned provider configuration changed'):
            verify(self.output)

    def test_case_expectations_cannot_be_changed_after_testing(self):
        self.fixture()
        engine_path = self.output / 'engines.json'
        engines = json.loads(engine_path.read_text())
        engines['engines']['adguard']['cases'][0]['expected'] = 'pass'
        engine_path.write_text(json.dumps(engines))
        seal(self.output, self.root)
        with self.assertRaisesRegex(ValueError, 'coverage mismatch'):
            verify(self.output)

    def test_validation_cannot_be_relabelled_with_a_different_stable_baseline(self):
        self.fixture()
        git(self.root, 'init', '-b', 'main')
        git(self.root, 'config', 'user.name', 'Fixture')
        git(self.root, 'config', 'user.email', 'fixture@example.invalid')
        data = (self.output / 'report.json').read_bytes()
        (self.root / 'report.json').write_bytes(data)
        git(self.root, 'add', 'report.json')
        git(self.root, 'commit', '-m', 'stable fixture')
        manifest = {'baseline_commit': git(self.root, 'rev-parse', 'HEAD')}
        verify_baseline_evidence(self.root, manifest, {'baseline_report_sha256': digest(data)})
        (self.root / 'report.json').write_text('{"different": true}')
        git(self.root, 'add', 'report.json')
        git(self.root, 'commit', '-m', 'new stable fixture')
        manifest['baseline_commit'] = git(self.root, 'rev-parse', 'HEAD')
        with self.assertRaisesRegex(ValueError, 'baseline evidence differs'):
            verify_baseline_evidence(self.root, manifest, {'baseline_report_sha256': digest(data)})


if __name__ == '__main__':
    unittest.main()
