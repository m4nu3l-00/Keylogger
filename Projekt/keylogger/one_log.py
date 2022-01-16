from pynput import keyboard


class OneLog:

    def __init__(self):
        self.__key = None
        self.__stop_event = None

    def __on_key_press(self, key) -> bool:
        """
        Event method if a key was pressed
        :param key: The released key
        :return: true, if the listening should be continued
        """
        self.__key = str(key)
        return False

    def log_key(self) -> str:
        """
        Used to log one key
        :return: returns the pressed key
        """
        try:
            with keyboard.Listener(on_press=self.__on_key_press) as listener:
                listener.join()
            return self.__key
        except Exception:
            raise Exception("Error while logging Stop-Keylogger")
