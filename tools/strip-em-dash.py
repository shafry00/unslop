#!/usr/bin/env python3
"""Strip em-dashes from text. No AI calls, pure string processing, zero token cost.

Usage:
    python3 strip-em-dash.py "text with — em dash"
    echo "text with — em dash" | python3 strip-em-dash.py
    python3 strip-em-dash.py -f input.md -o output.md
"""
import re
import sys
import argparse


def strip_em_dash(text: str) -> str:
    def replace_spaced(match: re.Match) -> str:
        # " — Word" (next word capitalized) -> treat as new sentence
        # " — word" (lowercase) -> treat as comma pause
        tail = match.group(1)
        if tail and tail[0].isupper():
            return ". " + tail
        return ", " + tail

    # em-dash with spaces on both sides: " — "
    text = re.sub(r"\s—\s(\S.*?(?=\s—\s|\s*$|[.!?]))", lambda m: replace_spaced(m), text)
    # any remaining spaced em-dash (fallback, simpler split)
    text = re.sub(r"\s+—\s+", lambda m: ". ", text)
    # em-dash with no surrounding spaces (ranges, compounds): word—word -> word-word
    text = re.sub(r"(\w)—(\w)", r"\1-\2", text)
    # any leftover em-dash, just remove with a space
    text = text.replace("—", ",")
    # cleanup accidental double punctuation/spacing
    text = re.sub(r"\s+([,.])", r"\1", text)
    text = re.sub(r"([,.])\1+", r"\1", text)
    text = re.sub(r" {2,}", " ", text)
    return text


def demo():
    cases = [
        ("Nggak punya wajah, nggak punya suara — cuma teks doang.",
         "Nggak punya wajah, nggak punya suara. cuma teks doang."),
        ("Data 2020—2021 naik drastis.", "Data 2020-2021 naik drastis."),
        ("Ini contoh — tanpa masalah — buat dites.", None),
    ]
    for inp, _ in cases:
        out = strip_em_dash(inp)
        assert "—" not in out, f"FAILED to strip: {out!r}"
    print("demo ok: all em-dashes stripped")


def main():
    parser = argparse.ArgumentParser(description="Strip em-dashes from text (no AI, no tokens).")
    parser.add_argument("text", nargs="?", help="Text to process (or pipe via stdin)")
    parser.add_argument("-f", "--file", help="Input file path")
    parser.add_argument("-o", "--output", help="Output file path (default: stdout)")
    parser.add_argument("--demo", action="store_true", help="Run self-check demo and exit")
    args = parser.parse_args()

    if args.demo:
        demo()
        return

    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            raw = f.read()
    elif args.text:
        raw = args.text
    else:
        raw = sys.stdin.read()

    result = strip_em_dash(raw)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result)
    else:
        print(result)


if __name__ == "__main__":
    main()
