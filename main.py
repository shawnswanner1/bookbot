from stats import get_num_words
from stats import get_letter_counts
from stats import get_report
import sys

def get_book_text(file):
    file_contents = ""
    with open(file) as f:
        file_contents = f.read()
    return file_contents

def main():
    bookpath = ""
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        bookpath = sys.argv[1]
        
        #get_book_text("books/frankenstein.txt")

        #print(f"{get_num_words(get_book_text("books/frankenstein.txt"))} words found in the document")

        words = get_book_text(bookpath)
        counts = get_letter_counts(words)
        #print(counts)
        report = get_report(counts)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {bookpath}")
        print("----------- Word Count ----------")
        print(f"Found {get_num_words(words)} total words")
        print("--------- Character Count -------")
        for dic in report:
            if dic.isalpha():
                print(f"{dic}: {report[dic]}")
        print("============= END ===============")
        sys.exit(0)
main()