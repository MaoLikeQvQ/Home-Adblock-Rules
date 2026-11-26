#!/usr/bin/env python3
"""Isolated real-engine tests with controlled DNS/HTTP. SPDX-License-Identifier: MIT."""
import argparse
from contextlib import contextmanager
import functools
import gzip
import hashlib
import http.server
import io
import json
import os
import platform
from pathlib import Path
import socket
import socketserver
import struct
import subprocess
import sys
import tarfile
import tempfile
import threading
import time
import urllib.request
import urllib.error
import zipfile

if __package__ in (None, ''):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts.validate import digest
from scripts.rules.protection import witness_scenarios

ROOT = Path(__file__).resolve().parent.parent
OPENER = urllib.request.build_opener(urllib.request.ProxyHandler({}))


def platform_id(system, machine):
    architecture = {'amd64': 'amd64', 'x86_64': 'amd64', 'arm64': 'arm64', 'aarch64': 'arm64'}.get(machine.lower())
    return system.lower() + '-' + (architecture or 'unsupported')


def get_json(url):
    with OPENER.open(url, timeout=2) as response:
        return json.load(response)


def free_port():
    with socket.socket() as listener:
        listener.bind(('127.0.0.1', 0))
        return listener.getsockname()[1]


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *_):
        pass


class DNSHandler(socketserver.BaseRequestHandler):
    def handle(self):
        packet, sock = self.request
        pos = 12
        while pos < len(packet) and packet[pos]:
            pos += 1 + packet[pos]
        if pos + 5 > len(packet):
            return
        qtype = struct.unpack('!H', packet[pos + 1:pos + 3])[0]
        value = socket.inet_pton(socket.AF_INET6, '2001:db8::123') if qtype == 28 else socket.inet_aton('192.0.2.123')
        question = packet[12:pos + 5]
        answer = bytes([192, 12]) + struct.pack('!HHIH', qtype, 1, 10, len(value)) + value
        response = packet[:2] + struct.pack('!5H', 0x8180, 1, 1, 0, 0) + question + answer
        sock.sendto(response, self.client_address)


@contextmanager
def serve(server):
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield server.server_address[1]
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)


@contextmanager
def engine_process(command, directory):
    with (directory / 'runtime.log').open('w') as log:
        process = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT)
        try:
            yield process
        except Exception as error:
            log.flush()
            details = (directory / 'runtime.log').read_text(errors='replace')[-6000:]
            raise RuntimeError(str(error) + chr(10) + details) from error
        finally:
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait(timeout=5)


def wait_ready(process, check, seconds=40):
    deadline = time.monotonic() + seconds
    while time.monotonic() < deadline:
        if process.poll() is not None:
            raise RuntimeError('engine exited before readiness: exit=' + str(process.returncode))
        try:
            if check():
                return
        except (OSError, ValueError, KeyError):
            pass
        time.sleep(.15)
    raise TimeoutError('engine readiness timed out')


def install_engine(spec, cache, name):
    if set(spec) != {'version', 'url', 'sha256'} or not spec['url'].startswith('https://'):
        raise ValueError('invalid engine specification')
    if len(spec['sha256']) != 64 or any(c not in '0123456789abcdef' for c in spec['sha256']):
        raise ValueError('invalid engine checksum')
    cache.mkdir(parents=True, exist_ok=True)
    archive = cache / spec['url'].rsplit('/', 1)[1]
    if not archive.exists() or digest(archive.read_bytes()) != spec['sha256']:
        with urllib.request.urlopen(spec['url'], timeout=60) as response:
            data = response.read(100 * 1024 * 1024 + 1)
        if len(data) > 100 * 1024 * 1024 or digest(data) != spec['sha256']:
            raise ValueError('engine download checksum mismatch')
        archive.write_bytes(data)
    data = archive.read_bytes()
    if archive.name.endswith('.zip'):
        with zipfile.ZipFile(io.BytesIO(data)) as bundle:
            members = [n for n in bundle.namelist() if n.endswith('/AdGuardHome')]
            if len(members) != 1:
                raise ValueError('unexpected engine archive')
            binary = bundle.read(members[0])
    elif archive.name.endswith('.tar.gz'):
        with tarfile.open(fileobj=io.BytesIO(data), mode='r:gz') as bundle:
            members = [n for n in bundle.getmembers() if n.isfile() and n.name.endswith('/AdGuardHome')]
            if len(members) != 1:
                raise ValueError('unexpected engine archive')
            binary = bundle.extractfile(members[0]).read()
    else:
        binary = gzip.decompress(data)
    target = cache / (name + '-' + spec['sha256'][:16])
    # Replacing a signed executable in place can invalidate macOS's cached
    # signature, and a concurrent test must never see a partially written file.
    with tempfile.NamedTemporaryFile(dir=cache, prefix=name + '-', delete=False) as temporary:
        temporary.write(binary)
        temporary_path = Path(temporary.name)
    try:
        temporary_path.chmod(0o700)
        os.replace(temporary_path, target)
    finally:
        temporary_path.unlink(missing_ok=True)
    return target.resolve(), digest(binary)


def dns_query(port, host, kind):
    labels = b''.join(bytes([len(x)]) + x.encode() for x in host.split('.')) + b'\0'
    packet = struct.pack('!6H', 1234, 0x100, 1, 0, 0, 0) + labels + struct.pack('!2H', kind, 1)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.settimeout(3)
        sock.sendto(packet, ('127.0.0.1', port))
        reply = sock.recv(4096)
    if reply[:2] != packet[:2] or reply[3] & 15:
        raise ValueError('unexpected DNS reply')
    address = reply[-(16 if kind == 28 else 4):]
    return address


def providers_ready(providers, counts):
    if not isinstance(providers, dict) or not all(
            isinstance(providers.get(name), dict) for name in ('home-adblock', 'home-adblock-allow')):
        return False
    return (providers['home-adblock'].get('ruleCount') == counts['clash_block'] and
            providers['home-adblock-allow'].get('ruleCount') == counts['clash_allow'])


def check_mihomo(binary, candidate, cases, directory, http_port):
    api, proxy = free_port(), free_port()
    base = f'http://127.0.0.1:{http_port}'
    hosts = ''.join('  ' + case['host'] + ': ' + case.get('destination_ip', '127.0.0.1') + chr(10) for case in cases)
    config = f'''mixed-port: {proxy}
allow-lan: false
mode: rule
log-level: info
external-controller: 127.0.0.1:{api}
hosts:
{hosts}rule-providers:
  home-adblock:
    type: http
    behavior: classical
    url: {base}/clash.yaml
    path: ./block.yaml
    interval: 28800
  home-adblock-allow:
    type: http
    behavior: classical
    url: {base}/clash-allow.yaml
    path: ./allow.yaml
    interval: 28800
rules:
  - AND,((RULE-SET,home-adblock),(NOT,((RULE-SET,home-adblock-allow)))),REJECT
  - MATCH,DIRECT
'''
    (directory / 'config.yaml').write_text(config)
    counts = json.loads((candidate / 'report.json').read_text())['counts']
    results = []
    with engine_process([str(binary), '-d', str(directory)], directory) as process:
        def ready():
            providers = get_json(f'http://127.0.0.1:{api}/providers/rules')['providers']
            return providers_ready(providers, counts)
        wait_ready(process, ready)
        for case in cases:
            request = urllib.request.Request(f"http://{case['host']}:{http_port}/report.json")
            request.set_proxy(f'127.0.0.1:{proxy}', 'http')
            try:
                with OPENER.open(request, timeout=4) as response:
                    response.read()
            except OSError:
                pass
            expected = 'using REJECT' if case['expected'] == 'block' else 'match Match using DIRECT'
            deadline = time.monotonic() + 3
            matched = None
            while time.monotonic() < deadline:
                for line in (directory / 'runtime.log').read_text().splitlines():
                    if f"--> {case['host']}:{http_port}" in line and expected in line:
                        matched = line
                if matched:
                    break
                time.sleep(.05)
            if not matched:
                raise ValueError('Mihomo mismatch: ' + case['id'])
            results.append({'id': case['id'], 'status': 'passed', 'expected': case['expected']})
    return results


def check_adguard(binary, candidate, cases, directory, http_port, upstream):
    web, dns = free_port(), free_port()
    config = f'''http:
  address: 127.0.0.1:{web}
users: []
dns:
  bind_hosts: [127.0.0.1]
  port: {dns}
  # Isolated loopback test traffic is deliberately bursty; the production
  # default rate limit would drop test queries after the first 20 per second.
  ratelimit: 0
  upstream_dns: ['127.0.0.1:{upstream}']
  bootstrap_dns: []
  use_private_ptr_resolvers: false
  serve_plain_dns: true
filtering:
  protection_enabled: true
  filtering_enabled: true
  blocking_mode: default
filters:
  - enabled: true
    url: http://127.0.0.1:{http_port}/adguard.txt
    name: candidate
    id: 1
schema_version: 35
'''
    path = directory / 'AdGuardHome.yaml'
    path.write_text(config)
    results = []
    command = [str(binary), '-w', str(directory), '-c', str(path), '--no-check-update', '--no-permcheck']
    counts = json.loads((candidate / 'report.json').read_text())['counts']
    with engine_process(command, directory) as process:
        def ready():
            status = get_json(f'http://127.0.0.1:{web}/control/filtering/status')
            if not status.get('filters'):
                return False
            loaded = status['filters'][0].get('rules_count', 0) == counts['adguard_block'] + counts['adguard_allow']
            if not loaded:
                return False
            # The filter metadata can be updated before the replacement matcher
            # is ready; wait for the actual known block to be evaluated as well.
            blocked_case = next((c for c in cases if c['expected'] == 'block'), None)
            if blocked_case is None:
                raise ValueError('AdGuard readiness requires a block scenario')
            check = get_json(f"http://127.0.0.1:{web}/control/filtering/check_host?name={blocked_case['host']}")
            return check['reason'].startswith('Filtered')
        wait_ready(process, ready)
        for case in cases:
            for kind_name in case['query_types']:
                kind = 1 if kind_name == 'A' else 28
                check = get_json(f"http://127.0.0.1:{web}/control/filtering/check_host?name={case['host']}&qtype={kind_name}")
                blocked = check['reason'].startswith('Filtered')
                if blocked != (case['expected'] == 'block'):
                    raise ValueError('AdGuard match mismatch: ' + case['id'] + ' ' + str(check))
                try:
                    address = dns_query(dns, case['host'], kind)
                except OSError as error:
                    raise RuntimeError(f"AdGuard DNS request failed: {case['id']} {kind_name}: {error}") from error
                expected = bytes(len(address)) if blocked else socket.inet_pton(
                    socket.AF_INET if kind == 1 else socket.AF_INET6, '192.0.2.123' if kind == 1 else '2001:db8::123')
                if address != expected:
                    raise ValueError('AdGuard DNS answer mismatch: ' + case['id'])
                results.append({'id': case['id'], 'query_type': kind_name, 'status': 'passed',
                                'reason': check['reason'], 'expected': case['expected']})
    return results


def prepare_fixture(directory):
    from scripts.build import yaml_payload
    from scripts.rules.protection import apply_protection, RuleIndex
    from scripts.rules.parsers import classical_to_adguard
    blocked = {'DOMAIN,ads.example.test', 'DOMAIN-SUFFIX,tracker.example.test',
               'DOMAIN-SUFFIX,content.video.example.test', 'DOMAIN-SUFFIX,ads.video.example.test',
               'DOMAIN-KEYWORD,fixture-keyword', 'IP-CIDR,127.0.0.2/32,no-resolve'}
    allowed = {'DOMAIN,allow.tracker.example.test'}
    policy = {'id': 'fixture-video', 'enabled': True, 'domain': 'video.example.test', 'scope': 'suffix',
              'reason': 'controlled fixture', 'permitted_block_rules': [{'domain': 'ads.video.example.test', 'scope': 'suffix'}]}
    blocked, _ = apply_protection('clash', blocked, allowed, [policy], RuleIndex())
    (directory / 'clash.yaml').write_text(yaml_payload(blocked, '# fixture' + chr(10)))
    (directory / 'clash-allow.yaml').write_text(yaml_payload(allowed, '# fixture' + chr(10)))
    dns_block, _ = classical_to_adguard(blocked)
    dns_block.add('*fixture-keyword*')
    dns_allow, _ = classical_to_adguard(allowed)
    (directory / 'adguard.txt').write_text(chr(10).join(sorted(dns_block) + ['@@' + x for x in sorted(dns_allow)]) + chr(10))
    counts = {'clash_block': len(blocked), 'clash_allow': len(allowed),
              'adguard_block': len(dns_block), 'adguard_allow': len(dns_allow)}
    (directory / 'report.json').write_text(json.dumps({'counts': counts}))
    cases = []
    for host, expected in [('ads.example.test', 'block'), ('child.ads.example.test', 'pass'),
                           ('notads.example.test', 'pass'), ('tracker.example.test', 'block'),
                           ('child.tracker.example.test', 'block'), ('allow.tracker.example.test', 'pass'),
                           ('content.video.example.test', 'pass'), ('ads.video.example.test', 'block'),
                           ('a-fixture-keyword.example.test', 'block')]:
        cases.append({'id': 'fixture-' + host, 'host': host, 'expected': expected,
                      'targets': ['clash', 'adguard'], 'query_types': ['A', 'AAAA']})
    cases.append({'id': 'fixture-ip', 'host': '127.0.0.2', 'destination_ip': '127.0.0.2',
                  'expected': 'block', 'targets': ['clash'], 'query_types': ['A']})
    return cases


def run(candidate, config, scenarios, cache):
    config_data = json.loads(config.read_text())
    scenario_data = json.loads(scenarios.read_text())
    cases = scenario_data['cases']
    ids = set()
    if scenario_data['schema_version'] != 1 or not cases:
        raise ValueError('missing scenarios')
    for case in cases:
        if case['id'] in ids or case['expected'] not in ('pass', 'block') or not case['targets']:
            raise ValueError('invalid scenario')
        ids.add(case['id'])
        if not set(case['targets']) <= {'clash', 'adguard'} or not set(case['query_types']) <= {'A', 'AAAA'}:
            raise ValueError('invalid scenario target/type')
        if not case['query_types']:
            raise ValueError('missing query types')
        from scripts.rules.parsers import domain
        domain(case['host'])
    selected_platform = platform_id(platform.system(), platform.machine())
    specs = config_data['engines'].get(selected_platform)
    if specs is None or set(specs) != {'mihomo', 'adguard'}:
        return {'status': 'incomplete', 'reason': 'No verified engine pins for ' + selected_platform}
    from scripts.validate import read_rules
    report = json.loads((candidate / 'report.json').read_text())
    if set(report['output_sha256']) != {'clash.yaml', 'clash-allow.yaml', 'adguard.txt'}:
        raise ValueError('missing rule output hashes')
    for name, expected_hash in report['output_sha256'].items():
        if digest((candidate / name).read_bytes()) != expected_hash:
            raise ValueError('candidate rules changed before engine tests: ' + name)
    actual_counts = {name: len(rules) for name, rules in read_rules(candidate).items()}
    if actual_counts != report['counts']:
        raise ValueError('candidate rule counts disagree with parsed outputs')
    for relative, supplied in [('config/validation.json', config), ('tests/scenarios.json', scenarios)]:
        snapshot = candidate / 'sources' / relative
        if not snapshot.is_file() or snapshot.read_bytes() != supplied.read_bytes():
            raise ValueError('engine test configuration differs from candidate snapshot: ' + relative)
    result = {'schema_version': 1, 'status': 'passed', 'platform': selected_platform,
              'scenarios_sha256': digest(scenarios.read_bytes()), 'engines': {},
              'validation_config_sha256': digest(config.read_bytes()),
              'output_sha256': report['output_sha256']}
    handler = functools.partial(QuietHandler, directory=str(candidate.resolve()))
    with tempfile.TemporaryDirectory(prefix='adblock-engines-') as temporary:
        work = Path(temporary).resolve()
        fixture = work / 'fixture'
        fixture.mkdir()
        fixture_cases = prepare_fixture(fixture)
        fixture_handler = functools.partial(QuietHandler, directory=str(fixture))
        with serve(http.server.ThreadingHTTPServer(('127.0.0.1', 0), handler)) as http_port:
            with serve(socketserver.ThreadingUDPServer(('127.0.0.1', 0), DNSHandler)) as dns_port:
                for engine, target in [('mihomo', 'clash'), ('adguard', 'adguard')]:
                    selected = [case for case in cases if target in case['targets']]
                    witnesses = witness_scenarios(candidate, target)
                    if not selected:
                        raise ValueError('missing engine scenarios')
                    binary, binary_hash = install_engine(specs[engine], cache, engine)
                    directory = work / engine
                    directory.mkdir()
                    if engine == 'mihomo':
                        checks = check_mihomo(binary, candidate, selected + witnesses, directory, http_port)
                    else:
                        checks = check_adguard(binary, candidate, selected + witnesses, directory, http_port, dns_port)
                    witness_ids = {case['id'] for case in witnesses}
                    witness_checks = [case for case in checks if case['id'] in witness_ids]
                    checks = [case for case in checks if case['id'] not in witness_ids]
                    fixture_run = work / (engine + '-fixture')
                    fixture_run.mkdir()
                    selected_fixture = [c for c in fixture_cases if target in c['targets']]
                    with serve(http.server.ThreadingHTTPServer(('127.0.0.1', 0), fixture_handler)) as fixture_port:
                        if engine == 'mihomo':
                            fixture_results = check_mihomo(binary, fixture, selected_fixture, fixture_run, fixture_port)
                        else:
                            fixture_results = check_adguard(binary, fixture, selected_fixture, fixture_run, fixture_port, dns_port)
                    result['engines'][engine] = {'version': specs[engine]['version'], 'archive_sha256': specs[engine]['sha256'],
                                                 'binary_sha256': binary_hash, 'cases': checks,
                                                 'protection_witness_cases': witness_checks,
                                                 'fixture_cases': fixture_results, 'status': 'passed'}
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--candidate', type=Path, required=True)
    parser.add_argument('--config', type=Path, default=ROOT / 'config/validation.json')
    parser.add_argument('--scenarios', type=Path, default=ROOT / 'tests/scenarios.json')
    parser.add_argument('--cache', type=Path, default=ROOT / '.engine-cache')
    args = parser.parse_args()
    try:
        result = run(args.candidate, args.config, args.scenarios, args.cache)
    except (OSError, ValueError, KeyError, RuntimeError) as error:
        result = {'status': 'failed', 'reason': str(error)}
    (args.candidate / 'engines.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + chr(10))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return {'passed': 0, 'incomplete': 3}.get(result['status'], 1)


if __name__ == '__main__':
    sys.exit(main())
