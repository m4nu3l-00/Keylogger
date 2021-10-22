import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from view import View
from control import Control


class GUI(View):
    def __init__(self):
        app = QtWidgets.QApplication([])
        window = QtWidgets.QWidget()
        window.setObjectName("Keylogger")
        window.resize(163, 190)
        window.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        window.setWindowTitle("Keylogger")
        self.StartButton = QtWidgets.QPushButton(window)
        self.StartButton.setGeometry(QtCore.QRect(10, 10, 141, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartButton.sizePolicy().hasHeightForWidth())
        self.StartButton.setSizePolicy(sizePolicy)
        self.StartButton.setObjectName("StartButton")
        self.SetButton = QtWidgets.QPushButton(window)
        self.SetButton.setGeometry(QtCore.QRect(10, 60, 141, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SetButton.sizePolicy().hasHeightForWidth())
        self.SetButton.setSizePolicy(sizePolicy)
        self.SetButton.setObjectName("SetButton")
        self.EndKeyOutput = QtWidgets.QLineEdit(window)
        self.EndKeyOutput.setGeometry(QtCore.QRect(10, 140, 141, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EndKeyOutput.sizePolicy().hasHeightForWidth())
        self.EndKeyOutput.setSizePolicy(sizePolicy)
        self.EndKeyOutput.setReadOnly(True)
        self.EndKeyOutput.setObjectName("EndKeyOutput")
        self.label = QtWidgets.QLabel(window)
        self.label.setGeometry(QtCore.QRect(10, 120, 47, 14))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.StartButton.setText("Start")
        self.SetButton.setText("Set end-key")
        self.label.setText("End-key:")

        window.show()
        app.setStyle("Fusion")
        app.exec()

    def start_view(self, control: Control):
        pass#TODO

    def show_keylogger_stopped(self):
        pass # TODO
