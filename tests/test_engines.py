import json
import gzip
from pathlib import Path
import socket
import socketserver
import sys
import tempfile
import unittest
from unittest.mock import patch

from scripts.smoke_engines import DNSHandler, serve, dns_query, engine_process, install_engine, run, providers_ready, platform_id
from scripts.validate import digest


class EngineInfrastructureTests(unittest.TestCase):
    def test_router_architecture_is_not_assumed_to_be_arm64(self):
        self.assertEqual(platform_id('Linux', 'aarch64'), 'linux-arm64')
        self.assertEqual(platform_id('Linux', 'x86_64'), 'linux-amd64')
        self.assertEqual(platform_id('Linux', 'armv7l'), 'linux-unsupported')
        self.assertEqual(platform_id('Linux', 'mips'), 'linux-unsupported')
    def test_mihomo_api_can_start_before_provider_initialization(self):
        counts = {'clash_block': 100, 'clash_allow': 2}
        for providers in (None, {}, {'home-adblock': None},
                          {'home-adblock': {'ruleCount': 0}, 'home-adblock-allow': {'ruleCount': 2}}):
            self.assertFalse(providers_ready(providers, counts))
        self.assertTrue(providers_ready({'home-adblock': {'ruleCount': 100}}, counts))

    def test_controlled_dns_answers_both_address_families(self):
        with serve(socketserver.ThreadingUDPServer(('127.0.0.1', 0), DNSHandler)) as port:
            self.assertEqual(dns_query(port, 'fixture.example.test', 1), socket.inet_aton('192.0.2.123'))
            self.assertEqual(dns_query(port, 'fixture.example.test', 28), socket.inet_pton(socket.AF_INET6, '2001:db8::123'))

    def test_process_cleanup_after_failed_check(self):
        with tempfile.TemporaryDirectory() as temp:
            process = None
            with self.assertRaisesRegex(RuntimeError, 'fixture'):
                with engine_process([sys.executable, '-c', 'import time; time.sleep(30)'], Path(temp)) as child:
                    process = child
                    raise ValueError('fixture')
            self.assertIsNotNone(process.poll())

    def test_unconfigured_engine_is_incomplete(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            config = root / 'validation.json'
            config.write_text(json.dumps({'engines': {}}))
            scenarios = root / 'scenarios.json'
            scenarios.write_text(json.dumps({'schema_version': 1, 'cases': [{'id': 'case', 'host': 'fixture.example.test',
                                   'expected': 'block', 'query_types': ['A'], 'targets': ['clash']}]}))
            self.assertEqual(run(root, config, scenarios, root / 'cache')['status'], 'incomplete')

    def test_invalid_engine_pin_does_not_download(self):
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaisesRegex(ValueError, 'checksum'):
                install_engine({'url': 'https://example.test/file', 'sha256': 'not-a-pin', 'version': 'fixture'}, Path(temp), 'fixture')

    def test_cached_executable_is_atomically_replaced_not_overwritten(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            archive = gzip.compress(b'fixture executable')
            (root / 'engine.gz').write_bytes(archive)
            spec = {'url': 'https://example.test/engine.gz', 'sha256': digest(archive), 'version': 'fixture'}
            with patch('scripts.smoke_engines.urllib.request.urlopen') as download:
                target, binary_hash = install_engine(spec, root, 'fixture')
                first_inode = target.stat().st_ino
                second, _ = install_engine(spec, root, 'fixture')
                self.assertNotEqual(first_inode, second.stat().st_ino)
                self.assertEqual(second.read_bytes(), b'fixture executable')
                self.assertEqual(binary_hash, digest(second.read_bytes()))
                download.assert_not_called()

    def test_changed_output_is_rejected_before_starting_an_engine(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            config = root / 'validation.json'
            config.write_text(json.dumps({'engines': {'linux-amd64': {'mihomo': {}, 'adguard': {}}}}))
            scenarios = root / 'scenarios.json'
            scenarios.write_text(json.dumps({'schema_version': 1, 'cases': [
                {'id': 'case', 'host': 'fixture.example.test', 'expected': 'block',
                 'query_types': ['A'], 'targets': ['clash', 'adguard']}]}))
            names = ['clash.yaml', 'clash-allow.yaml', 'adguard.txt']
            for name in names:
                (root / name).write_text('changed fixture')
            (root / 'report.json').write_text(json.dumps({'output_sha256': {name: '0' * 64 for name in names}}))
            with patch('scripts.smoke_engines.platform.system', return_value='Linux'), \
                 patch('scripts.smoke_engines.platform.machine', return_value='x86_64'), \
                 patch('scripts.smoke_engines.install_engine') as install:
                with self.assertRaisesRegex(ValueError, 'changed before engine tests'):
                    run(root, config, scenarios, root / 'cache')
                install.assert_not_called()
