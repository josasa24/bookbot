# Function prints the text from a given filepath
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

# Function gets the number of words in a text
def get_book_word_count(text):
    word_count = text.split()
    num_words = len(word_count)
    return num_words

# Function creates a unique list of lowercase letters and counts the number of each letter
def get_lowercase_letter_counter(text):
    lower_case_text = text.lower()
    my_set = set(lower_case_text)
    lowercase_dict = dict.fromkeys(my_set, 0)
    for i in lower_case_text:
        lowercase_dict[i] += 1
    return lowercase_dict

#Function converting dictionary to a sorted list
def dictionary_sort(text):
    lowercase_dict = get_lowercase_letter_counter(text)
    chars_list = []
    for char, count in lowercase_dict.items():
        # Only include alphabetical characters
        if char.isalpha():
            chars_list.append({"char": char, "count": count})
    
    # Sort the list by count in descending order
    chars_list.sort(key=lambda item: item["count"], reverse=True)
    return chars_list  # Return the sorted list, don't print it