from listener import listen
from validation import is_word_correctable
from corrector import correct


def main():
    while 1:
        user_word = listen()
        print(f"INCOMING-WORD: {user_word}")

        if not is_word_correctable(user_word):
            print(f"word '{user_word}' is not correctable")
            continue

        new_word = correct(user_word)
        print("corrected: ", new_word)
        

if __name__ == '__main__':
    print("hello there")
    main()