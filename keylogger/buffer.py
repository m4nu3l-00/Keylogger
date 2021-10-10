import queue
import threading


class Buffer:
    def __init__(self):
        """
        Initialize a Buffer with a 50 Items Space
        """
        self.__buffer = queue.Queue(50)
        self.__buffer_not_empty = threading.Event()

    def write_to_buffer(self, item: list) -> None:
        """
        Writes one Item (contains a List) into the Buffer
        :param item: List of Items (key, time, event)
        """
        self.__buffer.put(item)
        self.__buffer_not_empty.set()

    def read_from_buffer(self) -> list:
        """
        Reads Items from Buffer
        :return: One Item of the Buffer (contains a List)
        """
        self.__buffer_not_empty.wait(timeout=None)
        item = self.__buffer.get()
        if self.__buffer.empty():
            self.__buffer_not_empty.clear()
        return item
