# Keylogger Program

This is a simple keylogger program written in Python using the `pynput` library. The program logs all key presses to a file named `keylog.txt`. 

## Features

- Logs all key presses to a text file
- Handles both regular and special keys
- Stops logging when the 'esc' key is pressed

## Requirements

- Python 3.x
- `pynput` library

## Example

Run the program in a terminal using command `python keylogger.py` (make sure you are in the same directory). The program will start monitoring keyboard input. Type some text or press some keys on your keyboard. Open the keylog.txt file in the same directory. You should see the keys you pressed logged there. To stop the keylogger, press the esc key. This will exit the listener and stop logging keystrokes.

## Limitations

- Ethical and Legal Use: This keylogger should only be used for educational purposes or personal use with explicit permission from the owner of the computer. Unauthorized use of keyloggers is illegal and unethical.
- Special Keys Logging: Special keys are logged in a different format (e.g., [Key.space] for the space bar), which may make the log file harder to read.
- Performance Impact: Running a keylogger continuously may have a minor impact on system performance, especially on older machines.
- Security: The log file is stored in plain text and is not encrypted, making it vulnerable to unauthorized access. Ensure the file is stored in a secure location.