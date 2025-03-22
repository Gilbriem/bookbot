from stats import count_words, char_stats, convert_dict_to_list_of_dicts

import sys


def main():
    try:
        book_location = sys.argv[1]
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    wcount = count_words(book_location)
    stats = char_stats(book_location)
    chr_list = convert_dict_to_list_of_dicts(stats)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_location}")
    print("----------- Word Count ----------")
    print(f"Found {wcount} total words.")
    print("-------- Character Count --------")

    for item in chr_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["count"]}")

    print("============= END =============")






main()