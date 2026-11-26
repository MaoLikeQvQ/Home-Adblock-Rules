#!/usr/bin/env python3
"""Check published rule bytes by immutable GitHub commit. MIT."""
import argparse
import json
from pathlib import Path
import re
import sys
import time
import urllib.request

if __package__ in (None, ''):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts.validate import digest


def check(repository, commit, expected, attempts=4):
    if not re.fullmatch('[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository) or not re.fullmatch('[0-9a-f]{40}', commit):
        raise ValueError('invalid repository or immutable commit')
    for name, sha in expected.items():
        if name not in ('clash.yaml', 'clash-allow.yaml', 'adguard.txt'):
            raise ValueError('unexpected published output')
        url = f'https://raw.githubusercontent.com/{repository}/{commit}/{name}'
        error = None
        for attempt in range(attempts):
            try:
                with urllib.request.urlopen(url, timeout=20) as response:
                    data = response.read(32 * 1024 * 1024 + 1)
                if digest(data) != sha:
                    raise ValueError('published hash mismatch: ' + name)
                error = None
                break
            except (OSError, ValueError) as caught:
                error = caught
                if attempt + 1 < attempts:
                    time.sleep(2)
        if error:
            raise RuntimeError('publication exists but online verification pending/failed: ' + str(error))
    return {'status': 'verified', 'repository': repository, 'commit': commit, 'files': sorted(expected)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--publication', type=Path, required=True)
    parser.add_argument('--candidate', type=Path, required=True)
    args = parser.parse_args()
    publication = json.loads(args.publication.read_text())
    report = json.loads((args.candidate / 'report.json').read_text())
    try:
        print(json.dumps(check(report['repository'], publication['commit'], report['output_sha256']), indent=2))
        return 0
    except (OSError, ValueError, RuntimeError) as error:
        print(str(error), file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
