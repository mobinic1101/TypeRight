from pynput import keyboard
from pynput.keyboard import Key
import pyautogui


class StopListening(Exception):
    pass


def on_press(key: keyboard.Key | keyboard.KeyCode, letters: list):
    if isinstance(key, keyboard.Key):
        if key == keyboard.Key.space:
            print(f"'space' key pressed")
            letters.append(" ")
            raise StopListening()
        elif (key == keyboard.Key.backspace
              or key == keyboard.Key.enter):
            letters.append("!")
    else:
        letters.append(key.char)


def listen():
    letters = []
    listener = keyboard.Listener(on_press=lambda key: on_press(key, letters))
    try:
        listener.start()
        listener.join()
    except (StopListening):
        listener.stop()
        word = "".join(letters)
        letters.clear()
        return word
