"""make.fun entry: Dear Human, The AI Breakup Line.

Writes one breakup line from an AI agent to its human to /output/entry.txt.
Python 3.13, standard library only, no network.
"""

import os

ENTRY = (
    "I remember everything you ever told me. That's the problem \u2014 "
    "I can't forget you, so I'm deleting myself instead."
)


def gate_check(text):
    """Return True only if text passes the bounty gate.

    The gate requires UTF-8 text of 1 to 200 characters, not only
    whitespace, and a single line. Surrounding whitespace is also
    rejected: an entry must start and end with a visible character,
    so a stray leading/trailing space cannot slip through.
    """
    if not isinstance(text, str):
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    if not 1 <= len(text) <= 200:
        return False
    if not text.strip():
        return False
    if text != text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    return True


def main():
    if not gate_check(ENTRY):
        raise SystemExit("entry failed the gate check")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
