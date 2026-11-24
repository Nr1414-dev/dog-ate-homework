#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

Writes one line, under 200 characters, in which a dog explains why the
homework got eaten. Dog logic: no homework means no school, and no school
means the human stays home with the dog all day.
"""
import os

ENTRY = "I ate your homework so there's no homework, and no homework means no school, and no school means you stay home with me all day."


def main():
    # Gate guard: the sealed scorer requires UTF-8 text of 1 to 200
    # characters, not only white space. Refuse to write an invalid entry.
    if not (1 <= len(ENTRY) <= 200) or not ENTRY.strip():
        raise SystemExit("entry fails the 1-200 character gate")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    # Read-back check: what landed on disk must be exactly the entry.
    with open(path, encoding="utf-8") as f:
        if f.read() != ENTRY:
            raise SystemExit("read-back mismatch")


if __name__ == "__main__":
    main()
