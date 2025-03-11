from stats import get_word_count, get_sorted_char_count_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents



def main():
    # file_path = "./books/frankenstein.txt"
    file_path = sys.argv[1]
    print(f"file_path is {file_path}")
    
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    text = get_book_text(file_path)
    
    print("----------- Word Count ----------")
    word_count = get_word_count(text)
    print(word_count)
    
    print("--------- Character Count -------")
    
    sorted_char_count_dict = get_sorted_char_count_dict(text)
    for c in sorted_char_count_dict:
        if not c["char"].isalpha():
            continue
        print(f"{c["char"]}: {c["count"]}")

main()
