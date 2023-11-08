from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from Forms.StaffWindow import Ui_StaffWindow


class StaffWindow(QtWidgets.QMainWindow, Ui_StaffWindow):
    def __init__(self, ID, sql, parent=None):
        super(StaffWindow, self).__init__(parent)
        self.ID = ID
        self.sql = sql
        self.setupUi(self)

        self.data = self.sql.get_staff_info(self.ID)

        self.tableWidget.setColumnCount(len(self.data))
        self.tableWidget.setRowCount(len(self.data["Surname"]))
        self.headerLabels = list(self.data)
        self.tableWidget.setHorizontalHeaderLabels(self.headerLabels)

        self.tableWidget.setShowGrid(False)

        self.pushExit.clicked.connect(self.showLogin)

        self.addItems()

    def showLogin(self):
        self.parent().show()
        self.hide()

    def addItems(self):
        for i in range(len(self.data['Surname'])):
            for j in range(len(self.headerLabels)):
                print(self.data[self.headerLabels[j]])
                item = QTableWidgetItem(str(self.data[self.headerLabels[j]][i]))
                self.tableWidget.setItem(i, j, item)

        self.tableWidget.show()


