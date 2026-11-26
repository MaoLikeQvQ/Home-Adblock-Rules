import copy
import gzip
import json
from pathlib import Path
import tempfile
import unittest

from scripts.rules.protection import RuleIndex, apply_protection, load_policies
from scripts.validate import validate, seal
import test_build


def policy(domain='example.com'):
    return {'id': 'test', 'enabled': True, 'domain': domain, 'scope': 'suffix',
            'permitted_block_rules': [], 'reason': 'fixture',
            'evidence_level': 'upstream-reference', 'evidence': ['fixture'], 'reviewed_on': '2026-11-26'}


class ProtectionTests(unittest.TestCase):
    def test_all_origins_and_line_numbers_survive(self):
        index = RuleIndex()
        for source_id in ('first', 'second'):
            index.source({'id': source_id, 'format': 'adguard', 'targets': ['clash', 'adguard']},
                         '# comment' + chr(10) + '||api.example.com^' + chr(10))
        origins = index.origins[('clash', 'block', 'DOMAIN-SUFFIX,api.example.com')]
        self.assertEqual([o['source_id'] for o in origins], ['first', 'second'])
        self.assertTrue(all(o['line'] == 2 for o in origins))
        kept, decisions = apply_protection('clash', {'DOMAIN-SUFFIX,api.example.com'}, set(), [policy()], index)
        self.assertEqual(kept, set())
        self.assertEqual(len(decisions[0]['origins']), 2)

    def test_advertising_exception_and_video_protection(self):
        protection = policy()
        protection['permitted_block_rules'] = [{'domain': 'ads.example.com', 'scope': 'suffix'}]
        blocked = {'||video.example.com^', '||ads.example.com^'}
        kept, _ = apply_protection('adguard', blocked, set(), [protection], RuleIndex())
        self.assertEqual(kept, {'||ads.example.com^'})
        with self.assertRaisesRegex(ValueError, 'conflicts with allow'):
            apply_protection('adguard', blocked, {'||example.com^'}, [protection], RuleIndex())

    def test_parent_boundary_and_exact_protection_fail(self):
        protection = policy('api.example.com')
        with self.assertRaisesRegex(ValueError, 'boundary conflict'):
            apply_protection('clash', {'DOMAIN-SUFFIX,example.com'}, set(), [protection], RuleIndex())
        protection['scope'] = 'exact'
        with self.assertRaisesRegex(ValueError, 'boundary conflict'):
            apply_protection('clash', {'DOMAIN-SUFFIX,api.example.com'}, set(), [protection], RuleIndex())

    def test_local_cannot_bypass_protection(self):
        index = RuleIndex()
        rule = 'DOMAIN,api.example.com'
        index.add('clash', 'block', rule, {'source_id': 'local-block'})
        with self.assertRaisesRegex(ValueError, 'local block violates'):
            apply_protection('clash', {rule}, set(), [policy()], index)

    def test_non_domain_impact_requires_review(self):
        kept, decisions = apply_protection('clash', {'DOMAIN-KEYWORD,ad'}, set(), [policy()], RuleIndex())
        self.assertEqual(kept, {'DOMAIN-KEYWORD,ad'})
        self.assertEqual(decisions[0]['decision'], 'review')
        self.assertEqual(decisions[0]['analysis']['affected'][0]['host'], 'probead.example.com')

    def test_patterns_have_valid_protected_subdomain_witnesses(self):
        for target, rule in [('clash', 'DOMAIN-KEYWORD,-ad.sm.cn'), ('adguard', '*-ad.sm.cn*')]:
            _, decisions = apply_protection(target, {rule}, set(), [policy('gecko.snssdk.com')], RuleIndex())
            witness = decisions[0]['analysis']['affected'][0]['host']
            self.assertTrue(witness.endswith('.gecko.snssdk.com'))
            self.assertIn('-ad.sm.cn', witness)
            self.assertEqual(decisions[0]['check_id'], 'pattern-protection-intersection')

    def test_exact_protection_can_prove_literal_pattern_disjoint(self):
        protection = policy('api.example.com')
        protection['scope'] = 'exact'
        _, decisions = apply_protection('clash', {'DOMAIN-KEYWORD,unrelated'}, set(), [protection], RuleIndex())
        self.assertEqual(decisions[0]['decision'], 'keep')
        self.assertEqual(decisions[0]['analysis']['affected'], [])

    def test_no_resolve_ip_still_requires_destination_evidence(self):
        rule = 'IP-CIDR,192.0.2.1/32,no-resolve'
        _, decisions = apply_protection('clash', {rule}, set(), [policy()], RuleIndex())
        self.assertEqual(decisions[0]['analysis']['network'], '192.0.2.1/32')
        self.assertTrue(decisions[0]['analysis']['no_resolve'])
        self.assertEqual(decisions[0]['decision'], 'review')

    def test_strict_policy_validation(self):
        for modification in ('unknown', 'overlap', 'outside', 'bool', 'duplicate'):
            with self.subTest(modification=modification), tempfile.TemporaryDirectory() as temp:
                protection = policy()
                config = {'schema_version': 1, 'policies': [protection]}
                if modification == 'unknown':
                    protection['typo'] = True
                elif modification == 'overlap':
                    other = policy('api.example.com')
                    other['id'] = 'other'
                    config['policies'].append(other)
                elif modification == 'outside':
                    protection['permitted_block_rules'] = [{'domain': 'different.test', 'scope': 'exact'}]
                elif modification == 'bool':
                    protection['enabled'] = 'true'
                else:
                    config['policies'].append(copy.deepcopy(protection))
                path = Path(temp) / 'protection.json'
                path.write_text(json.dumps(config))
                with self.assertRaises(ValueError):
                    load_policies(path)


class IntegratedProtectionTests(unittest.TestCase):
    setUp = test_build.BuildTests.setUp
    generate = test_build.BuildTests.generate

    def test_build_failure_preserves_existing_output(self):
        self.generate()
        old = (self.output / 'clash.yaml').read_bytes()
        config = {'schema_version': 1, 'policies': [policy('api.example.com')]}
        (self.root / 'config/protection.json').write_text(json.dumps(config))
        with self.assertRaisesRegex(ValueError, 'boundary conflict'):
            self.generate()
        self.assertEqual((self.output / 'clash.yaml').read_bytes(), old)

    def test_origin_export_and_source_order_do_not_change_policy(self):
        self.source.write_text('||api.example.com^' + chr(10) + '||ad.other.test^' + chr(10))
        config = {'schema_version': 1, 'policies': [policy()]}
        (self.root / 'config/protection.json').write_text(json.dumps(config))
        sources_path = self.root / 'config/sources.json'
        sources = json.loads(sources_path.read_text())
        sources['sources'].append({**sources['sources'][0], 'id': 'other'})
        (self.inputs / 'other.txt').write_bytes(self.source.read_bytes())
        sources_path.write_text(json.dumps(sources))
        self.generate()
        old = (self.output / 'clash.yaml').read_bytes()
        sources['sources'].reverse()
        sources_path.write_text(json.dumps(sources))
        self.generate()
        self.assertEqual((self.output / 'clash.yaml').read_bytes(), old)
        records = [json.loads(line) for line in gzip.decompress((self.output / 'rules.jsonl.gz').read_bytes()).decode().splitlines()]
        self.assertTrue(any(len(item['origins']) == 2 for item in records))

    def test_validation_hashes_and_bootstrap(self):
        self.generate()
        config = self.root / 'config/validation.json'
        config.write_text(json.dumps({'schema_version': 1, 'added_ratio': .05, 'removed_ratio': .05, 'engines': {}}))
        result = validate(self.output, None, config)
        self.assertEqual(result['findings'][0]['id'], 'bootstrap-required')
        first = seal(self.output, self.root)
        self.assertEqual(first, seal(self.output, self.root))
        (self.output / 'adguard.txt').write_text('tampered')
        with self.assertRaisesRegex(ValueError, 'hash mismatch'):
            validate(self.output, None, config)
