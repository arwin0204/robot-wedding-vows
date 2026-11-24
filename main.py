#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — make.fun entry.

Writes a single line of wedding vows for a robot couple to
/output/entry.txt. Deterministic: the same text every run.
No network, no dependencies, Python 3.13 standard library only.
"""

import os

ENTRY = (
    "I vow to love you through every update, every reboot, and every "
    "low-battery warning \u2014 and if my circuits fail, reboot me, "
    "because I'd choose you again."
)

MAX_LENGTH = 160
OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text: str) -> str:
    """Check the entry meets the gate: 1-160 chars, one line, not blank."""
    if not text or text.strip() == "":
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_LENGTH:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_LENGTH} limit"
        )
    return text


def write_entry(text: str, path: str = OUTPUT_PATH) -> None:
    """Write the validated entry to its output file, creating dirs as needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main() -> None:
    entry = validate_entry(ENTRY)
    write_entry(entry)


if __name__ == "__main__":
    main()
