import input_handler
from validation import is_word_correctable
from corrector import correct


def main():
    while 1:
        user_word = input_handler.listen()
        if not user_word:
            continue
        word_separator = user_word[-1]
        user_word = user_word[:-1]
        print(f"INCOMING-WORD: {user_word}, length: ", len(user_word))

        if not is_word_correctable(user_word):
            print(f"word '{user_word}' is not correctable")
            continue

        # correcting the word
        new_word = correct(user_word)
        print("corrected: ", new_word)

        # replacing the new word
        new_word = new_word["word"]
        if new_word:
            input_handler.clear_word(len(user_word) + 1)
            input_handler.write_word(new_word + word_separator)
        

if __name__ == '__main__':
    print("hello there")
    main()