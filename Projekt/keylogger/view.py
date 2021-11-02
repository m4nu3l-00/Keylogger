class View:
    def start_view(self, control) -> None:
        """
        Abstract Method, must be overwritten
        Should start the view
        :param control: Instance of the control-class
        """
        raise NotImplementedError('subclasses must override start_view()!')

    def show_keylogger_stopped(self) -> None:
        """
        Abstract Method, must be overwritten
        Should notify the user if the key was stopped
        """
        raise NotImplementedError('subclasses must override show_keylogger_stopped()!')

    def error(self, text: str) -> None:
        """
        Abstract Method, must be overwritten
        Should notify if an error occurred
        :param text: Error-text
        """
        raise NotImplementedError('subclasses must override error()!')
