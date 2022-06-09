from threading import Event


class View:
    def __init__(self):
        """
        Initialize an Instance
        Should only be called from subclasses
        """
        self._control = None
        self._keylogger_stopped = Event()

    def start_view(self, control) -> None:
        """
        Should be overwritten and start the view
        This parent class method sets the control object
        :param control: Instance of the control-class
        """
        self._control = control

    def show_keylogger_stopped(self) -> None:
        """
        Abstract Method, must be overwritten
        Should notify the user if the key was stopped
        """
        raise NotImplementedError('subclasses must override show_keylogger_stopped()!')

    def show_error(self, text: str) -> None:
        """
        Abstract Method, must be overwritten
        Should notify if an error occurred and close the program
        :param text: Error-text
        """
        raise NotImplementedError('subclasses must override error()!')
