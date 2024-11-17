from settings import WORDS_FILE_PATH

def get_all_words(file_path: str=WORDS_FILE_PATH):
    with open(file_path, "r") as file:
        return [line[:-1] for line in file]
    
all_words = get_all_words()