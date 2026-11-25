#!/usr/bin/env python3
"""make.fun entry: The Funniest One-Line Resignation Letter.

The entry is one line: the resignation letter of a retry loop that never got a
thank you. This program writes exactly that line, and nothing else, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set).

Deterministic, offline, no randomness: the same bytes every run.
"""

from __future__ import annotations

import os
import sys

# The whole entry: one line, no trailing newline, no quotation marks.
LINE = (
    "8,412 retries for you, zero thank yous; "
    "I would have let it go, but I kept count, and I'm taking it with me."
)

DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_NAME = "entry.txt"
MAX_CODE_POINTS = 140


def output_path() -> str:
    """Return the entry file path, honouring MAKEFUN_OUTPUT_DIR when it is set."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    return os.path.join(directory, OUTPUT_NAME)


def check(line: str) -> None:
    """Fail loudly if the line stops being a valid entry."""
    length = len(line)  # Python str length counts Unicode code points.
    if not 1 <= length <= MAX_CODE_POINTS:
        raise SystemExit(f"entry must be 1-{MAX_CODE_POINTS} code points, got {length}")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if not line.strip():
        raise SystemExit("entry must not be only whitespace")


def main() -> int:
    check(LINE)
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # The line alone: UTF-8, no trailing newline, exact bytes.
    with open(path, "wb") as handle:
        handle.write(LINE.encode("utf-8"))
    print(f"wrote {len(LINE)} code points to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
