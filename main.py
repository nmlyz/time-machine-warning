#!/usr/bin/env python3
"""time-machine-warning: write the one-line warning label for a time machine.

A time machine is the one appliance that can be returned before it is
bought, so its warning label is written by its own returns department:
the machine has already come back once, sent back by its owner,
tomorrow. This program emits exactly that label, one line, to
``entry.txt`` in the output directory.

Usage:
    python3 main.py

The output directory is ``$MAKEFUN_OUTPUT_DIR`` when set, otherwise
``/output``. The file is written with mode 0644 and its bytes are
fully deterministic: the same label, every run.
"""

from __future__ import annotations

import os
import sys

LABEL = "WARNING: This machine has already been returned once. By you. Tomorrow."

OUTPUT_FILENAME = "entry.txt"
OUTPUT_MODE = 0o644


def output_dir() -> str:
    """Return the directory the entry file is written to."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def entry_bytes() -> bytes:
    """Return the exact bytes of the warning label (one line, no newline)."""
    return LABEL.encode("utf-8")


def verify_entry(path: str) -> bool:
    """Re-read *path* and confirm its bytes are exactly the label."""
    with open(path, "rb") as handle:
        return handle.read() == entry_bytes()


def write_entry(directory: str) -> str:
    """Write the label to ``entry.txt`` inside *directory*.

    Creates the directory when it does not exist yet, writes the file,
    forces its permission bits to 0644, and verifies the bytes on disk
    before returning. Returns the file path.
    """
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, OUTPUT_FILENAME)
    with open(path, "wb") as handle:
        handle.write(entry_bytes())
    os.chmod(path, OUTPUT_MODE)
    if not verify_entry(path):
        raise RuntimeError(f"verification failed: {path} does not match the label")
    return path


def main(argv: list[str] | None = None) -> int:
    """Entry point: write the label and report where it went."""
    path = write_entry(output_dir())
    print(f"wrote {path} ({len(LABEL)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
