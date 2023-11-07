from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from Forms.LoginWindow import Ui_LoginWindow
from SqlQuery.SqlQuery import SqlQuery
from WindowStarts.AdminWidow import AdminWindow
from WindowStarts.RegWindow import RegWindow
from WindowStarts.StaffWindow import StaffWindow
from WindowStarts.VisitorWindow import VisitorWindow


class LoginWindow(QtWidgets.QMainWindow, Ui_LoginWindow):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__()
        self.setupUi(self)

        self.pushReg.clicked.connect(self.showRegWindow)
        self.pushLogin.clicked.connect(self.pressLogin)

        self.sql = SqlQuery()


    def keyPressEvent(self, e):
        if (Qt.Key_Enter):
            self.showWindow()

    def showRegWindow(self):
        self.regWindow = RegWindow(self)
        self.regWindow.show()
        self.hide()

    def pressLogin(self):
        self.login = self.Login.text()
        self.password = self.Password.text()

        res = self.sql.chekc_password(self.login, self.password)

        if res[1] == 'Visitor':
            self.visitorWindow = VisitorWindow(self, res[0])
            self.visitorWindow.show()
            self.hide()
        elif res[1] == 'Staff':
            if res[2] == 0:
                self.staffWindow = StaffWindow(self, res[0])
                self.staffWindow.show()
                self.hide()
            elif res[2] == 1:
                self.adminWindow = AdminWindow(self, res[0])
                self.adminWindow.show()
                self.hide()
        elif res[1] == 'Error':
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Неправильный логин или пароль")
            msg.setIcon(QMessageBox.Critical)

            msg.exec_()

