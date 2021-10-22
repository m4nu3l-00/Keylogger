class View:
    def start_view(self, control):
        raise NotImplementedError('subclasses must override start_view()!')

    def show_keylogger_stopped(self):
        raise NotImplementedError('subclasses must override show_keylogger_stopped()!')
