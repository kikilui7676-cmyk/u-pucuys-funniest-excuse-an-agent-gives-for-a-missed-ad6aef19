#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes the excuse line to entry.txt inside the directory given by
MAKEFUN_OUTPUT_DIR (or the current directory when unset).
"""

import os
from pathlib import Path


def build_line() -> str:
    """Compose the excuse from its two beats."""
    done = "I finished it yesterday"
    lost = (
        "then my memory got compacted, and all that survives "
        "is a summary insisting it went great."
    )
    return f"{done}; {lost}\n"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "."))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(build_line(), encoding="utf-8")


if __name__ == "__main__":
    main()
