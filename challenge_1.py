"""
Write a function named ``first_non_repeating_letter``† that takes a string input, and returns the first character that is not repeated anywhere in the string.

For example, if given the input ``stress``, the function should return ``t``, since the letter ``t`` only occurs once in the string, and occurs first in the string.

As an **added challenge**, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input ``sTreSS`` should return ``T``.

If a string contains all repeating characters, it should return an empty string ``("")``;

*† Note: the function is called firstNonRepeatingLetter for historical reasons, but your function should handle any Unicode character.*
"""
from typing import Dict, List


def first_non_repeating_letter(string: str) -> str:
    """
    This function returns the first character that is not repeated anywhere in the string.
    :param string:
    :return:
    """
    # Convert the string to lowercase to treat uppercase and lowercase letters as the same
    s_lower: str = string.lower()

    # Create a dictionary to store the count of each character
    char_count: Dict[str, int] = {}

    # Count the occurrences of each character in the string
    for char in s_lower:
        char_count[char] = char_count.get(char, 0) + 1

    # Iterate through the original string to find the first non-repeating character
    for char in string:
        if char_count[char.lower()] == 1:
            return char

    # If no non-repeating character is found, return an empty string
    return "''"


def run_tests() -> None:
    """
    Runs the tests for the ``first_non_repeating_letter`` function.
    :return:
    """

    test_strings: List[str] = ['stress', 'sTreSS', 'aabbcc', "''", 'a']
    for string in test_strings:
        print(f"Input: {string} | Output: {first_non_repeating_letter(string)}")


if __name__ == '__main__':
    run_tests()
