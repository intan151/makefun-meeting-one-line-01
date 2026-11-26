#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line.

Writes the single sentence that could have replaced an entire pointless
meeting to /output/entry.txt (make.fun program/v1 entrypoint).

Deterministic: the same line, byte for byte, on every run.
"""

import os

ENTRY = (
    "This meeting is cancelled: the answer is yes, the deadline is Friday, "
    "and the email you're reading just saved us an hour."
)


def self_check(text: str) -> None:
    """Gate self-check: mirrors the sealed scorer's gate.

    entry.txt must be UTF-8 text of 1 to 200 characters, not only
    whitespace, and a single line / single sentence (this competition's
    entry is one line).
    """
    assert isinstance(text, str)
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1..200"
    assert text.strip(), "entry is only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert text == text.strip(), "entry has leading/trailing whitespace"
    assert text.endswith("."), "entry must be one sentence"
    assert text.count(".") == 1, "entry must be a single sentence"
    text.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    self_check(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    self_check(written)
    assert written == ENTRY, "written entry differs from ENTRY"
    print(f"wrote {path} ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
