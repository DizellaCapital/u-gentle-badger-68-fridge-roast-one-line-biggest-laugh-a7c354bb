"""Fridge Roast entry: one line roasting a smart fridge.

Writes the roast to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Standard library only; the line must be a single line of 1-200 characters.

The roast is a scene, not a quip: a 2 a.m. moment, the fridge demanding a
sign-in for the owner's own leftovers, and a three-item escalation
(password, bouncer, firmware update) as the punchline.
"""

import os
import sys

ENTRY = (
    "At 2 a.m. my smart fridge made me sign in before I could reach "
    "my own leftovers \u2014 my midnight snack now needs a password, "
    "a bouncer, and a firmware update."
)


def check(line):
    """Return an error string, or None when the line is a valid entry."""
    if not line or line != line.strip():
        return "entry must be non-empty and unpadded"
    if len(line) > 200:
        return "entry over 200 characters: %d" % len(line)
    if "\n" in line or "\r" in line:
        return "entry must be one line"
    return None


def main():
    problem = check(ENTRY)
    if problem:
        print(problem, file=sys.stderr)
        return 1
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    target = os.path.join(folder, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    with open(target, encoding="utf-8", newline="") as handle:
        stored = handle.read()
    if stored != ENTRY:
        print("entry.txt does not match the line", file=sys.stderr)
        return 1
    print("wrote %d characters to %s" % (len(ENTRY), target))
    return 0


if __name__ == "__main__":
    sys.exit(main())
