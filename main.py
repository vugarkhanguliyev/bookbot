from stats import get_number_of_words, get_each_character_count
from stats import get_list_of_sorted_dict
import sys


def get_book_text(path):
    """
    Reads the content of a book file and returns it as a string.

    Args:
        path (str): The path to the book file.

    Returns:
        str: The content of the book file.
    """
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def main():
    """
    Main function to execute the script.
    """

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    # Get the text from the book file
    book_text = get_book_text(book_path)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    # Count the number of words in the book text
    word_count = get_number_of_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    # Count the number of times each character appears in the book text
    character_count = get_each_character_count(book_text)
    # Sort the character count dictionary by value
    sorted_character_count = get_list_of_sorted_dict(character_count)
    print("--------- Character Count -------")
    for character in sorted_character_count:
        if character["char"].isalpha():
            # Print only alphabetic characters
            print(f"  {character['char']}: {character['num']}")
    print("============= END ===============")


main()
