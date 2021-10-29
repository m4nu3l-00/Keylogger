import threading
import time
from pynput import keyboard
from buffer import Buffer
import global_variables


class Keylogger:
    def __init__(self, buffer: Buffer, key: str):
        """
        Initialize an Instance with given Buffer
        :param buffer: Object of the Buffer class
        """
        self.__pressed_keys = []
        self.__buffer = buffer
        self.__stop_key = key
        self.__stop_lock = threading.Lock()
        self.__keylogger_stopped = threading.Event()
        self.__listener_thread = None

    def __on_key_release(self, key) -> bool:
        """
        Event method if a key was released
        :param key: The released key
        :return: true, if the listening should be continued
        """
        key_string = str(key).upper()
        if key_string not in self.__pressed_keys:
            return True
        release_time = time.time()
        # Special Case if key is shift
        if key_string == "KEY.SHIFT":
            for char in self.__pressed_keys:
                if not char.replace('\'', '').isalpha() and not char == "KEY.SHIFT":
                    self.__buffer.write_to_buffer([char, release_time, False])
                    self.__pressed_keys.remove(char)
        self.__buffer.write_to_buffer([key_string, release_time, False])
        self.__pressed_keys.remove(key_string)
        return True

    def __on_key_press(self, key) -> bool:
        """
        Event method if a key was pressed
        :param key: The pressed key
        :return: true, if the listening should be continued
        """
        key_string = str(key).upper()
        if key_string in self.__pressed_keys:
            return True
        self.__pressed_keys.append(key_string)
        press_time = time.time()
        if key_string == self.__stop_key:
            self.stop_logging()
        else:
            self.__buffer.write_to_buffer([key_string, press_time, True])
        return True

    def stop_logging(self) -> None:
        """
        Stops the Keylogger and writes End to the Buffer so the writer will stop too
        The implementation is thread safe
        """
        with self.__stop_lock:
            if not self.__keylogger_stopped.is_set():
                self.__buffer.write_to_buffer(["End"])
                self.__keylogger_stopped.set()

    def keylogger_running(self) -> bool:
        """
        Check if the Logger is still active
        :return: True, if the keylogger is running
        """
        return not self.__keylogger_stopped.is_set()

    def wait_for_keylogger_stopped(self) -> None:
        self.__keylogger_stopped.wait()

    def start_logging(self) -> None:
        """
        This starts the logging process
        """
        self.__keylogger_stopped.clear()
        try:
            self.__listener_thread = threading.Thread(target=self.__run_listener)
            self.__listener_thread.daemon = True
            self.__listener_thread.start()
        except Exception:
            raise Exception("Error while starting Keylogger.")

    def __run_listener(self) -> None:
        """
        This method is used to start the listener until the __keylogger_stopped event
        """
        try:
            with keyboard.Listener(on_press=self.__on_key_press, on_release=self.__on_key_release):
                self.__keylogger_stopped.wait()
        except:
            global_variables.error_text = "The keylogger has crashed."
            global_variables.error_flag.set()
