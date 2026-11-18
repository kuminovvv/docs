#!/usr/bin/env python3
"""Проверка целостности автономного пакета backend; без зависимостей и сетевых обращений."""
from pathlib import Path
from urllib.parse import unquote
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "AGENTS.md", "CLAUDE.md", "REVIEW.md", "README.md",
    "docs/README.md", "docs/00-overview.md", "docs/01-context-loading.md",
    "docs/02-task-workflow.md", "docs/09-testing-and-verification.md",
    "docs/10-git-and-delivery.md", "docs/12-verification-techniques.md",
    "docs/13-review-and-gates.md", "docs/14-security-and-privacy.md",
    "docs/15-project-overrides.md", "docs/templates/project-profile.md",
    "docs/templates/verification-report.md",
    ".claude/skills/verify/SKILL.md", ".github/workflows/docs-check.yml",
    "docs/go.md",
    "docs/api-contracts.md",
    "docs/data-integrity.md",
    "docs/testing.md",
    "docs/observability.md"
]
errors = []
for name in REQUIRED:
    if not (ROOT / name).is_file():
        errors.append(f"missing required file: {name}")
for md in ROOT.rglob("*.md"):
    if ".git" in md.parts:
        continue
    text = md.read_text(encoding="utf8")
    if not text.strip():
        errors.append(f"empty file: {md.relative_to(ROOT)}")
    for match in re.finditer(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", text):
        url = match.group(1).strip().split(" ", 1)[0]
        if url.startswith(("https://", "http://", "mailto:", "#")):
            continue
        url = unquote(url.split("#", 1)[0].split("?", 1)[0])
        if not url:
            continue
        target = (md.parent / url).resolve()
        if not target.is_relative_to(ROOT) or not target.exists():
            errors.append(f"broken link {md.relative_to(ROOT)} -> {url}")
if errors:
    for error in errors:
        print("FAIL:", error)
    sys.exit(1)
print("PASS: required files and internal links for backend")
