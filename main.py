def main():
    book_path = "./books/frankenstein.txt"
    book_content = get_book_text(book_path)
    num_words = get_word_count(book_content)
    print(f"Found {num_words} total words")

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(content):
    words_list = content.split()
    return len(words_list)

if __name__ == "__main__":
    main()
