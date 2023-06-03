from pyautogui import *
from time import *
from pynput import keyboard
from random import *

l = ["up","down","right","left","up","down","up","down","up","down","up","down","up","down"]

def check():
    sleep(15)
    while(True):
        sleep(0.3)
        s = l[randint(0,len(l)-1)]
        press(s)
    
    
n = 0
def on_press(key):
    if key == keyboard.Key.ctrl_l:
        check()
    if key == keyboard.Key.ctrl_r:
        check()
    if key == keyboard.Key.enter:
        check()
    if key == keyboard.Key.shift_l:
        check()
    if key == keyboard.Key.shift_r:
        check()
    if key == keyboard.Key.tab:
        check()

# Create a listener
listener = keyboard.Listener(on_press=on_press)

# Start the listener in a separate thread
listener.start()

# Keep the main thread running to prevent the script from exiting
listener.join()
