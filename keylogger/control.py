import threading
from buffer import Buffer
from keylogger import Keylogger
from view import View
from writer import CsvWriter


class Control:
    def __init__(self, view: View):
        self.__stop_key = "Key.end"
        self.__running_keylogger = None
        self.__writer_thread = None
        self.__view = view
        self.__view.start_view(self)

    def start(self) -> bool:
        """
        This method is used to start the keylogger.
        :return: True, if the keylogger was started; False, if it is already active
        """
        if self.__running_keylogger is not None and self.__running_keylogger.listener_active():
            return False

        buffer = Buffer()
        self.__running_keylogger = Keylogger(buffer, self.__stop_key)
        writer = CsvWriter(buffer)

        self.__writer_thread = threading.Thread(target=writer.read_buffer)
        self.__writer_thread.daemon = True
        self.__writer_thread.start()

        self.__running_keylogger.start_logging()
        return True

    def stop(self) -> bool:
        """
        This method is used to stop the keylogger.

        :return: True, if the keylogger was stopped successfully; False if the keylogger is not running
        """
        if self.__running_keylogger is None or not self.__running_keylogger.listener_active():
            return False

        self.__running_keylogger.stop_logging()
        self.__writer_thread.join()
        self.__running_keylogger = None
        return True

    def keylogger_is_running(self) -> bool:
        """
        This method is used to check if the keylogger is running
        :return: True, if the keylogger is running.
        """
        return self.__running_keylogger is not None and self.__running_keylogger.listener_active()

    def get_stop_key(self) -> str:
        """
        This method is used to get current stop key
        :return: The current stop key
        """
        return self.__stop_key

    def set_stop_key(self, key: str) -> None:
        """
        This method is used to set a new stop key
        :param key: The key which should be used as stop key
        """
        self.__stop_key = key
