import operator
import string
from pathlib import Path


class Book:
    def __init__(self, path: Path):
        self.path = path
        self.__contents = None

    def read(self) -> str:
        if not self.__contents:
            with self.path.open() as f:
                self.__contents = f.read()
        return self.__contents

    def word_count(self) -> int:
        return len(self.read().split())

    def char_counts_lower(self) -> dict[str, int]:
        counts = {}
        for c in self.read():
            counts[c.lower()] = counts.setdefault(c.lower(), 0) + 1
        return counts

    def char_counts_lower_sorted_tuples(
        self, reverse: bool = False
    ) -> list[tuple[str, int]]:
        return sorted(
            [
                (c, v)
                for c, v in self.char_counts_lower().items()
                if c in string.ascii_lowercase
            ],
            key=operator.itemgetter(1),
            reverse=reverse,
        )

    def report(self) -> None:
        print(f"--- Begin report of {self.path.relative_to('.')} ---")
        print(f"{self.word_count()} words found in the document")
        print()
        for c, count in self.char_counts_lower_sorted_tuples():
            print(f"The '{c}' character was found {count} times")
        print("--- End report ---")


def main():
    frankenstein = Book(Path("./books/frankenstein.txt"))
    frankenstein.report()


if __name__ == "__main__":
    main()
