from pyautogui import *
from time import *
from pynput import keyboard
from random import *


def check():
    sleep(5)
    keyDown("alt")
    keyDown("F4")
    keyUp("alt")
    
    
n = 0
def on_press(key):
    if key == keyboard.Key.enter:
        check()

# Create a listener
listener = keyboard.Listener(on_press=on_press)

# Start the listener in a separate thread
listener.start()

# Keep the main thread running to prevent the script from exiting
listener.join()
