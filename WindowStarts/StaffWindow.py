from PyQt5 import QtWidgets

from Forms.StaffWindow import Ui_StaffWindow


class StaffWindow(QtWidgets.QMainWindow, Ui_StaffWindow):
    def __init__(self, parent=None):
        super(StaffWindow, self).__init__()
        self.setupUi(self)