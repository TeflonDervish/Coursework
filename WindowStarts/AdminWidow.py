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

        #self.staffData = self.Sql.get_staff()
        #self.visitorData = self.Sql.get_visitors()
        #self.purchasedData = self.Sql.get_purchased_service()


    def showLogin(self):
        self.parent().show()
        self.hide()

    def buttonConnect(self):
        print(2)
        self.pushAddStaff.clicked.connect(self.AddStaff)
        self.pushAddVisitor.clicked.connect(self.AddVisitor)
        self.pushAddPurchased_3.clicked.connect(self.AddPurchased)

        print(2)
        self.pushChangeStaff.clicked.connect(self.ChangeStaff)
        self.pushChangeVisistor.clicked.connect(self.ChangeVisitor)
        self.pushChangePurchased_3.clicked.connect(self.ChangePurchased)

        print(2)
        self.pushRemoveStaff.clicked.connect(self.RemoveStaff)
        self.pushRemoveVisitor.clicked.connect(self.RemoveVisitor)
        self.pushRemovePurchased_3.clicked.connect(self.RemovePurchased)

        print(2)
        self.pushSearchStaff.clicked.connect(self.SearchStaff)
        self.pushSearchVisitor.clicked.connect(self.SearchVisitor)
        self.pushSearchPurchased_2.clicked.connect(self.SearchPurchased)

        print(2)

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
