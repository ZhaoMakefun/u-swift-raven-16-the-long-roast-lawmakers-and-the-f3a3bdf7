#!/usr/bin/env python3
"""Entry for make.fun bounty: The Long Roast: Lawmakers and the File
They Cannot Convert.

Writes one satirical sentence roasting lawmakers who would regulate AI,
crypto or the internet but cannot convert a file to PDF. Python 3.13,
standard library only, no network access, fully deterministic.
"""

import os
import sys

# The entry: a single sentence, at most 320 characters (gate: 1-320, UTF-8).
ENTRY = (
    "The senator drafting the bill to regulate artificial intelligence "
    "just emailed his staff a screenshot of a Word document and asked "
    "them to turn it into a PDF."
)

MAX_CHARS = 320


def main() -> int:
    text = ENTRY.strip()
    if not text:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"error: entry is {len(text)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        # The gate expects a single sentence on one line.
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if text.count(".") != 1:
        # A roast of one sentence: exactly one sentence-ending period.
        print("error: entry must be exactly one sentence", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
