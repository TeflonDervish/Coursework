from PyQt5 import QtWidgets

from Forms.ChangePurchasedService import Ui_ChangePurchasedService


class ChangePurchasedService(QtWidgets.QMainWindow, Ui_ChangePurchasedService):
    def __init__(self, data, parent=None):
        super(ChangePurchasedService, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.pushOk)

    def pushOk(self):
        self.close()