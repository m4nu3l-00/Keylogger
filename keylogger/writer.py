import csv
from buffer import Buffer
import os


class CsvWriter:

    def __init__(self, buffer: Buffer):
        """
        Initialize an Instance with given Buffer
        :param buffer: Object of the Buffer class
        """
        self.__buffer = buffer
        self.__csv_file = None

    def read_buffer(self) -> None:
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
                    raise Exception("Type Error")
            except Exception:
                raise Exception("Error while reading Buffer")

    def __open_file(self):
        try:
            if os.path.isfile("./keylogger.csv"):
                os.remove("./keylogger.csv")
            self.__csv_file = open('keylogger.csv', 'a+', newline='')
        except Exception:
            raise Exception("Error during opening File")

    def __write_csv(self, event_array: list) -> None:
        writer = csv.writer(self.__csv_file)
        writer.writerow(event_array)
        self.__csv_file.flush()
        os.fsync(self.__csv_file.fileno())
