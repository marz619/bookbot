import operator
import string
import sys
from io import StringIO
from pathlib import Path


class Book:
    def __init__(self, path: Path):
        self.path = path
        self.__contents = None

    def contents(self) -> str:
        if not self.__contents:
            with self.path.open() as f:
                self.__contents = f.read()
        return self.__contents

    def word_count(self) -> int:
        return len(self.contents().split())

    def char_counts_lower(self) -> dict[str, int]:
        counts = {}
        for c in self.contents():
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

    def report(self) -> str:
        buffer = StringIO()
        buffer.write("============ BOOKBOT ============\n")
        buffer.write(f"Analyzing book found at {self.path.relative_to('.')}...\n")
        buffer.write("----------- Word Count ----------\n")
        buffer.write(f"Found {self.word_count()} total words\n")
        buffer.write("--------- Character Count -------\n")
        for c, count in self.char_counts_lower_sorted_tuples(reverse=True):
            buffer.write(f"{c}: {count}\n")
        buffer.write("============= END ===============")
        return buffer.getvalue()


def main(args: list[str]) -> int:
    # ensure an arg has been provided
    if not len(args):
        print("Usage: python3 main.py <path_to_book> [path_to_book ...]")
        return 1
    # load the book and print the report
    for book_path in args:
        print(Book(Path(book_path)).report())
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
