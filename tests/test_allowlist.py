import unittest

from scripts.rules.allowlist import compile_allowlist, exclude, parse_compiled_rule
from scripts.rules.parsers import parse_classical


class AllowlistCompilationTests(unittest.TestCase):
    def test_suffix_allow_drops_only_covered_blocks(self):
        blocked = {'DOMAIN,api.safe.example.com', 'DOMAIN-SUFFIX,safe.example.com',
                   'DOMAIN-SUFFIX,child.safe.example.com', 'DOMAIN,unsafe.example.com'}
        compiled, decisions = compile_allowlist(blocked, {'DOMAIN-SUFFIX,safe.example.com'})
        self.assertEqual(compiled, {'DOMAIN,unsafe.example.com'})
        self.assertEqual(len(decisions), 3)
        self.assertTrue(all(d['decision'] == 'drop' for d in decisions))

    def test_exact_allow_keeps_children_and_partial_parent_block(self):
        blocked = {'DOMAIN,safe.example.com', 'DOMAIN-SUFFIX,safe.example.com',
                   'DOMAIN,child.safe.example.com'}
        compiled, _ = compile_allowlist(blocked, {'DOMAIN,safe.example.com'})
        self.assertEqual(compiled, {'DOMAIN,child.safe.example.com',
                                  exclude('DOMAIN-SUFFIX,safe.example.com', {'DOMAIN,safe.example.com'})})

    def test_parent_retains_both_exact_and_suffix_holes_in_one_rule(self):
        allowed = {'DOMAIN,api.example.com', 'DOMAIN-SUFFIX,cdn.example.com'}
        compiled, _ = compile_allowlist({'DOMAIN-SUFFIX,example.com'}, allowed)
        rule = compiled.pop()
        self.assertEqual(parse_compiled_rule(rule), rule)
        self.assertIn('OR,', rule)
        with self.assertRaises(ValueError):
            parse_classical('payload:\n  - ' + rule)
        self.assertEqual(parse_classical('payload:\n  - ' + rule, compiled=True), {rule})

    def test_keyword_and_ip_preserve_domain_exceptions_and_no_resolve(self):
        allowed = {'DOMAIN,safe.example.com', 'DOMAIN,allow-ad.example.com', 'DOMAIN-SUFFIX,cdn.example.com'}
        compiled, _ = compile_allowlist({'DOMAIN-KEYWORD,-ad', 'IP-CIDR,192.0.2.0/24,no-resolve'}, allowed)
        self.assertEqual(compiled, {exclude('DOMAIN-KEYWORD,-ad', allowed - {'DOMAIN,safe.example.com'}),
                                  exclude('IP-CIDR,192.0.2.0/24,no-resolve', allowed)})

    def test_generated_parser_rejects_route_actions_and_unknown_logic(self):
        rule = exclude('DOMAIN-SUFFIX,example.com', {'DOMAIN,api.example.com'})
        for broken in [rule + ',DIRECT', rule.replace('NOT,', 'OR,'),
                       rule.replace('DOMAIN,api.example.com', 'DOMAIN,api.example.com,REJECT'),
                       exclude('DOMAIN-SUFFIX,example.com', {'RULE-SET,external'})]:
            with self.subTest(rule=broken), self.assertRaises(ValueError):
                parse_compiled_rule(broken)
