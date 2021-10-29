import sys
import threading
import tkinter as tk
from tkinter import messagebox

from keylogger import global_variables
from view import View
from control import Control


class GUI(View):
    def __init__(self):
        self.__control = None
        self.__state = "Start"
        self.__click_lock = threading.Lock()

        self.__window = tk.Tk()
        self.__window.resizable(True, False)
        self.__window.title('Keylogger')
        self.__window.protocol("WM_DELETE_WINDOW", self.__end_after_close)

        self.__start_button = tk.Button(
            self.__window,
            text='Start',
            command=self.__clicked_start
        )
        self.__start_button.pack(
            padx=10,
            pady=2,
            fill='both'
        )

        self.__set_button = tk.Button(
            self.__window,
            text='Set end-key',
            command=self.__clicked_set_key
        )
        self.__set_button.pack(
            padx=10,
            pady=2,
            fill='both'
        )

        self.__end_key_label = tk.Label(
            self.__window,
            text='End-key:',
            anchor='sw',
            justify=tk.LEFT
        )
        self.__end_key_label.pack(
            padx=10,
            pady=(5, 0),
            fill='both'
        )

        self.__end_key_text = tk.Text(
            self.__window,
            height=1
        )
        self.__end_key_text.insert('1.0', "Loading...")
        self.__end_key_text.pack(
            padx=10,
            pady=5,
            fill='both'
        )

    def start_view(self, control: Control) -> None:
        """
        Executes the window
        :param control: Instance of the Control- Class
        """
        self.__control = control
        self.__end_key_text.delete('1.0', tk.END)
        self.__end_key_text.insert('1.0', control.get_stop_key())
        self.__end_key_text['state'] = 'disabled'
        try:
            self.__window.mainloop()
        except KeyboardInterrupt:
            if self.__control.stop():
                print("Keylogger has been stopped.")
            self.__window.destroy()

    def __end_after_close(self) -> None:
        """
        Terminates the Keylogger if the window is closed and keylogger is still running
        """
        self.__click_lock.acquire()
        if self.__control.keylogger_is_running():
            if self.__control.stop():
                messagebox.showinfo("Keylogger Stopped", "Keylogger has been stopped.")
            else:
                messagebox.showerror("Error!", "Couldn't stop Keylogger before Closing.")
        self.__window.destroy()

    def show_keylogger_stopped(self) -> None:
        """
        Change gui to show that the Keylogger stopped
        """
        self.__start_button['text'] = "Start"
        self.__set_button['state'] = 'normal'
        if self.__click_lock.locked():
            self.__click_lock.release()

    def __clicked_start(self) -> None:
        """
        Starting the Keylogger
        """
        self.__click_lock.acquire()
        if self.__start_button['text'] == "Start":
            self.__start_button['text'] = "Stop"
            self.__set_button['state'] = 'disabled'
            if not self.__control.start():
                messagebox.showerror("Error!", "Keylogger could not be started.")
            self.__click_lock.release()
        elif self.__start_button['text'] == "Stop":
            if not self.__control.stop():
                messagebox.showerror("Error!", "Keylogger could not be stopped.")

    def __clicked_set_key(self) -> None:
        """
        Uses a Thread to set a new stop-key
        """
        self.__click_lock.acquire()
        self.__start_button["state"] = "disabled"
        self.__set_button["state"] = "disabled"

        self.__end_key_text["state"] = "normal"
        self.__end_key_text.delete('1.0', tk.END)
        self.__end_key_text.insert('1.0', "Please press a key!")
        self.__end_key_text.configure(fg="blue")
        self.__end_key_text['state'] = 'disabled'

        stop_key_thread = threading.Thread(target=self.__set_stop_key)
        stop_key_thread.daemon = True
        stop_key_thread.start()

    def __set_stop_key(self) -> None:
        """
        Sets the stop-key of the Keylogger
        """
        try:
            if not self.__control.set_stop_key():
                messagebox.showerror("Error!", "New End-Key could not be set.")
            self.__end_key_text["state"] = "normal"
            self.__end_key_text.delete('1.0', tk.END)
            self.__end_key_text.insert('1.0', self.__control.get_stop_key())
            self.__end_key_text.configure(fg="black")
            self.__end_key_text['state'] = 'disabled'

            self.__start_button["state"] = "normal"
            self.__set_button["state"] = "normal"
            self.__click_lock.release()
        except:
            global_variables.error_text = "The keylogger has crashed."
            global_variables.error_flag.set()

    def error(self, text: str) -> None:
        """
        Displays the error on the gui
        :param text: Error-text
        """
        messagebox.showerror("Error!", "Error occurred:\n" + text)
        self.__window.destroy()
        sys.exit()
