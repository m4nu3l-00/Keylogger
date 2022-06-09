import csv
from buffer import Buffer
import os
import global_variables


class Writer:
    def __init__(self, buffer: Buffer):
        """
        Initialize an instance with given Buffer
        The object is used to write items from the Buffer into a file
        :param buffer: Instance of the Buffer class
        """
        self.__buffer = buffer
        self.__csv_file = None

    def read_buffer(self) -> None:
        """
        Read and clear the item of the Buffer
        """
        try:
            self.__open_file()
            while True:
                try:
                    event_array = list(self.__buffer.read_from_buffer())
                    if event_array[0] == 'End':
                        self.__csv_file.close()
                        return
                    if type(event_array[0]) == str and type(event_array[1]) == float and type(event_array[2]) == bool:
                        self.__write_csv(event_array)
                    else:
                        raise Exception("Type Error.")
                except Exception:
                    raise Exception("Error while reading Buffer and writing to the array.")
        except Exception as e:
            global_variables.error_text = str(e)
            global_variables.error_flag.set()

    def __open_file(self) -> None:
        """
        opens the csv-file
        """
        try:
            if os.path.isfile(os.path.dirname(os.path.realpath(__file__)) + "/keylogger.csv"):
                os.remove(os.path.dirname(os.path.realpath(__file__)) + "/keylogger.csv")
            self.__csv_file = open(os.path.dirname(os.path.realpath(__file__)) + "/keylogger.csv", "a+", newline="", encoding="utf-8")
        except Exception:
            raise Exception("Can't open keylogger-file.")

    def __write_csv(self, event_array: list) -> None:
        """
        writes an item to the csv-file and saves the csv-file
        :param event_array: List of items (key, time, event)
        """
        writer = csv.writer(self.__csv_file)
        writer.writerow(event_array)
        self.__csv_file.flush()
        os.fsync(self.__csv_file.fileno())
