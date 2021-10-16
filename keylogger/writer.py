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
        if os.path.isfile("./keylogger.csv"):
            os.remove("./keylogger.csv")
        try:
            self.__csv_file = open('keylogger.csv', 'a+', newline='')
            self.__writer = csv.writer(self.__csv_file)

        except Exception as e:
            raise Exception(e)

    def __del__(self):
        self.__csv_file.close()

    def read_buffer(self) -> None:
        """
        Reads continuous the Buffer and calls the write_csv function
        :return: Returns if everything is fine, otherwise throws Exceptions
        """
        while True:
            try:
                event_array = list(self.__buffer.read_from_buffer())
                if type(event_array[0]) == str and type(event_array[1]) == float and type(event_array[2]) == bool:
                    self.write_csv(event_array)
                else:
                    raise Exception("Type Error")
            except Exception as e:
                raise Exception(e)

    def write_csv(self, event_array: list) -> None:
        """
        Writes Data from the Array into a csv-Files
        Structure of the File ist: Key, Time, Event
        :param event_array: Format of the List (String: Key, int: Time, bool: Event)
        Event=1 -> press; Event=0 ->release
        """
        self.__writer.writerow(event_array)
        self.__csv_file.flush()
        os.fsync(self.__csv_file.fileno())
