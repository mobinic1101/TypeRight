from string import digits, punctuation
from utils import all_words
import settings


def has_digits_or_punctuation(word: str|list):
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
            repeat_count = 1

        if repeat_count >= 3:
            return True
    return False


def is_word_correctable(word: str):
    """
    returns False if word is already correct or
    cant get corrected otherwise returns True

    Args:
        word (str): the user typed word
        max_len (int, optional): if the word was larger than this number
        it will return False. Defaults to 20.

    Returns:
        boolean: True or False
    """
    false_conditions = [
        len(word) > settings.MAX_WORD_LENGTH or len(word) < settings.MIN_WORD_LENGTH,
        has_digits_or_punctuation(word),
        check_repetition(word),
        word in all_words,
        not word,
    ]

    if any(false_conditions):
        return False
    return True

if __name__ == '__main__':
    print(is_word_correctable("hollo "))
