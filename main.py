from PyQt5.QtWidgets import *
import sys
from Layout.Calc import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow): # главное окно



    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)

        self.is_eq = False

        self.add_function()

    def add_function(self):
        self.push0.clicked.connect(lambda: self.PushNumber(self.push0.text()))
        self.push1.clicked.connect(lambda: self.PushNumber(self.push1.text()))
        self.push2.clicked.connect(lambda: self.PushNumber(self.push2.text()))
        self.push3.clicked.connect(lambda: self.PushNumber(self.push3.text()))
        self.push4.clicked.connect(lambda: self.PushNumber(self.push4.text()))
        self.push5.clicked.connect(lambda: self.PushNumber(self.push5.text()))
        self.push6.clicked.connect(lambda: self.PushNumber(self.push6.text()))
        self.push7.clicked.connect(lambda: self.PushNumber(self.push7.text()))
        self.push8.clicked.connect(lambda: self.PushNumber(self.push8.text()))
        self.push9.clicked.connect(lambda: self.PushNumber(self.push9.text()))

        self.pushAdd.clicked.connect(lambda: self.PushNumber(self.pushAdd.text()))
        self.pushDel.clicked.connect(lambda: self.PushNumber(self.pushDel.text()))
        self.pushDiff.clicked.connect(lambda: self.PushNumber(self.pushDiff.text()))
        self.pushMul.clicked.connect(lambda: self.PushNumber(self.pushMul.text()))

        self.pushEqual.clicked.connect(self.results)

    def PushNumber(self, number):
        if self.Result.text() == "0" or self.is_eq:
            self.Result.setText(number)
            self.is_eq = False
        else:
            self.Result.setText(self.Result.text() + number)

    def results(self):
        res = eval(self.Result.text())
        self.Result.setText(str(res))
        self.is_eq = True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
    print(1)