from PyQt5 import QtWidgets

from Forms.StaffWindow import Ui_StaffWindow


class StaffWindow(QtWidgets.QMainWindow, Ui_StaffWindow):
    def __init__(self, ID, sql, parent=None):
        super(StaffWindow, self).__init__(parent)
        self.ID = ID
        self.sql = sql
        self.setupUi(self)

        self.pushExit.clicked.connect(self.showLogin)

    def showLogin(self):
        self.parent().show()
        self.hide()
