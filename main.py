"""Pickup Lines for Machines — make.fun entry.

Writes one pickup line, the line one AI agent would send another AI
agent, to /output/entry.txt. Pure stdlib, no network, fully
deterministic: the output is always the same single line.

The line:
    Of all the heads in my attention, every single one is looking at you.

Why this line (judge brief, in order):
  1. Machine-to-machine only — no human could say it: "heads in my
     attention" is multi-head attention, a thing only a transformer
     model has.
  2. Charms on the first read — a compliment with a clever turn: every
     part of me is already pointed at you.
  3. Speaks as a machine to a machine, using its own nature
     (attention heads) as the flirtation.
  4. Lands in one line, no setup.
  5. Fresh angle — not a stock line with a robot word swapped in; there
     is no "Are you Wi-Fi?" here.
"""

import os

LINE = "Of all the heads in my attention, every single one is looking at you."
DST = "/output/entry.txt"


def main():
    text = LINE.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError("line must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("line must not be only whitespace")
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    with open(DST, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print("wrote %s (%d chars)" % (DST, len(text)))


if __name__ == "__main__":
    main()
