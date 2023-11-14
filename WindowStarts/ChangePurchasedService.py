from PyQt5 import QtWidgets
from PyQt5.QtCore import QDateTime

from Forms.ChangePurchasedService import Ui_ChangePurchasedService


class ChangePurchasedService(QtWidgets.QMainWindow, Ui_ChangePurchasedService):
    def __init__(self, sql, data, parent=None):
        super(ChangePurchasedService, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.pushOk)

        self.data = data
        self.sql = sql
        if not data:
            self.mod = 'insert'
        else:
            self.mod = 'update'
            print(1)
            self.visitorID.setText(data[1])
            self.StaffID.setText(data[2])
            self.serviceID.setText(data[3])
            self.Price.setValue(float(data[4]))
            print(int(data[5][0:4]), int(data[5][5:7]), int(data[5][8:10]), int(data[5][11:13]), int(data[5][14: 16]))
            self.StartTime.setDateTime(QDateTime(int(data[5][0:4]), int(data[5][5:7]), int(data[5][8:10]), int(data[5][11:13]), int(data[5][14: 16])))
            self.EndTime.setDateTime(QDateTime(int(data[6][0:4]), int(data[6][5:7]), int(data[6][8:10]), int(data[6][11:13]), int(data[6][14: 16])))


    def pushOk(self):
        visID = self.visitorID.text()
        staID = self.StaffID.text()
        serID = self.serviceID.text()
        price = str(self.Price.value())
        start_time = self.StartTime.dateTime().toString('yyyy-dd-MM hh:mm')
        end_time = self.EndTime.dateTime().toString('yyyy-dd-MM hh:mm')
        if self.mod == 'insert':
            self.sql.sql_insert('PurchasedService', ["'" + visID + "'", "'" + staID + "'", "'" + serID + "'", price,
                                                     "'" + start_time + "'", "'" + end_time + "'"])
        elif self.mod == 'update':
            self.sql.query("UPDATE PurchasedService SET " +
                           "Visitor_ID = '" + visID +
                           "', Staff_ID = '" + staID +
                           "', Service_ID = '" + serID +
                           "', Price = " + price +
                           ", StartTime = '" + start_time +
                           "', EndTime = '" + end_time +
                           "' WHERE PurchasedService_ID = " + self.data[0] + ';')
        self.close()