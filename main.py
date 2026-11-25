"""One Line, One Laugh — entry program.

Writes a single funny line (under 200 characters) to /output/entry.txt.
The line stands alone: no picture, no setup, punchline lands at the end.
"""

from pathlib import Path

ENTRY = "I asked my AI assistant to make me laugh, so it showed me my screen time report."

# The gate allows 1-200 characters; fail loudly here rather than
# shipping an entry the scorer would refuse.
assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, gate allows 1-200"

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
