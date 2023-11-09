from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Forms.RegWindow import Ui_RegWindow


class RegWindow(QtWidgets.QMainWindow, Ui_RegWindow):
    def __init__(self, sql, parent=None):
        super(RegWindow, self).__init__(parent)
        self.setupUi(self)
        self.sql = sql

        self.pushLogin.clicked.connect(self.showLogin)
        self.pushReg.clicked.connect(self.pushAddVisitor)

    def showLogin(self):
        self.parent().show()
        self.hide()

    def pushAddVisitor(self):
        surname = self.Surname.text()
        name = self.Name.text()
        phoneNumber = self.PhoneNumber.text()
        email = self.Email.text()
        login = self.Login.text()
        password = self.Password.text()

        text_error = ''

        if surname == '':
            text_error = 'Пожалуйста введите Фамилию'
        elif name == '':
            text_error = 'Пожалуйста введите Имя'
        elif phoneNumber == '':
            text_error = 'Пожалуйста введите Телефонный номер'
        elif email == '':
            text_error = 'Пожалуйста введите Email'
        elif login == '':
            text_error = 'Пожалуйста введите Логин'
        elif password == '':
            text_error = 'Пожалуйста введите Пароль'

        if text_error == '':
            print(1)
            self.sql.sql_insert("Visitors", [surname, name, phoneNumber, email, login, password])
            self.parent().show()
            self.hide()
        else:
            msg = QMessageBox(self)
            msg.setWindowTitle("Ошибка")
            msg.setText(text_error)
            msg.setIcon(QMessageBox.Critical)
            msg.addButton(QMessageBox.Ok)

            msg.show()


    def closeEvent(self, a0):
        self.parent().close()
        self.close()
