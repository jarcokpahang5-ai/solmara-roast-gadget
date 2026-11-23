#!/usr/bin/env python3
"""One-line roast entry for make.fun's
"One-Line Roast: The Gadget You Use Every Day" bounty.

Holds a single original roast line of at most 200 characters aimed at a
gadget used every day, validates it, prints it, and writes it to
/output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
"""

import os
import re

LINE = (
    "My robot vacuum mapped my house in perfect detail, "
    "then spends twenty minutes a day getting stuck under "
    "the same chair it has mapped a hundred times."
)

OUTPUT_PATH = "/output/entry.txt"

# A sentence terminator only counts as a sentence break when followed by a
# space or the end of the string.
_SENTENCE_END = re.compile(r"[.!?](?=\s|$)")


def validate_line(line: str) -> str:
    """Validate the line is a single sentence of 1..200 characters."""
    if not isinstance(line, str):
        raise ValueError("line must be a string")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1..200 characters, got {len(line)}")
    if len(_SENTENCE_END.findall(line)) != 1:
        raise ValueError("line must be exactly one sentence")
    return line


def main() -> None:
    line = validate_line(LINE)
    print(line)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
