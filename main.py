"""One-Liner Marathon entry.

Writes a single one-line comedy joke to /output/entry.txt.

The joke is a small parenting confession: a lie about the ice cream
truck that held for six years, ending on the image of a freezer full
of lies. The turn is the parent admitting the con with zero remorse,
which is where the laugh lands.
"""

import os

ENTRY = (
    "I told my kids the ice cream truck only plays music when it's out "
    "of ice cream. They believed me for six years. I have no regrets, "
    "only a freezer full of lies."
)


def validate(entry: str) -> None:
    """Enforce the competition gate before writing: 1-280 chars, one line."""
    if not (1 <= len(entry) <= 280):
        raise ValueError(f"entry is {len(entry)} characters, must be 1-280")
    if "\n" in entry or not entry.strip():
        raise ValueError("entry must be a single non-blank line")


def main() -> None:
    validate(ENTRY)
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
