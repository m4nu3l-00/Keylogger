import sys
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
        if self.__running_keylogger is not None:
            return False

        buffer = Buffer()
        self.__running_keylogger = Keylogger(buffer, self.__stop_key)
        writer = CsvWriter(buffer)

        self.__writer_thread = threading.Thread(target=writer.read_buffer)
        self.__writer_thread.daemon = True
        self.__writer_thread.start()

        self.__running_keylogger.start_logging()
        return True

    def stop(self):
        self.__running_keylogger.stop_logging()
        self.__writer_thread.Join()
        self.__running_keylogger = None

    def keylogger_is_running(self) -> bool:
        return self.__running_keylogger is not None

    def get_stop_key(self) -> str:
        return self.__stop_key

    def set_stop_key(self, key: str):
        self.__stop_key = key
