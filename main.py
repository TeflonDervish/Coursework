from PyQt5.QtWidgets import *
import sys

from Forms.LoginWindow import Ui_LoginWindow


class MainWindow(QMainWindow, Ui_LoginWindow): # главное окно

    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)

        self.is_eq = False

        self.add_function()

    def add_function(self):
        self.pushLogin.clicked.connect(self.pressLogin)

    def pressLogin(self):
        error = QMessageBox()

        date = QDateEdit
        date.exec_()
        error.setWindowTitle("Ошибка")
        error.setText("Сейчас нельзя")
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)

        error.setDefaultButton(QMessageBox.Ok)
        error.setInformativeText("Пизда тебе")
        error.setDetailedText("Тикай с городу")

        error.buttonClicked.connect(self.popup_action)

        error.exec_()

    def popup_action(self, btn):
        if btn.text() == 'Ok':
            print("Зоебись")
        elif btn.text() == 'Reset':
            self.pushLogin.setText("Пизда тебе")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())