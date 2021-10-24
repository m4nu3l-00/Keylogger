import sys
import threading

from PyQt5 import QtCore, QtGui, QtWidgets

from view import View
from control import Control


class GUI(View):
    def __init__(self):
        self.__control = None

        self.__app = QtWidgets.QApplication(sys.argv)
        self.__app.setStyle("Fusion")
        self.__window = QtWidgets.QWidget()
        screen_size = QtWidgets.QDesktopWidget().screenGeometry(-1)
        self.__window.setWindowIcon(QtGui.QIcon('icon.png'))
        app_icon = QtGui.QIcon()
        app_icon.addFile('icon.png', QtCore.QSize(16, 16))
        app_icon.addFile('icon.png', QtCore.QSize(24, 24))
        app_icon.addFile('icon.png', QtCore.QSize(32, 32))
        app_icon.addFile('icon.png', QtCore.QSize(48, 48))
        app_icon.addFile('icon.png', QtCore.QSize(256, 256))
        self.__app.setWindowIcon(app_icon)

        self.__window.resize(screen_size.width() * 0.11, screen_size.height() * 0.03)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(1)
        size_policy.setVerticalStretch(1)
        size_policy.setHeightForWidth(self.__window.sizePolicy().hasHeightForWidth())
        self.__window.setSizePolicy(size_policy)
        self.__window.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.__window.setWindowTitle("Keylogger")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.__window)
        self.verticalLayout.setObjectName("verticalLayout")
        _translate = QtCore.QCoreApplication.translate

        # StartButton
        self.__start_button = QtWidgets.QPushButton(self.__window)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(1)
        size_policy.setVerticalStretch(1)
        size_policy.setHeightForWidth(self.__start_button.sizePolicy().hasHeightForWidth())
        self.__start_button.setSizePolicy(size_policy)
        self.__start_button.setObjectName("SetButton")
        self.verticalLayout.addWidget(self.__start_button)
        self.__start_button.setText(_translate("Keylogger", "Start"))

        # SetButton
        self.__set_button = QtWidgets.QPushButton(self.__window)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(1)
        size_policy.setVerticalStretch(1)
        size_policy.setHeightForWidth(self.__set_button.sizePolicy().hasHeightForWidth())
        self.__set_button.setSizePolicy(size_policy)
        self.__set_button.setObjectName("SetButton")
        self.verticalLayout.addWidget(self.__set_button)
        self.__set_button.setText(_translate("Keylogger", "Set end-key"))

        # EndKeyLabel
        self.__end_key_label = QtWidgets.QLabel(self.__window)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(1)
        size_policy.setVerticalStretch(1)
        size_policy.setHeightForWidth(self.__end_key_label.sizePolicy().hasHeightForWidth())
        self.__end_key_label.setSizePolicy(size_policy)
        self.__end_key_label.setObjectName("label")
        self.verticalLayout.addWidget(self.__end_key_label)
        self.__end_key_label.setText("End-key:")

        # EndKeyOutput
        self.__end_key_output = QtWidgets.QLineEdit(self.__window)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(1)
        size_policy.setVerticalStretch(1)
        size_policy.setHeightForWidth(self.__end_key_output.sizePolicy().hasHeightForWidth())
        self.__end_key_output.setSizePolicy(size_policy)
        self.__end_key_output.setReadOnly(True)
        self.__end_key_output.setObjectName("EndKeyOutput")
        self.verticalLayout.addWidget(self.__end_key_output)
        self.__end_key_output.setText(_translate("Keylogger", "EndKeyOutput"))
        self.__end_key_output.setAlignment(QtCore.Qt.AlignCenter)

        # Events
        self.__start_button.clicked.connect(self.__clicked_start)
        self.__set_button.clicked.connect(self.__clicked_set_key)

    def start_view(self, control: Control):
        self.__control = control
        self.__end_key_output.setText(self.__control.get_stop_key())
        self.__app.aboutToQuit.connect(self.end_after_close)
        self.__window.show()
        sys.exit(self.__app.exec())

    def end_after_close(self):
        if self.__control.keylogger_is_running():
            if self.__control.stop():
                QtWidgets.QMessageBox.about(self.__window, "Keylogger Stopped", "Keylogger has been stopped")
            else:
                QtWidgets.QMessageBox.critical(self.__window, "Error!", "Can't stop Keylogger before Closing")
        return sys.argv

    def show_keylogger_stopped(self):
        self.__start_button.setText("Start")
        self.__set_button.setEnabled(True)

    def __clicked_start(self):
        if self.__start_button.text() == "Start":
            self.__start_button.setText("Stop")
            self.__set_button.setEnabled(False)
            if not self.__control.start():
                QtWidgets.QMessageBox.critical(self.__window, "Error!", "New End-Key could not be set.")
        elif self.__start_button.text() == "Stop":
            self.__start_button.setText("Start")
            self.__set_button.setEnabled(True)
            if not self.__control.stop():
                QtWidgets.QMessageBox.critical(self.__window, "Error!", "New End-Key could not be set.")

    def __clicked_set_key(self):
        self.__start_button.setEnabled(False)
        self.__set_button.setEnabled(False)
        self.__end_key_output.setEnabled(False)
        self.__end_key_label.setEnabled(False)

        self.__end_key_output.setText("Please press a key!")
        self.__end_key_output.setFont(QtGui.QFont("Arial", 11))
        self.__end_key_output.setStyleSheet("color: blue;")

        self.__writer_thread = threading.Thread(target=self.__set_stop_key)
        self.__writer_thread.daemon = True
        self.__writer_thread.start()

    def __set_stop_key(self):
        if not self.__control.set_stop_key():
            QtWidgets.QMessageBox.critical(self.__window, "Error!", "New End-Key could not be set.")
        self.__end_key_output.setText(self.__control.get_stop_key())

        self.__end_key_output.setFont(QtGui.QFont("Arial", 12))
        self.__end_key_output.setStyleSheet("color: black;")
        self.__start_button.setEnabled(True)
        self.__set_button.setEnabled(True)
        self.__end_key_output.setEnabled(True)
        self.__end_key_label.setEnabled(True)
