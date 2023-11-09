from PyQt5 import QtWidgets

from Forms.ChangeStaff import Ui_ChangeStaff


class ChangeStaff(QtWidgets.QMainWindow, Ui_ChangeStaff):
    def __init__(self, data, parent=None):
        super(ChangeStaff, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.pushOk)

        def pushOk(self):
            self.close()