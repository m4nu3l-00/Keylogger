from view import View
from control import Control

class Console(View):

    def start_view(self, control: Control):
        while True:
            console_input = input()
            ifconsole_input == "start":
                control.start()
        #TODO
