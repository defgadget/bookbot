def count_letters(text: str) -> list[dict]:
    lowered_string = text.lower()
    print(lowered_string)
    letters_count = {}
    for char in lowered_string:
        if char not in letters_count:
            letters_count[char] = 1
        else:
            letters_count[char] += 1

    letters_list = []
    for letter, count in letters_count.items():
        letters_list.append({"letter": letter, "count": count})
    return letters_list


def count_words(text: str) -> int:
    words = text.split()
    return len(words)


def open_book(path: str) -> str:
    with open(path) as f:
        file_contents = f.read()

    return file_contents


def sort_on(items: dict) -> int:
    return items["count"]


def print_report(book: str, words: int, letters: list[dict]) -> None:
    print(f"--- Begin report of {book} ---")
    print(f"{words} words found in the document")
    print()
    print()


    letters.sort(reverse=True, key=sort_on)
    for letter in letters:
        if not letter["letter"].isalpha():
            continue
        print(f"The '{letter["letter"]}' character was found {letter["count"]} times")
    print("--- End Report ---")


def main():
    book_path = "./books/frankenstein.txt"
    book_text = open_book(book_path)
    words = count_words(book_text)
    letters = count_letters(book_text)
    print_report(book_path, words, letters)


main()
