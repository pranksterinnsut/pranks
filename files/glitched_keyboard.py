import keyboard

def on_press(event):

    key = event.name

    for i in range(5):
        keyboard.press(key)
        keyboard.release(key)

keyboard.on_press(on_press)
keyboard.wait()
