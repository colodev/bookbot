import sys

from stats import word_count, char_count, chars_dict_to_sorted_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    
    text = get_book_text(path)
    wc = word_count(text)
    cc = char_count(text)
    sc = chars_dict_to_sorted_list(cc)

    print("============ BOOKBOT ============")
    print("Analyzing book found at " + path)
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    for char_dict in sc:
        if char_dict["char"].isalpha():
            print(char_dict["char"] + ": "  + str(char_dict["count"]))
    print("============= END ===============")


if __name__ == "__main__":
    main()