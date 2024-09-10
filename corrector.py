WORDS_PATH = "./words.txt"


def get_all_words(file_path: str):
    with open(file_path, "r") as file:
        return file.readlines()


all_words = get_all_words()


def correct(user_word):
    ...