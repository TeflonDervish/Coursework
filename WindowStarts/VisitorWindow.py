from PyQt5 import QtWidgets

from Forms.StaffWindow import Ui_StaffWindow
from Forms.VisitorWindow import Ui_VisitorWindow


class VisitorWindow(QtWidgets.QMainWindow, Ui_VisitorWindow):
    def __init__(self, ID, sql, parent=None):
        super(VisitorWindow, self).__init__(parent)
        self.ID = ID
        self.sql = sql
        self.setupUi(self)

        self.pushExit.clicked.connect(self.showLogin)

    def showLogin(self):
        self.parent().show()
        self.hide()