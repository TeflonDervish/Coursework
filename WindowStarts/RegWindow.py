from PyQt5 import QtCore, QtGui, QtWidgets

from Forms.RegWindow import Ui_RegWindow


class RegWindow(QtWidgets.QMainWindow, Ui_RegWindow):
    def __init__(self, parent=None):
        super(RegWindow, self).__init__(parent)
        self.setupUi(self)

