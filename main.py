#!/usr/bin/env python3
"""time-machine-warning: write one warning label for a time machine to /output/entry.txt.

The label is worded like a printed notice stuck to the machine itself:
a WARNING header, then a returns notice whose last two words turn the
whole thing into a causal loop. Standard library only, no network.
Deterministic: the same bytes on every run.
"""

import os
import sys

# The label is built from three parts, so each part can be checked on its
# own: the printed-label header, the statement of fact, and the two-beat
# punchline that turns the statement into a causal loop. The surprise is
# saved for the last few words, and the whole line is 71 characters,
# inside the 120-character limit for the label.
HEADER = "WARNING:"
NOTICE = ("This machine has already been returned once. "
          "By you. Tomorrow.")

LINE = HEADER + " " + NOTICE

MIN_LEN = 1
MAX_LEN = 120


def problems(text: str) -> list:
    """Return every gate violation for the entry text (empty means valid)."""
    found = []
    if not (MIN_LEN <= len(text) <= MAX_LEN):
        found.append(f"entry is {len(text)} code points, must be {MIN_LEN}-{MAX_LEN}")
    stripped = text.strip()
    if not stripped:
        found.append("entry must not be only white space")
    if text != stripped:
        found.append("entry must not start or end with white space")
    if "\n" in text or "\r" in text:
        found.append("entry must be a single line")
    if not stripped.endswith("."):
        found.append("entry must end with a full stop")
    return found


def main() -> int:
    text = LINE
    bad = problems(text)
    if bad:
        for item in bad:
            print(item, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # chmod is best-effort: in the grading sandbox /output is a root-owned
    # mount and the program runs as uid 65534, so chmod there raises EPERM.
    # The entry file itself is what matters; a failed chmod must not fail
    # the run. (The output directory itself is never chmodded or removed.)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    # Read the file back as bytes and confirm they match the line exactly.
    with open(path, "rb") as f:
        if f.read() != text.encode("utf-8"):
            print("entry.txt does not match the label line", file=sys.stderr)
            return 1
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
