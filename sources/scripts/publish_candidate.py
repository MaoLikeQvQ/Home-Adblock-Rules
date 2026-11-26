#!/usr/bin/env python3
"""Publish a sealed candidate using append-only Git history. MIT."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

if __package__ in (None, ''):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts.promote import ROOT, git, verify


def publish_candidate(repo, candidate, apply=False):
    manifest, _ = verify(candidate, repo)
    remote = git(repo, 'ls-remote', '--heads', 'origin', 'refs/heads/candidate')
    if not apply:
        return {'status': 'dry-run', 'candidate_id': manifest['candidate_id']}
    with tempfile.TemporaryDirectory(prefix='candidate-publish-') as temp:
        checkout = Path(temp) / 'checkout'
        if remote:
            git(repo, 'fetch', 'origin', 'refs/heads/candidate:refs/remotes/origin/candidate')
            reference = 'refs/remotes/origin/candidate'
            previous = json.loads(git(repo, 'show', reference + ':manifest.json'))
            if previous['candidate_id'] == manifest['candidate_id']:
                return {'status': 'unchanged', 'commit': git(repo, 'rev-parse', reference),
                        'candidate_id': manifest['candidate_id']}
        else:
            reference = 'HEAD'
        git(repo, 'worktree', 'add', '--detach', str(checkout), reference)
        try:
            if not remote:
                git(checkout, 'checkout', '--orphan', 'candidate-initial')
            git(checkout, 'rm', '-r', '-f', '--ignore-unmatch', '.')
            shutil.copytree(candidate, checkout, dirs_exist_ok=True)
            git(checkout, 'config', 'user.name', 'github-actions[bot]')
            git(checkout, 'config', 'user.email', '41898282+github-actions[bot]@users.noreply.github.com')
            git(checkout, 'add', '-A')
            unchanged = subprocess.run(['git', '-C', str(checkout), 'diff', '--cached', '--quiet']).returncode == 0
            if unchanged:
                return {'status': 'unchanged', 'commit': git(checkout, 'rev-parse', 'HEAD')}
            git(checkout, 'commit', '-m', 'chore: publish verified candidate ' + manifest['candidate_id'][:12])
            content_commit = git(checkout, 'rev-parse', 'HEAD')
            report = json.loads((candidate / 'report.json').read_text())
            old_base = f"https://raw.githubusercontent.com/{report['repository']}/dist"
            fixed_base = f"https://raw.githubusercontent.com/{report['repository']}/{content_commit}"
            pinned = (candidate / 'mihomo.example.yaml').read_text().replace(old_base, fixed_base)
            (checkout / 'mihomo.pinned.yaml').write_text(pinned)
            git(checkout, 'add', 'mihomo.pinned.yaml')
            git(checkout, 'commit', '-m', 'docs: pin paired providers to immutable rule commit')
            commit = git(checkout, 'rev-parse', 'HEAD')
            git(checkout, 'push', 'origin', 'HEAD:refs/heads/candidate')
            return {'status': 'published', 'commit': commit, 'candidate_id': manifest['candidate_id']}
        finally:
            git(repo, 'worktree', 'remove', '--force', str(checkout))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--candidate', type=Path, required=True)
    parser.add_argument('--repo', type=Path, default=ROOT)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    try:
        print(json.dumps(publish_candidate(args.repo, args.candidate, args.apply), indent=2))
        return 0
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as error:
        print(str(error), file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
