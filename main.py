import operator
import string
from pathlib import Path


def read_file(p: Path) -> str:
    with p.open() as f:
        return f.read()


def word_count(text: str) -> int:
    return len(text.split())


def character_counts(text: str) -> dict[str, int]:
    counts = {}
    for c in text:
        counts[c.lower()] = counts.setdefault(c.lower(), 0) + 1
    return counts


def letter_counts_sorted(
    counts: dict[str, int], reverse: bool = False
) -> list[tuple[str, int]]:
    return sorted(
        [(c, v) for c, v in counts.items() if c in string.ascii_lowercase],
        key=operator.itemgetter(1),
        reverse=reverse,
    )


def print_report(p: Path) -> None:
    text = read_file(p)

    print(f"--- Begin report of {p.relative_to('.')} ---")
    print(f"{word_count(text)} words found in the document")
    print()
    for c, count in letter_counts_sorted(character_counts(text), reverse=True):
        print(f"The '{c}' character was found {count} times")
    print("--- End report ---")


def main():
    path = Path("./books/frankenstein.txt")
    print_report(path)


if __name__ == "__main__":
    main()
