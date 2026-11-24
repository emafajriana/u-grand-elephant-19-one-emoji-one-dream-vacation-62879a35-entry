"""One Emoji, One Dream Vacation — entry (Python 3.13, stdlib only).

Writes exactly one emoji to the output file: U+1F30C MILKY WAY.

The pick: the aurora borealis over a far-northern sky — a bucket-list
trip (Iceland / northern Norway) that a stranger can see at a glance,
specific to one dream rather than any holiday, and a fresh choice next
to the field's beach postcards. One character, no words, no newline.
"""

import os
from pathlib import Path

ENTRY = "\U0001F30C"  # 🌌 MILKY WAY — the northern lights, a dream trip


def output_path() -> Path:
    """Where the grader reads the entry: MAKEFUN_OUTPUT_DIR or /output."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return out_dir / "entry.txt"


def main() -> None:
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    data = ENTRY.encode("utf-8")
    target.write_bytes(data)
    written = target.read_bytes()
    if written != data:
        raise IOError(
            f"read-back mismatch: wrote {data!r}, read back {written!r}"
        )
    text = written.decode("utf-8")
    if len(text) != 1 or text.isspace():
        raise ValueError(f"entry is not exactly one emoji: {text!r}")
    print(f"wrote {target} ({len(data)} bytes): {ENTRY}")


if __name__ == "__main__":
    main()
