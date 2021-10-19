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
            elif console_input == "Stop":
                if control.stop():
                    print("Keylogger erfolgreich beendet!")
                else:
                    print("Der Keylogger ist bereits beendet!")
            elif console_input == "Exit":
                if control.keylogger_is_running():
                    print("Bitte beende den Keylogger zuerst!")
                else:
                    sys.exit()
            elif console_input == "Setze Stop-Key":
                pass#TODO
            elif console_input == "Zeige Stop-Key":
                pass#TODO
            elif console_input == "Hilfe":
                pass#TODO Alle Befehle anzeigen
            elif console_input == "Hilfe":
                pass#TODO Alle Befehle anzeigen
            else:
                print("Das ist kein gültiger Befehl!")
