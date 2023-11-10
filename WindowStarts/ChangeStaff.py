from PyQt5 import QtWidgets

from Forms.ChangeStaff import Ui_ChangeStaff


class ChangeStaff(QtWidgets.QMainWindow, Ui_ChangeStaff):
    def __init__(self, sql, data, parent=None):
        super(ChangeStaff, self).__init__(parent)
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
            self.LaborBook.setText(data[5])
            self.MedicalBook.setText(data[6])
            self.Login.setText(data[7])
            self.Password.setText(data[8])
            self.comboBox.setCurrentText(data[9])

        print(1)

    def pushOk(self):
        surname = self.Surname.text()
        name = self.Name.text()
        phone = self.phoneNumber.text()
        email = self.Email.text()
        laborBook = self.LaborBook.text()
        medBook = self.MedicalBook.text()
        login = self.Login.text()
        password = self.Password.text()
        access_mod = self.comboBox.currentText()
        print(access_mod)
        if self.mod == 'insert':
            self.sql.sql_insert("Staff", ["'" + surname + "'", "'" + name + "'", "'" + phone + "'", "'" + email + "'",
                                          laborBook, medBook, "'" + login + "'", "'" + password + "'", access_mod])
        elif self.mod == 'update':
            self.sql.query("UPDATE Staff SET " +
                           "Surname = '" + surname +
                           "', Name = '" + name +
                           "', MiddleName = '" + '' +
                           "', LaborBookName = " + laborBook +
                           ", MedicalBookName = " + medBook +
                           ", login = '" + login +
                           "', password = '" + password +
                           "', access_mod = " + access_mod +
                           " WHERE Staff_ID = " + self.data[0] + ';')
        self.close()
