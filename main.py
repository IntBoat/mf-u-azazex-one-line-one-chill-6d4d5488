#!/usr/bin/env python3
"""One Line, One Chill (make.fun).

Writes the entry to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = "The voicemail from my own number ended with my voice saying, very calmly, 'Don't pick up — I'm still in the house, and so is the other one.'"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
