from pynput import keyboard
# import pyautogui

def on_press(key: keyboard.KeyCode | keyboard.Key, word:list):
    ...

def listen():
    listener = keyboard.Listener(on_press=on_press)
    ...