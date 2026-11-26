#!/usr/bin/env python3
"""Make the Judge Laugh in One Line — entry runner.

Reads the one-liner from entry.txt (resolved relative to this file, never
the working directory) and writes it to /output/entry.txt.
"""
import re
from pathlib import Path

MAX_CHARS = 200


def load_line() -> str:
    path = Path(__file__).with_name("entry.txt")
    return path.read_text(encoding="utf-8").strip()


def normalize_line(line: str) -> str:
    """Collapse any run of whitespace to a single space and strip the ends,
    so the line reads cleanly out loud no matter how entry.txt is formatted."""
    return re.sub(r"\s+", " ", line).strip()


def validate_line(line: str) -> None:
    """Enforce the competition gate: 1-200 chars of real text, no bare
    whitespace, so the scorer marks the entry valid."""
    if not line:
        raise SystemExit("entry.txt is empty")
    if line != line.strip():
        raise SystemExit("line has leading or trailing whitespace")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"line is {len(line)} chars, over the 200 limit")


def main() -> None:
    line = normalize_line(load_line())
    validate_line(line)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(line + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
