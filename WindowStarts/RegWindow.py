from PyQt5 import QtCore, QtGui, QtWidgets

from Forms.RegWindow import Ui_RegWindow
from WindowStarts.LoginWindow import LoginWindow


class RegWindow(QtWidgets.QMainWindow, Ui_RegWindow):
    def __init__(self, parent=None):
        super(RegWindow, self).__init__(parent)
        self.setupUi(self)

        self.pushLogin.clicked.connect(self.showLoginWindow)

    def showLoginWindow(self):
        self.loginWindow = LoginWindow()
        self.loginWindow.show()
        self.close()
