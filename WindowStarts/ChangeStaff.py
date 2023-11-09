from PyQt5 import QtWidgets

from Forms.ChangeStaff import Ui_ChangeStaff


class ChangeStaff(QtWidgets.QMainWindow, Ui_ChangeStaff):
    def __init__(self, data, parent=None):
        print(2)
        super(ChangeStaff, self).__init__(parent)
        print(2)
        self.setupUi(self)
        print(2)
        self.pushButton.clicked.connect(self.pushOk)
        print(2)

    def pushOk(self):
        self.close()
