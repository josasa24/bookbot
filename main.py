def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def main(book_text):
    print(book_text)

# Call the functions
book_text = get_book_text("books/frankenstein.txt")
main(book_text)

def number_of_words(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()