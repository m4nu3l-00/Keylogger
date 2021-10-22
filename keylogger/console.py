import sys
from view import View
from control import Control


class Console(View):

    def start_view(self, control: Control):
        print("Welcome to the Keylogger!")
        while True:
            console_input = input().lower()

            if console_input == "start":
                if control.start():
                    print("Keylogger started successfully.")
                    key = control.get_stop_key().replace('\'', '')
                    print("Type \"stop\" or press \"%s\" to end the keylogger." % key)
                else:
                    print("Keylogger is already running.")

            elif console_input == "stop":
                if not control.stop():
                    print("The Keylogger is already terminated.")

            elif console_input == "exit":
                if control.keylogger_is_running():
                    print("Please terminate the keylogger first.")
                else:
                    sys.exit()

            elif console_input == "set stop key":
                print("Please press the key you want to use as stop key.")
                if control.set_stop_key():
                    key = control.get_stop_key().replace('\'', '')
                    print("\nKey \"%s\" was set as stop-key." % key)

            elif console_input == "show stop key":
                key = control.get_stop_key().replace('\'', '')
                print("\nKey \"%s\" was set as stop-key." % key)

            elif console_input == "help":
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

            else:
                print("Unknown command! Type \"help\" to get all commands.")

    def show_keylogger_stopped(self):
        print("Keylogger terminated successfully!")
