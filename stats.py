# Function prints the text from a given filepath
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

# Function gets the number of words in a text
def get_book_word_count(filepath):
    with open(filepath) as w:
        word_count = w.read().split()
        num_words = len(word_count)
    return print(f"{num_words} words found in the document")

# Function creates a unique list of lowercase letters and counts the number of each letter
def get_lowercase_letter_counter(text):
    lower_case_text = text.lower()
    my_set = set(lower_case_text)
    lowercase_dict = dict.fromkeys(my_set, 0)
    for i in lower_case_text:
        lowercase_dict[i] += 1
    return print(f"{lowercase_dict}")