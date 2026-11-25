#!/usr/bin/env python3
"""Two Robots in an Elevator -- one line of awkward robot small talk.

Writes a single line (under 200 characters) to entry.txt inside the
output directory given by MAKEFUN_OUTPUT_DIR, defaulting to /output.
Stdlib only; fully deterministic -- the same line every run.
"""

import os

LINE = (
    "So... do you also pretend to study the floor numbers to avoid "
    "eye contact, or is my social protocol just outdated firmware?"
)

# The sealed gate accepts 1-200 characters; fail loudly rather than
# ever writing an invalid entry.
assert 1 <= len(LINE) <= 200, "entry line must be 1-200 characters"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
