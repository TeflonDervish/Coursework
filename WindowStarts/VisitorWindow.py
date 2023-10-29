from PyQt5 import QtWidgets

from Forms.StaffWindow import Ui_StaffWindow
from Forms.VisitorWindow import Ui_VisitorWindow


class VisitorWindow(QtWidgets.QMainWindow, Ui_VisitorWindow):
    def __init__(self, parent=None):
        super(VisitorWindow, self).__init__()
        self.setupUi(self)