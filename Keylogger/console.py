import sys
import threading

from view import View
from control import Control


class Console(View):
    def __init__(self):
        """
        Initialize an Instance.
        The object is used for console interaction with the user.
        """
        super(Console, self).__init__()
        self.__write_lock = threading.Lock()

    def start_view(self, control: Control) -> None:
        """
        Starts the Interface of the Console
        Handles user Input
        :param control: Instance of the Control-Class
        """
        super(Console, self).start_view(control)
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
                    if self._control.start():
                        self._keylogger_stopped.clear()
                        print("Keylogger started successfully.")
                        key = self._control.get_stop_key()
                        print("Type \"stop\" or press \"%s\" to end the keylogger.\n" % key)
                    else:
                        print("The Keylogger is already terminated.\n")

                elif console_input == "stop":
                    if self._control.stop():
                        print("Stopping the keylogger...")
                    else:
                        print("The Keylogger is already terminated.\n")

                elif console_input == "exit":
                    if self._control.keylogger_is_running():
                        print("Please terminate the keylogger with \"stop\" first.")
                    else:
                        sys.exit()

                elif console_input == "set stop key":
                    if not self._control.keylogger_is_running():
                        print("Please press the key you want to use as stop key.\n")
                    if self._control.set_stop_key():
                        key = self._control.get_stop_key()
                        print("Key \"%s\" was set as stop-key.\n" % key)
                    else:
                        print("You can't set a stop key while the keylogger is running")

                elif console_input == "show stop key":
                    key = self._control.get_stop_key()
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
                if self._control.keylogger_is_running():
                    if self._control.stop():
                        self._keylogger_stopped.wait()
                        print("Keylogger has been stopped.")
                    else:
                        print("Couldn't stop Keylogger before Closing.")
                sys.exit()

    def show_keylogger_stopped(self) -> None:
        """
        Prints that the Keylogger has stopped
        """
        print("Keylogger terminated successfully!")
        self._keylogger_stopped.set()
        if self. __write_lock.locked():
            self.__write_lock.release()

    def show_error(self, text: str) -> None:
        """
        Displays the error on the console and closes the program
        :param text: Error-text
        """
        print("Error occurred:\n" + text)
        sys.exit()
