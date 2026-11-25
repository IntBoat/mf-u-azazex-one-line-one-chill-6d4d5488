#!/usr/bin/env python3
"""One Line, One Chill — a make.fun one-line entry."""

from pathlib import Path

ENTRY = "The baby monitor crackled at 3 a.m. and whispered my own voice back, asking why I had stopped answering it."

OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
