from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from Forms.YieldWindow import Ui_YieldWindow


class YieldWindow(QtWidgets.QMainWindow, Ui_YieldWindow):
    def __init__(self, sql, parent=None):
        super(YieldWindow, self).__init__(parent)
        self.setupUi(self)
        self.findButton.clicked.connect(self.Find)
        self.sql = sql
        self.data = []

    def Find(self):
        start_time = self.startTime.dateTime().toString('yyyy-dd-MM hh:mm')
        end_time = self.endTime.dateTime().toString('yyyy-dd-MM hh:mm')
        self.data = self.sql.service_profit(startTime=start_time, endTime=end_time)
        print(self.data)
        self.addItems()

    def addItems(self):
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(['Имя услуги', 'Стоимость'])
        self.tableWidget.setRowCount(len(self.data['Имя услуги']))
        self.tableWidget.setShowGrid(False)
        for i in range(len(self.data['Имя услуги'])):
            item = QTableWidgetItem(self.data['Имя услуги'][i])
            self.tableWidget.setItem(i, 0, item)

            item = QTableWidgetItem(self.data['Стоимость'][i])
            self.tableWidget.setItem(i, 1, item)

        self.tableWidget.show()