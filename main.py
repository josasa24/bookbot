import sys
from stats import get_book_text, get_book_word_count, get_lowercase_letter_counter, dictionary_sort

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    word_count = get_book_word_count(book_text)
    lowercase_counter = get_lowercase_letter_counter(book_text)
    sorted_chars = dictionary_sort(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"{word_count} words found in the document")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        print(f"{char_dict['char']}: {char_dict['count']}")
    print("============= END ===============")

main()