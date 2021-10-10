from keylogger import Keylogger
from writer import CsvWriter
from buffer import Buffer
from threading import Thread


def main() -> None:
    """
    The main-Method of the program
    """
    buffer = Buffer()
    keylogger = Keylogger(buffer)
    writer = CsvWriter(buffer)
    writer_thread = Thread(target=writer.read_buffer)
    writer_thread.start()
    keylogger.start_logging()


if __name__ == "__main__":
    main()
