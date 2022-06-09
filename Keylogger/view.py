from threading import Event


class View:
    def __init__(self):
        """
        Initialize an instance
        Should only be called from subclasses
        """
        self._control = None
        self._keylogger_stopped = Event()

    def start_view(self, control) -> None:
        """
        Should be overwritten and start the view
        This parent class method sets the Control object
        :param control: Instance of the Control class
        """
        self._control = control

    def show_keylogger_stopped(self) -> None:
        """
        Abstract method, must be overwritten
        Should notify the user, if the key was stopped
        """
        raise NotImplementedError('subclasses must override show_keylogger_stopped()!')

    def show_error(self, text: str) -> None:
        """
        Abstract method, must be overwritten
        Should notify the user, if an error occurred and close the program
        :param text: error text
        """
        raise NotImplementedError('subclasses must override error()!')
