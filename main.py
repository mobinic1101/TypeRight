import pyautogui
from input_handler import listen
from validation import is_word_correctable
from corrector import correct


def main():
    while 1:
        user_word = listen()
        print(f"INCOMING-WORD: {user_word}")

        if not is_word_correctable(user_word):
            print(f"word '{user_word}' is not correctable")
            continue

        # correcting the word
        new_word = correct(user_word)
        print("corrected: ", new_word)

        # replacing the new word
        pyautogui.press("backspace", presses=len(user_word) + 1)

        

if __name__ == '__main__':
    print("hello there")
    main()