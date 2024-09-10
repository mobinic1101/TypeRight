from pynput import keyboard
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
    

def clear_word(press_count: int):
    """presses backspace several times to clear a word.

    Args:
        press_count (int): the number of times the backspace key is going to get pressed.
    """
    pyautogui.press("backspace", presses=press_count)


def write_word(word):
    pyautogui.write(word)
    
