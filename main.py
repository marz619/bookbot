def character_counts(text: str) -> dict[str, int]:
    counts = {}
    for c in text:
         counts[c.lower()] = counts.setdefault(c.lower(), 0) + 1
    return counts


def main():
    text = None
    with open("./books/frankenstein.txt") as f:
        text = f.read()
    char_counts = character_counts(text)
    print(char_counts)


if __name__ == "__main__":
    main()

