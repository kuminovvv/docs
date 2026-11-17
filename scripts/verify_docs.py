#!/usr/bin/env python3
"""Minimal offline doc integrity check; no network or third-party packages."""
from pathlib import Path
from urllib.parse import unquote
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'AGENTS.md', 'agents.md', 'CLAUDE.md', 'REVIEW.md', 'README.md',
    'docs/README.md', 'docs/09-testing-and-verification.md',
    'docs/12-verification-techniques.md', 'docs/13-review-and-gates.md',
    'docs/14-security-and-privacy.md',
    'docs/frontend/README.md', 'docs/frontend/react-components.md',
    'docs/frontend/typescript.md', 'docs/frontend/nextjs.md',
    'docs/backend/README.md', 'docs/backend/go.md',
    'docs/backend/api-contracts.md', 'docs/backend/data-integrity.md',
    'docs/backend/testing.md', '.claude/skills/verify/SKILL.md',
]
errors = []
for name in REQUIRED:
    if not (ROOT / name).is_file():
        errors.append(f'missing required file: {name}')
for md in ROOT.rglob('*.md'):
    if '.git' in md.parts:
        continue
    text = md.read_text(encoding='utf8')
    if not text.strip():
        errors.append(f'empty file: {md.relative_to(ROOT)}')
    # Ignore external links, in-page anchors, inline code and images.
    # Local links only, hash anchors are allowed after the target file exists.
    for match in re.finditer(r'(?<!!)\[[^\]]+\]\(([^)]+)\)', text):
        url = match.group(1).strip().split(' ', 1)[0]
        if url.startswith(('https://', 'http://', 'mailto:', '#')):
            continue
        url = unquote(url.split('#', 1)[0].split('?', 1)[0])
        if not url:
            continue
        path = (md.parent / url).resolve()
        if not path.is_relative_to(ROOT) or not path.exists():
            errors.append(f'broken link {md.relative_to(ROOT)} -> {url}')
if errors:
    for err in errors:
        print('FAIL:', err)
    sys.exit(1)
print('PASS: required docs and internal relative links valid')
