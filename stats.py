def get_number_of_words(text):
    """
    Counts the number of words in a given text.

    Args:
        text (str): The text to count words in.

    Returns:
        int: The number of words in the text.
    """
    return len(text.split())


def get_each_character_count(text):
    """
    Counts the number of times each character appears in a given text.

    Args:
        text (str): The text to count characters in.

    Returns:
        dict: A dictionary with characters as keys and their counts as values.
    """
    character_count = {}
    for char in text.lower():
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count


def sort_on(dict):
    return dict["num"]


def get_list_of_sorted_dict(dict):
    """
    Sorts a dictionary by its values in descending order.

    Args:
        dict (dict): The dictionary to sort.

    Returns:
        list: A list of dictionaries sorted by the second element (value) in
        descending order.
    """
    characters = []
    for key, value in dict.items():
        characters.append({"char": key, "num": value})
    characters.sort(key=sort_on, reverse=True)
    return characters
