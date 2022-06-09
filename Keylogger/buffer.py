import queue
import threading


class Buffer:
    def __init__(self):
        """
        Initialize a Buffer with a 576 000 Items Space
        The object is used as buffer between a Keylogger and a Writer object
        """
        self.__buffer = queue.Queue(576000)

    def write_to_buffer(self, item: list) -> None:
        """
        Writes one item (contains a list) into the Buffer
        :param item: List of items (key, time, event)
        """
        self.__buffer.put(item)

    def read_from_buffer(self) -> list:
        """
        Reads items from the buffer
        :return: One item of the buffer (contains a list)
        """
        if self.__buffer.full():
            print("Warning! Queue is full. Logged Data may be incorrect.")
        item = self.__buffer.get(block=True, timeout=None)
        return item
