import sys
from view import View
from control import Control


class Console(View):

    def start_view(self, control: Control):
        print("Willkommen zum Keylogger!")
        while True:
            console_input = input()
            if console_input == "Start":
                if control.start():
                    print("Keylogger erfolgreich gestartet!")
                else:
                    print("Der Keylogger läuft bereits!")
            if console_input == "Stop":
                control.stop()
            if console_input == "Exit":
                if control.keylogger_is_running():
                    print("Bitte beende den Keylogger zuerst.")
                else:
                    sys.exit()
            if console_input == "Setze Stop-Key":
                pass#TODO
            if console_input == "Zeige Stop-Key":
                pass#TODO
            if console_input == "Hilfe":
                pass#TODO Alle Befehle anzeigen
