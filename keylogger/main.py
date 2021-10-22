import sys
import getopt
from console import Console
from control import Control
from Keylogger_gui import UiKeylogger
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

def main(argv) -> None:
    """
    The main-Method of the program
    The arguments are evaluated and the respective view (and control) is started
    """
    #Test

    app = QApplication([])
    window = QWidget()
    x = UiKeylogger()
    x.setup(window)
    window.show()
    app.setStyle("Fusion")
    app.exec()
    #Test
    console = False
    gui = False

    try:
        opts, args = getopt.getopt(argv, "ghc")
    except getopt.GetoptError:
        print_help()
        sys.exit()
    for opt, arg in opts:
        if opt == '-h':
            print_help()
            sys.exit()
        elif opt == '-c':
            console = True
        elif opt == '-g':
            gui = True
    if console and gui:
        print("A simultaneous use of -c and -g is not allowed.")
        sys.exit()

    try:
        if gui:
            view = None
            #TODO Erstelle gui object
        else:
            view = Console()
        Control(view)
    except Exception as e:
        print("An error occurred!")
        print(str(e))


def print_help():
    print("Keylogger v0.1")
    print("Arguments:")
    print("-c: Starts the keylogger in the console (default)")
    print("-g: Starts a GUI for the keylogger")
    print("-h: Shows this help-text")


if __name__ == "__main__":
    main(sys.argv[1:])
