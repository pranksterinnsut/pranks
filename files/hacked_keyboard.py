from pynput import keyboard
from webbrowser import *
from random import *

list = ["google.com","youtube.com","facebook.com","amazon.com","yahoo.com","wikipedia.org","zoom.us","netflix.com","reddit.com","live.com","instagram.com","linkedin.com","office.com","microsoft.com","aliexpress.com","yahoo.co.jp","whatsapp.com","google.com.hk","tiktok.com","ebay.com","amazon.co.jp","stackoverflow.com","bing.com","pinterest.com","twitter.com","google.co.jp","apple.com","github.com","google.co.uk","google.de","imdb.com"]#

def open_():
    x = randint(0,len(list))
    s = list[x]
    open(s)

def on_press(key):
    if key == keyboard.Key.enter:
        open_()

# Create a listener
listener = keyboard.Listener(on_press=on_press)

# Start the listener in a separate thread
listener.start()

# Keep the main thread running to prevent the script from exiting
listener.join()
