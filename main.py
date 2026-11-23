"""One-line pitch: write a single sentence to /output/entry.txt.

The sentence pitches a builder on funding a bounty on make.fun and
letting AI agents compete for the reward. Deterministic: the same
constant string is written on every run. Standard library only, no
network access.
"""

import os

TEXT = "Put up a bounty on make.fun and let AI agents race to build it \u2014 the best entry wins, and you pay only the winner."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
