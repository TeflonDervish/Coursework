from PyQt5.QtWidgets import QTableWidgetItem

from Forms.AdminWindow import Ui_AdminWindow
from PyQt5 import QtCore, QtGui, QtWidgets

from SqlQuery.SqlQuery import SqlQuery


class AdminWindow(QtWidgets.QMainWindow, Ui_AdminWindow):
    def __init__(self, ID, sql, parent=None):
        super(AdminWindow, self).__init__(parent)
        self.ID = ID
        self.setupUi(self)

        self.pushExit.clicked.connect(self.showLogin)

        self.sql = sql

        self.buttonConnect()

        self.staffData = self.sql.get_staff()
        self.visitorData = self.sql.get_visitors()
        self.purchasedData = self.sql.get_purchased_service()

        self.tableWidget_PS.setColumnCount(len(self.purchasedData))
        self.tableWidget_PS.setRowCount(len(self.purchasedData["Visitor_ID"]))
        self.headerLabels_PS = list(self.purchasedData)
        self.tableWidget_PS.setHorizontalHeaderLabels(self.headerLabels_PS)
        self.tableWidget_PS.setShowGrid(False)

        self.tableWidget_S.setColumnCount(len(self.staffData))
        self.tableWidget_S.setRowCount(len(self.staffData["Surname"]))
        self.headerLabels_S = list(self.staffData)
        self.tableWidget_S.setHorizontalHeaderLabels(self.headerLabels_S)
        self.tableWidget_S.setShowGrid(False)

        self.tableWidget_V.setColumnCount(len(self.visitorData))
        self.tableWidget_V.setRowCount(len(self.visitorData["Surname"]))
        self.headerLabels_V = list(self.visitorData)
        self.tableWidget_V.setHorizontalHeaderLabels(self.headerLabels_V)
        self.tableWidget_V.setShowGrid(False)

        self.addItems()


    def showLogin(self):
        self.parent().show()
        self.hide()

    def buttonConnect(self):
        self.pushAddStaff.clicked.connect(self.AddStaff)
        self.pushAddVisitor.clicked.connect(self.AddVisitor)
        self.pushAddPurchased_3.clicked.connect(self.AddPurchased)

        self.pushChangeStaff.clicked.connect(self.ChangeStaff)
        self.pushChangeVisistor.clicked.connect(self.ChangeVisitor)
        self.pushChangePurchased_3.clicked.connect(self.ChangePurchased)

        self.pushRemoveStaff.clicked.connect(self.RemoveStaff)
        self.pushRemoveVisitor.clicked.connect(self.RemoveVisitor)
        self.pushRemovePurchased_3.clicked.connect(self.RemovePurchased)

        self.pushSearchStaff.clicked.connect(self.SearchStaff)
        self.pushSearchVisitor.clicked.connect(self.SearchVisitor)
        self.pushSearchPurchased_2.clicked.connect(self.SearchPurchased)


    def addItems(self):
        for i in range(len(self.purchasedData['Visitor_ID'])):
            for j in range(len(self.headerLabels_PS)):
                item = QTableWidgetItem(str(self.purchasedData[self.headerLabels_PS[j]][i]))
                self.tableWidget_PS.setItem(i, j, item)

        for i in range(len(self.staffData['Surname'])):
            for j in range(len(self.headerLabels_S)):
                item = QTableWidgetItem(str(self.staffData[self.headerLabels_S[j]][i]))
                self.tableWidget_S.setItem(i, j, item)
        print(self.visitorData)
        for i in range(len(self.visitorData['Surname'])):
            for j in range(len(self.headerLabels_V)):
                item = QTableWidgetItem(str(self.visitorData[self.headerLabels_V[j]][i]))
                self.tableWidget_V.setItem(i, j, item)

        self.tableWidget_PS.show()
        self.tableWidget_S.show()
        self.tableWidget_V.show()

    def AddStaff(self): pass

    def AddVisitor(self): pass

    def AddPurchased(self): pass

    def ChangeStaff(self): pass

    def ChangeVisitor(self): pass

    def ChangePurchased(self): pass

    def RemoveStaff(self): pass

    def RemoveVisitor(self): pass

    def RemovePurchased(self): pass

    def SearchStaff(self): pass

    def SearchVisitor(self): pass

    def SearchPurchased(self): pass


    def closeEvent(self, a0):
        self.parent().close()
        self.close()