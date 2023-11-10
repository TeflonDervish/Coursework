from PyQt5 import QtWidgets

from Forms.ChangeVisitor import Ui_ChangeVisitor


class ChangeVisitor(QtWidgets.QMainWindow, Ui_ChangeVisitor):
    def __init__(self, sql, data, parent=None):
        super(ChangeVisitor, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.pushOk)

        self.data = data
        self.sql = sql

        if not data:
            self.mod = 'insert'
        else:
            self.mod = 'update'

            self.Surname.setText(data[1])
            self.Name.setText(data[2])
            self.phoneNumber.setText(data[3])
            self.Email.setText(data[4])
            self.Login.setText(data[5])
            self.Password.setText(data[6])


    def pushOk(self):
        surname = self.Surname.text()
        name = self.Name.text()
        phone = self.phoneNumber.text()
        email = self.Email.text()
        login = self.Login.text()
        password = self.Password.text()
        print(1)
        if self.mod == 'insert':
            self.sql.sql_insert('Visitors', ["'" + surname + "'",
                                            "'" + name + "'",
                                            "'" + phone + "'",
                                            "'" + email + "'",
                                            "'" + login + "'",
                                            "'" + password + "'"])
        elif self.mod == 'update':
            self.sql.query("UPDATE Visitors SET " +
                           "Surname = '" + surname +
                           "', Name = '" + name +
                           "', PhoneNumber = '" + phone +
                           "', Email = '" + email +
                           "', login = '" + login +
                           "', password = '" + password +
                           "' WHERE Visitor_ID = " + self.data[0] + ';')
        self.close()