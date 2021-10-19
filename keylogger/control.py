import sys
import threading
from buffer import Buffer
from keylogger import Keylogger
from view import View
from writer import CsvWriter


class Control:
    def __init__(self, view: View):
        self.__view = view
        self.__view.start_view()

    def start(self):
        buffer = Buffer()
        keylogger = Keylogger(buffer)
        writer = CsvWriter(buffer)
        writer_thread = threading.Thread(target=writer.read_buffer)
        writer_thread.daemon = True
        writer_thread.start()
        keylogger.start_logging()
        writer_thread.join()
        sys.exit()

    def stop(self):
        pass

    def set_stop_key(self, key:str):
        pass