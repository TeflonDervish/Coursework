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
        self.regWindow = None
        self.adminWindow = None
        self.staffWindow = None
        self.visitorWindow = None
        self.setupUi(self)

        self.pushReg.clicked.connect(self.showRegWindow)
        self.pushLogin.clicked.connect(self.pressLogin)

        self.sql = SqlQuery()

    def showRegWindow(self):
        self.regWindow = RegWindow(sql=self.sql, parent=self)
        self.regWindow.show()
        self.hide()

    def pressLogin(self):
        self.login = self.Login.text()
        self.password = self.Password.text()

        res = self.sql.chekc_password(self.login, self.password)
        print(res)
        if res[1] == 'Visitor':
            self.visitorWindow = VisitorWindow(res[0], sql=self.sql, parent=self)
            self.visitorWindow.show()
            self.hide()
        elif res[1] == 'Staff':
            self.staffWindow = StaffWindow(res[0], sql=self.sql, parent=self)
            self.staffWindow.show()
            self.hide()
        elif res[1] == "Admin":
            self.adminWindow = AdminWindow(res[0], sql=self.sql, parent=self)
            self.adminWindow.show()
            self.hide()
        elif res[1] == 'Error':
            msg = QMessageBox(self)
            msg.setWindowTitle("Ошибка")
            msg.setText("Неправильный логин или пароль")
            msg.setIcon(QMessageBox.Critical)

            msg.show()

        self.Login.setText('')
        self.Password.setText('')
