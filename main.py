import sys

from stats import (
    get_num_words, 
    character_counter, 
    sort_on, 
    sorted_characters,
)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    chars_dict = character_counter(text)
    chars_sorted_list = sorted_characters(character_counter(text))
    print_report(book_path, num_words, chars_sorted_list)

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}.")
    print("----------- Word Count ------------")
    print(f"Found {num_words} total words")
    print("----------- Character Count -------")
    for item in chars_sorted_list:
        print(f"{item["name"]}: {item["num"]}")

    print("============== END ==============")

if len(sys.argv) >= 2:
    main()
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

