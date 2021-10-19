import sys
import getopt
from console import Console
from control import Control


def main(argv) -> None:
    """
    The main-Method of the program
    """
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
        print("Eine simultane Auswahl von -c und -g ist nicht erlaubt.")
        sys.exit()

    try:
        if gui:
            view = None
            #TODO Erstelle gui object
        else:
            view = Console()
        Control(view)
    except Exception as e:
        print("Ein Fehler ist aufgetreten!")
        print(str(e))


def print_help():
    print("Keylogger v0.1")
    print("Argumente:")
    print("-c: Startet den Keylogger in der Konsole (default)")
    print("-g: Startet eine GUI für den Keylogger")
    print("-h: Zeigt diesen Hilfetext")


if __name__ == "__main__":
    main(sys.argv[1:])
