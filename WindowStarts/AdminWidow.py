from Forms.AdminWindow import Ui_AdminWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class AdminWindow(QtWidgets.QMainWindow, Ui_AdminWindow):
    def __init__(self, parent=None):
        super(AdminWindow, self).__init__()
        self.setupUi(self)
