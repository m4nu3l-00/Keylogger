import time
from pynput import keyboard
from buffer import Buffer


class Keylogger:
    def on_key_release(self, key) -> bool:
        """
        Event method if a key was released
        :param key: The released key
        :return: true, if the listening should be continued
        """
        if key not in self.__pressed_keys:
            return True
        self.__pressed_keys.remove(key)
        release_time = time.time()
        self.__buffer.write_to_buffer([str(key), release_time, False])
        return True

    def on_key_press(self, key) -> bool:
        """
        Event method if a key was pressed
        :param key: The pressed key
        :return: true, if the listening should be continued
        """
        if key in self.__pressed_keys:
            return True
        self.__pressed_keys.append(key)
        press_time = time.time()
        self.__buffer.write_to_buffer([str(key), press_time, True])
        if str(key) == 'Key.end':
            return False
        return True

    def __init__(self, buffer: Buffer, key:str):
        """
        Initialize an Instance with given Buffer
        :param buffer: Object of the Buffer class
        """
        self.__pressed_keys = []
        self.__buffer = buffer

    def stop_logging(self):
        pass

    def start_logging(self) -> None:
        """
        This starts the logging process
        """
        try:
            with keyboard.Listener(on_press=self.on_key_press, on_release=self.on_key_release) as listener:
                listener.join()
        except Exception as e:
            Exception(e)
        return
