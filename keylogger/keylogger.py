from pynput import keyboard
import time


pressed_keys = []


def on_key_release(key: keyboard._win32.KeyCode) -> bool:
    """
    Event method if a key was released.
    :param key: The released key.
    :return: true, if the listening should be continued.
    """
    if key not in pressed_keys:
        return True
    pressed_keys.remove(key)
    release_time = time.time()
    print(release_time, ": ",  key, " released")
    return True

def on_key_press(key: keyboard._win32.KeyCode) -> bool:
    """
    Event method if a key was pressed.
    :param key: The pressed key.
    :return: true, if the listening should be continued.
    """
    if key in pressed_keys:
        return True
    pressed_keys.append(key)
    press_time = time.time()
    print(press_time, ": ", key, " pressed")
    return True


def start_logger() -> int:
    """
    The method to initialize the key press and key release listener.
    :return: -1 if an error occured.
    """
    with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
        listener.join()
    return -1
