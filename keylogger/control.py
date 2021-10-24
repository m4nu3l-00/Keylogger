import threading
from buffer import Buffer
from keylogger import Keylogger
from view import View
from writer import CsvWriter
from one_log import OneLog


class Control:
    def __init__(self, view: View):
        self.__stop_key = "Key.end"
        self.__keylogger = None
        self.__writer_thread = None
        self.__keylogger_monitoring_thread = None
        self.__view = view
        self.__view.start_view(self)

    def start(self) -> bool:
        """
        This method is used to start the keylogger.
        :return: True, if the keylogger was started; False, if it is already active
        """
        if self.keylogger_is_running():
            return False

        buffer = Buffer()
        self.__keylogger = Keylogger(buffer, self.__stop_key)
        writer = CsvWriter(buffer)

        self.__writer_thread = threading.Thread(target=writer.read_buffer)
        self.__writer_thread.daemon = True
        self.__writer_thread.start()

        self.__keylogger.start_logging()

        self.__keylogger_monitoring_thread = threading.Thread(target=self.__monitor_keylogger)
        self.__keylogger_monitoring_thread.daemon = True
        self.__keylogger_monitoring_thread.start()
        return True

    def __monitor_keylogger(self):
        self.__keylogger.wait_for_keylogger_stopped()
        self.__writer_thread.join()
        self.__keylogger = None
        self.__view.show_keylogger_stopped()

    def stop(self) -> bool:
        """
        This method is used to stop the keylogger.
        :return: True, if the keylogger was stopped successfully; False, if the keylogger is not running
        """
        if not self.keylogger_is_running():
            return False
        self.__keylogger.stop_logging()
        self.__keylogger_monitoring_thread.join()
        return True

    def keylogger_is_running(self) -> bool:
        """
        This method is used to check if the keylogger is running
        :return: True, if the keylogger is running
        """
        return self.__keylogger is not None and self.__keylogger.keylogger_running()

    def get_stop_key(self) -> str:
        """
        This method is used to get current stop key
        :return: The current stop key
        """
        return self.__stop_key.replace('\'', '').replace('Key.', '').replace('[', '').replace(']', '')\
            .upper().replace('SS', 'ß')

    def set_stop_key(self) -> bool:
        """
        This method is used to set a new stop key
        :return: True, if the stop key was set successfully; False, if the keylogger is running
        """
        if not self.keylogger_is_running():
            self.__stop_key = OneLog().log_key()
            return True
        return False
