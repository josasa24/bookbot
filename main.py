# Import the functions
from stats import get_book_text
from stats import get_book_word_count
from stats import get_lowercase_letter_counter

# Define the texts
frankenstein_txt = get_book_text("books/frankenstein.txt")
# mobydick_txt = get_book_text("books/mobydick.txt")

get_lowercase_letter_counter(frankenstein_txt)