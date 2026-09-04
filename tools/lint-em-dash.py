#!/usr/bin/env python3
"""Fail CI if em-dash is used as real prose punctuation.

Allowed (not flagged):
  - inside fenced code blocks (```...```)
  - inside blockquote lines (lines starting with >, i.e. quoted transcripts)
  - inline code spans (`...`)
  - meta-references where the em-dash is quoted/parenthesized on its own,
    e.g. "—", (—), karakter "—" — these are explanations ABOUT the character,
    not uses of it as punctuation.

Anything else (em-dash surrounded by spaces/words as a real dash) fails.
"""
import re
import sys
import glob

META_PATTERNS = [
    re.compile(r'"—"'),
    re.compile(r'\(—\)'),
    re.compile(r'karakter\s+"—"', re.IGNORECASE),
]

# whole-line exceptions: deliberate "wrong example" quotes, not real usage
LINE_EXCEPTION_PREFIXES = [
    "**Before:**",
    "**before:**",
]


def strip_code_blocks(text: str) -> str:
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = re.sub(r"`[^`\n]*`", "", text)
    lines = [ln for ln in text.split("\n") if not ln.lstrip().startswith(">")]
    return "\n".join(lines)


def find_violations(path: str):
    raw = open(path, encoding="utf-8").read()
    cleaned = strip_code_blocks(raw)
    for meta in META_PATTERNS:
        cleaned = meta.sub("", cleaned)
    # quoted example strings (deliberate "wrong" or transcript quotes), exempt content inside "..."
    cleaned = re.sub(r'"[^"\n]*—[^"\n]*"', "", cleaned)
    violations = []
    for i, line in enumerate(cleaned.split("\n"), 1):
        stripped = line.strip()
        if any(stripped.startswith(p) for p in LINE_EXCEPTION_PREFIXES):
            continue
        if "—" in line:
            violations.append((i, stripped))
    return violations


def main():
    files = sys.argv[1:] or glob.glob("**/*.md", recursive=True)
    files = [f for f in files if ".git/" not in f]
    failed = False
    for f in files:
        for lineno, line in find_violations(f):
            failed = True
            print(f"{f}:{lineno}: em-dash used as prose punctuation: {line}")
    if failed:
        print("\nFAILED: em-dash found in prose. Replace with comma, period, or connecting word.")
        sys.exit(1)
    print(f"OK: no em-dash prose violations in {len(files)} files.")


if __name__ == "__main__":
    main()
