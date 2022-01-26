import queue
import threading


class Buffer:
    def __init__(self):
        """
        Initialize a Buffer with a 10 000 000 Items Space
        """
        self.__buffer = queue.Queue(10000000)

    def write_to_buffer(self, item: list) -> None:
        """
        Writes one Item (contains a List) into the Buffer
        :param item: List of Items (key, time, event)
        """
        self.__buffer.put(item)

    def read_from_buffer(self) -> list:
        """
        Reads Items from Buffer
        :return: One Item of the Buffer (contains a List)
        """
        if self.__buffer.full():
            print("Warning! Queue is full. Logged Data may be incorrect.")
        item = self.__buffer.get(block=True, timeout=None)
        return item
