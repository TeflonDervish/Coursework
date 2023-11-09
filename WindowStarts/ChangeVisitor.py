from PyQt5 import QtWidgets

from Forms.ChangeVisitor import Ui_ChangeVisitor


class ChangeVisitor(QtWidgets.QMainWindow, Ui_ChangeVisitor):
    def __init__(self, data, parent=None):
        super(ChangeVisitor, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.pushOk)

        def pushOk(self):
            self.close()