from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

from Forms.AdminWindow import Ui_AdminWindow
from PyQt5 import QtCore, QtGui, QtWidgets

from SqlQuery.SqlQuery import SqlQuery
from WindowStarts.ChangePurchasedService import ChangePurchasedService
from WindowStarts.ChangeStaff import ChangeStaff
from WindowStarts.ChangeVisitor import ChangeVisitor
from WindowStarts.YieldWindow import YieldWindow


class AdminWindow(QtWidgets.QMainWindow, Ui_AdminWindow):
    def __init__(self, ID, sql, parent=None):
        super(AdminWindow, self).__init__(parent)
        self.ID = ID
        self.setupUi(self)

        self.rowV = 0
        self.rowS = 0
        self.rowPS = 0

        self.pushExit.clicked.connect(self.showLogin)
        self.refresh.clicked.connect(self.Refresh)

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

        self.tableWidget_S.itemClicked.connect(self.itemClickedS)
        self.tableWidget_V.itemClicked.connect(self.itemClickedV)
        self.tableWidget_PS.itemClicked.connect(self.itemClickedPS)

        self.addItems()


    def showLogin(self):
        self.parent().show()
        self.hide()

    def itemClickedS(self, item):
        self.rowS = item.row()
    def itemClickedV(self, item):
        self.rowV = item.row()

    def itemClickedPS(self, item):
        self.rowPS = item.row()

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

        self.Dohod.clicked.connect(self.dohod)


    def addItems(self):
        for i in range(len(self.purchasedData['Visitor_ID'])):
            for j in range(len(self.headerLabels_PS)):
                item = QTableWidgetItem(str(self.purchasedData[self.headerLabels_PS[j]][i]))
                self.tableWidget_PS.setItem(i, j, item)

        for i in range(len(self.staffData['Surname'])):
            for j in range(len(self.headerLabels_S)):
                item = QTableWidgetItem(str(self.staffData[self.headerLabels_S[j]][i]))
                self.tableWidget_S.setItem(i, j, item)

        for i in range(len(self.visitorData['Surname'])):
            for j in range(len(self.headerLabels_V)):
                item = QTableWidgetItem(str(self.visitorData[self.headerLabels_V[j]][i]))
                self.tableWidget_V.setItem(i, j, item)

        self.tableWidget_PS.show()
        self.tableWidget_S.show()
        self.tableWidget_V.show()

    def dohod(self):
        dohod_window = YieldWindow(sql=self.sql, parent=self)
        dohod_window.show()
    def AddStaff(self):
        changeS = ChangeStaff(sql=self.sql, data=[], parent=self)
        changeS.show()

    def AddVisitor(self):
        changeV = ChangeVisitor(sql=self.sql, data=[], parent=self)
        changeV.show()

    def AddPurchased(self):
        changePS = ChangePurchasedService(sql=self.sql, data=[], parent=self)
        changePS.show()

    def ChangeStaff(self):
        data = []
        for i in range(10):
            data.append(self.tableWidget_S.item(self.rowS, i).text())

        changeS = ChangeStaff(sql=self.sql, data=data, parent=self)
        changeS.show()

    def ChangeVisitor(self):
        data = []
        for i in range(7):
            data.append(self.tableWidget_V.item(self.rowV, i).text())

        changeS = ChangeVisitor(sql=self.sql, data=data, parent=self)
        changeS.show()

    def ChangePurchased(self):
        data = []
        for i in range(7):
            data.append(self.tableWidget_PS.item(self.rowPS, i).text())

        changePS = ChangePurchasedService(sql=self.sql, data=data, parent=self)
        changePS.show()

    def RemoveStaff(self):
        confirmation = QMessageBox.question(self, 'Подтверждение', 'Вы уверены что хотите удалить запись',
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if confirmation == QMessageBox.Yes:
            try:
                self.sql.sql_delete("Staff", "Staff_ID", self.tableWidget_S.item(self.rowS, 0).text())
            except:
                pass

    def RemoveVisitor(self):
        confirmation = QMessageBox.question(self, 'Подтверждение', 'Вы уверены что хотите удалить запись',
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if confirmation == QMessageBox.Yes:
            try:
                self.sql.sql_delete("Visitors", "Visitor_ID", self.tableWidget_V.item(self.rowV, 0).text())
            except:
                pass

    def RemovePurchased(self):
        confirmation = QMessageBox.question(self, 'Подтверждение', 'Вы уверены что хотите удалить запись',
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if confirmation == QMessageBox.Yes:
            try:
                self.sql.sql_delete("PurchasedService", "PurchasedService_ID", self.tableWidget_PS.item(self.rowPS, 0).text())
            except:
                pass



    def Refresh(self):
        self.tableWidget_S.clear()
        self.tableWidget_V.clear()
        self.tableWidget_PS.clear()

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

    def closeEvent(self, a0):
        self.parent().close()
        self.close()