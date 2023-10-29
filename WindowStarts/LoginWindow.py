from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from Forms.LoginWindow import Ui_LoginWindow
from WindowStarts.AdminWidow import AdminWindow
from WindowStarts.RegWindow import RegWindow
from WindowStarts.StaffWindow import StaffWindow
from WindowStarts.VisitorWindow import VisitorWindow


class LoginWindow(QtWidgets.QMainWindow, Ui_LoginWindow):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__()
        self.setupUi(self)

        self.pushReg.clicked.connect(self.showRegWindow)
        self.pushLogin.clicked.connect(self.showWindow)

    def keyPressEvent(self, e):
        if (Qt.Key_Enter):
            self.showWindow()

    def showRegWindow(self):
        self.regWindow = RegWindow()
        self.regWindow.show()
        self.close()

    def showWindow(self):
        if self.Login.text() == 'admin':
            self.adminWindow = AdminWindow()
            self.adminWindow.show()
            self.close()
        elif self.Login.text() == 'visitor':
            self.visitorWindow = VisitorWindow()
            self.visitorWindow.show()
            self.close()
        elif self.Login.text() == 'staff':
            self.staffWindow = StaffWindow()
            self.staffWindow.show()
            self.close()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Неправильный логин или пароль")
            msg.setIcon(QMessageBox.Critical)

            msg.exec_()

