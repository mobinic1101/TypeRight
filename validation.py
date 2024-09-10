from string import digits, punctuation
from corrector import all_words


def has_digits_or_punctuation(word: str):
    for char in word:
        if char in digits or char in punctuation:
            return True
    return False

def check_repetition(word: str):
    """returns True if a char in a word repeated more than 2 times.

    Args:
        word (str)

    Returns:
        boolean
    """
    repeat_count = 1
    prev_char = ""
    for char in word:
        if char == prev_char:
            repeat_count += 1
        else:
            prev_char = char

        if repeat_count <= 3:
            return True
    return False


def is_valid(word: str, max_len: int = 10):
    invalid_len = max_len < len(word) < 3
    contains_invalid = has_digits_or_punctuation(word)
    chars_repeated_exceed = check_repetition(word)
    word_exists_in_all_words = word in all_words

    if (
        invalid_len or
        contains_invalid or
        chars_repeated_exceed or
        word_exists_in_all_words
    ):
        return False
    return True

