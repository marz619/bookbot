import operator
import string
import sys
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
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {self.path.relative_to('.')}...")
        print("----------- Word Count ----------")
        print(f"Found {self.word_count()} total words")
        print("--------- Character Count -------")
        for c, count in self.char_counts_lower_sorted_tuples(reverse=True):
            print(f"{c}: {count}")
        print("============= END ===============")


def main(args: list[str]) -> int:
    # ensure an arg has been provided
    if not len(args):
        print("Usage: python3 main.py <path_to_book>")
        return 1
    # load the book and print the report
    Book(Path(args[0])).report()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
