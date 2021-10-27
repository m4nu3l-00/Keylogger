import sys
import threading

from view import View
from control import Control


class Console(View):
    def __init__(self):
        self.__write_lock = threading.Lock()

    def start_view(self, control: Control) -> None:
        """
        Starts the Interface of the Console. Handles user Input
        :param control: Instance of the Control-Class
        """
        print("Welcome to the Keylogger!\n")
        print("Possible commands are:")
        help_text_dict = {
            "help": "Prints the help-interface",
            "exit": "Terminate the Program",
            "start": "Starts the keylogger",
            "stop": "Stops the keylogger",
            "set stop key": "Setting the stop-key which will terminate the keylogger",
            "show stop key": "Prints the defined stop-key"
        }
        for key, value in help_text_dict.items():
            print(key + ": " + value)
        print()
        while True:
            try:
                console_input = input().lower()
                self.__write_lock.acquire()

                if console_input == "start":
                    if control.start():
                        print("Keylogger started successfully.")
                        key = control.get_stop_key()
                        print("Type \"stop\" or press \"%s\" to end the keylogger.\n" % key)
                    else:
                        print("The Keylogger is already terminated.\n")

                elif console_input == "stop":
                    if not control.stop():
                        print("The Keylogger is already terminated.\n")

                elif console_input == "exit":
                    if control.keylogger_is_running():
                        print("Please terminate the keylogger with \"stop\" first.")
                    else:
                        sys.exit()

                elif console_input == "set stop key":
                    if not control.keylogger_is_running():
                        print("Please press the key you want to use as stop key.\n")
                    if control.set_stop_key():
                        key = control.get_stop_key()
                        print("Key \"%s\" was set as stop-key.\n" % key)
                    else:
                        print("You can't set a stop key while the keylogger is running")

                elif console_input == "show stop key":
                    key = control.get_stop_key()
                    print("Key \"%s\" was set as stop-key.\n" % key)

                elif console_input == "help":
                    print("Possible commands are:")
                    for key, value in help_text_dict.items():
                        print(key + ": " + value)
                    print()

                else:
                    print("Unknown command! Type \"help\" to get all commands.\n")

                if console_input != "stop":
                    self.__write_lock.release()

            except KeyboardInterrupt:
                if control.stop():
                    print("\nKeylogger was stopped.")
                sys.exit()

    def show_keylogger_stopped(self) -> None:
        """
        Prints that the Keylogger has stopped
        """
        print("Keylogger terminated successfully!")

        if self. __write_lock.locked():
            self.__write_lock.release()
