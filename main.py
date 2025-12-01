from stats import get_word_count, count_chars, sort_output
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_content = get_book_text(book_path)
    num_words = get_word_count(book_content)
    chars_count_dict = count_chars(book_content)
    sorted_list = sort_output(chars_count_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_list:
        if char_dict["char"].isalpha():
            print(f"{char_dict["char"]}: {char_dict["num"]}")

def get_book_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents

if __name__ == "__main__":
    main()
