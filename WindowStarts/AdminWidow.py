from Forms.AdminWindow import Ui_AdminWindow
from PyQt5 import QtCore, QtGui, QtWidgets

from SqlQuery.SqlQuery import SqlQuery


class AdminWindow(QtWidgets.QMainWindow, Ui_AdminWindow):
    def __init__(self, ID, parent=None):
        super(AdminWindow, self).__init__(parent)
        self.ID = ID
        self.setupUi(self)

        self.pushExit.clicked.connect(self.showLogin)

        self.Sql = SqlQuery()

        self.staffData = self.Sql.get_staff()
        self.visitorData = self.Sql.get_visitors()
        self.purchasedData = self.Sql.get_purchased_service()

        self.buttonConect()

    def showLogin(self):
        self.parent().show()
        self.hide()

    def buttonConnect(self):
        self.pushAddStaff.clicked.connect(self.AddStaff)
        self.pushAddVisito.clicked.connect(self.AddVisitor)
        self.pushAddAdmin.clicked.connect(self.AddAdmin)

        self.pushChangeStaff.clicked.connect(self.ChangeStaff)
        self.pushChangeVisitor.clicked.connect(self.ChangeVisitor)
        self.pushChangeAdmin.clicked.connect(self.ChangeAdmin)

        self.pushRemoveStaff.clicked.connect(self.RemoveStaff)
        self.pushRemoveVisitor.clicked.connect(self.RemoveVisitor)
        self.pushRemoveAdmin.clicked.connect(self.RemoveAdmin)

        self.pushSearchStaff.clicked.connect(self.SearchStaff)
        self.pushSearchVisior.clicked.connect(self.SearchVisitor)
        self.pushSearchAdmin.clicked.connect(self.SearchAdmin)

    def AddStaff(self): pass
    def AddVisitor(self): pass
    def AddAdmin(self): pass

    def ChangeStaff(self): pass

    def ChangeVisitor(self): pass

    def ChangeAdmin(self): pass

    def RemoveStaff(self): pass

    def RemoveVisitor(self): pass

    def RemoveAdmin(self): pass