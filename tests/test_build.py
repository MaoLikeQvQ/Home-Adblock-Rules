import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from scripts.build import (
    adguard_to_classical, build, classical_to_adguard, domain, local_rules,
    parse_adguard, parse_classical, pin_sources,
)


class ParsingTests(unittest.TestCase):
    def test_domain_scope_and_ip_are_preserved(self):
        rules = parse_classical("""# notice
payload:
  - DOMAIN,Ads.Example.com
  - 'DOMAIN-SUFFIX,example.net'
  - IP-CIDR,192.0.2.3/32,no-resolve
  - DOMAIN-KEYWORD,-ad.example
""")
        self.assertEqual(rules, {"DOMAIN,ads.example.com", "DOMAIN-SUFFIX,example.net",
                                 "IP-CIDR,192.0.2.3/32,no-resolve", "DOMAIN-KEYWORD,-ad.example"})

    def test_adguard_exceptions_survive_conversion(self):
        blocked, allowed = parse_adguard("! notice\n||example.com^\n@@||api.example.com^\n|exact.example.org^\n")
        self.assertEqual(adguard_to_classical(allowed), {"DOMAIN-SUFFIX,api.example.com"})
        self.assertEqual(adguard_to_classical(blocked), {"DOMAIN-SUFFIX,example.com", "DOMAIN,exact.example.org"})

    def test_classical_exact_is_not_widened(self):
        rules, omitted = classical_to_adguard({"DOMAIN,ads.example.com", "DOMAIN-SUFFIX,example.net", "IP-CIDR,192.0.2.1/32"})
        self.assertEqual(rules, {"|ads.example.com^", "||example.net^"})
        self.assertEqual(omitted, ["IP-CIDR,192.0.2.1/32"])

    def test_native_wildcard_is_not_turned_into_suffix(self):
        blocked, _ = parse_adguard("*-ad.example.com*\n")
        self.assertEqual(blocked, {"*-ad.example.com*"})
        with self.assertRaises(ValueError):
            adguard_to_classical(blocked)

    def test_upstream_dns_names_do_not_become_network_rules(self):
        blocked, _ = parse_adguard("||103.179.189.35^\n||fb_servpub-a.akamaihd.net^\n")
        self.assertEqual(adguard_to_classical(blocked), {
            "DOMAIN-SUFFIX,103.179.189.35", "DOMAIN-SUFFIX,fb_servpub-a.akamaihd.net"})

    def test_conditional_rule_is_rejected(self):
        for rule in ["||example.com^$third-party", "@@||example.com^$client=abc", "example.com/path", "<html>oops</html>"]:
            with self.subTest(rule=rule), self.assertRaises(ValueError):
                parse_adguard(rule)

    def test_invalid_domains(self):
        for value in ["localhost", "127.0.0.1", "-ads.example.com", "ad..example.com", "*.example.com"]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                domain(value)

    def test_idna(self):
        self.assertEqual(domain("广告.example"), "xn--4rr70v.example")

    def test_classical_rejects_policy_field(self):
        with self.assertRaises(ValueError):
            parse_classical("payload:\n  - DOMAIN,example.com,REJECT\n")

    def test_whitelist_does_not_accept_keyword(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "allowlist.txt"
            path.write_text("DOMAIN-KEYWORD,example\n")
            with self.assertRaises(ValueError):
                local_rules(path, allow=True)

    def test_github_sources_are_pinned_to_one_commit_per_branch(self):
        sources = [{"id": "one", "url": "https://raw.githubusercontent.com/owner/repo/main/one.txt"},
                   {"id": "two", "url": "https://raw.githubusercontent.com/owner/repo/main/two.txt"}]
        commit = "a" * 40
        response = json.dumps({"object": {"type": "commit", "sha": commit}}).encode()
        with patch("scripts.build.fetch", return_value=response) as mocked:
            evidence = pin_sources(sources)
        self.assertEqual(mocked.call_count, 1)
        self.assertEqual(evidence["two"]["resolved_url"], f"https://raw.githubusercontent.com/owner/repo/{commit}/two.txt")


class BuildTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "config").mkdir()
        (self.root / "scripts").mkdir()
        (self.root / "licenses").mkdir()
        self.inputs = self.root / "inputs"
        self.inputs.mkdir()
        self.output = self.root / "dist"
        sources = [{"id": "test", "url": "https://example.com/list", "format": "adguard",
                    "targets": ["clash", "adguard"], "min_rules": 2}]
        (self.root / "config/sources.json").write_text(json.dumps({"sources": sources}))
        (self.root / "config/blocklist.txt").write_text("DOMAIN,local.example.org\n")
        (self.root / "config/allowlist.txt").write_text("DOMAIN,local.example.org\nDOMAIN-SUFFIX,custom.example.com\n")
        for name in ["LICENSE", "NOTICE.md", "scripts/build.py", "licenses/AWAvenue-LICENSE", "licenses/217heidai-LICENSE", "licenses/home-dns-adblock-LICENSE"]:
            (self.root / name).write_text("fixture\n")
        self.source = self.inputs / "test.txt"
        self.source.write_text("||example.com^\n||other.example.net^\n||example.com^\n@@||api.example.com^\n")

    def generate(self):
        return build(self.root, self.output, "owner/repo", self.inputs)

    def test_normal_entrypoint_merge_allowlist_and_attribution(self):
        report = self.generate()
        self.assertEqual(report["counts"], {"clash_block": 2, "clash_allow": 3, "adguard_block": 2, "adguard_allow": 3})
        allow = (self.output / "clash-allow.yaml").read_text()
        self.assertIn("DOMAIN-SUFFIX,api.example.com", allow)
        self.assertNotIn("DOMAIN,local.example.org", (self.output / "clash.yaml").read_text())
        self.assertIn("@@||api.example.com^", (self.output / "adguard.txt").read_text())
        example = (self.output / "mihomo.example.yaml").read_text()
        self.assertIn("AND,((RULE-SET,home-adblock),(NOT,((RULE-SET,home-adblock-allow)))),REJECT", example)
        self.assertNotIn("home-adblock-allow,DIRECT", example)
        self.assertIn("https://raw.githubusercontent.com/owner/repo/dist/", example)
        self.assertEqual((self.output / "sources/test.txt").read_bytes(), self.source.read_bytes())
        self.assertTrue((self.output / "sources/licenses/AWAvenue-LICENSE").exists())

    def test_repeated_build_is_byte_identical(self):
        self.generate()
        snapshot = {p.relative_to(self.output): p.read_bytes() for p in self.output.rglob("*") if p.is_file()}
        self.generate()
        self.assertEqual(snapshot, {p.relative_to(self.output): p.read_bytes() for p in self.output.rglob("*") if p.is_file()})

    def test_failure_preserves_previous_outputs(self):
        self.generate()
        previous = (self.output / "clash.yaml").read_bytes()
        for broken in ["<html>not a list</html>", "||only.example.com^\n"]:
            self.source.write_text(broken)
            with self.subTest(broken=broken), self.assertRaises(ValueError):
                self.generate()
            self.assertEqual((self.output / "clash.yaml").read_bytes(), previous)

    def test_missing_source_preserves_previous_outputs(self):
        self.generate()
        previous = (self.output / "report.json").read_bytes()
        self.source.unlink()
        with self.assertRaises(OSError):
            self.generate()
        self.assertEqual((self.output / "report.json").read_bytes(), previous)

    def test_sharp_drop_above_minimum_is_rejected(self):
        self.source.write_text("".join(f"||ad{i}.example.com^\n" for i in range(10)))
        self.generate()
        previous = (self.output / "report.json").read_bytes()
        self.source.write_text("||ad0.example.com^\n||ad1.example.com^\n")
        with self.assertRaisesRegex(ValueError, "dropped"):
            self.generate()
        self.assertEqual((self.output / "report.json").read_bytes(), previous)

    def test_source_contribution_is_based_on_actual_rules(self):
        config = self.root / "config/sources.json"
        sources = json.loads(config.read_text())
        second = {**sources["sources"][0], "id": "second"}
        sources["sources"].append(second)
        config.write_text(json.dumps(sources))
        (self.inputs / "second.txt").write_text("||example.com^\n||new.example.org^\n")
        report = self.generate()
        summary = report["sources"][1]["contribution"]["adguard"]
        self.assertEqual(summary["input_block_rules"], 2)
        self.assertEqual(summary["added_after_previous_sources"], 1)
        self.assertEqual(summary["duplicates_with_previous_sources"], 1)
        self.assertEqual(summary["exclusive_examples"], ["||new.example.org^"])
        self.assertTrue((self.output / "SOURCES.md").exists())
        self.assertIn("adguard.txt", report["output_sha256"])

    def test_tampered_source_snapshot_is_rejected(self):
        self.generate()
        snapshot = self.output / "sources/test.txt"
        snapshot.write_text("||tampered.example.com^\n||other.example.net^\n")
        with self.assertRaisesRegex(ValueError, "hash mismatch"):
            build(self.root, self.output, "owner/repo", self.output / "sources")

    def test_pinned_live_build_can_be_reproduced_offline(self):
        config = self.root / "config/sources.json"
        sources = json.loads(config.read_text())
        sources["sources"][0]["url"] = "https://raw.githubusercontent.com/owner/repo/main/rules.txt"
        config.write_text(json.dumps(sources))
        data = self.source.read_bytes()
        def response(url):
            if url.startswith("https://api.github.com/"):
                return json.dumps({"object": {"type": "commit", "sha": "a" * 40}}).encode()
            self.assertIn("/" + "a" * 40 + "/", url)
            return data
        with patch("scripts.build.fetch", side_effect=response):
            build(self.root, self.output, "owner/repo")
        previous = {p.relative_to(self.output): p.read_bytes() for p in self.output.rglob("*") if p.is_file()}
        build(self.root, self.output, "owner/repo", self.output / "sources")
        self.assertEqual(previous, {p.relative_to(self.output): p.read_bytes() for p in self.output.rglob("*") if p.is_file()})

    def test_home_dns_is_a_required_full_source(self):
        root = Path(__file__).resolve().parents[1]
        sources = json.loads((root / "config/sources.json").read_text())["sources"]
        source = next(item for item in sources if item["id"] == "home-dns")
        self.assertEqual(source["targets"], ["clash", "adguard"])
        self.assertTrue(source["url"].endswith("/dist/adguard-dns-full.txt"))


if __name__ == "__main__":
    unittest.main()
