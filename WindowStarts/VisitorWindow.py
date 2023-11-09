from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Forms.StaffWindow import Ui_StaffWindow
from Forms.VisitorWindow import Ui_VisitorWindow


class VisitorWindow(QtWidgets.QMainWindow, Ui_VisitorWindow):
    def __init__(self, ID, sql, parent=None):
        super(VisitorWindow, self).__init__(parent)
        self.ID = ID
        self.sql = sql
        self.setupUi(self)

        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setHorizontalHeaderLabels(['Услуга', 'Стоимость'])
        self.tableWidget.setShowGrid(False)

        self.activeServices = [False, False, False, False,
                              False, False, False, False]
        self.chosenPackage = 'packNo'

        self.pack1.toggled.connect(lambda: self.packageSet("Pack1"))
        self.pack2.toggled.connect(lambda: self.packageSet("Pack2"))
        self.pack3.toggled.connect(lambda: self.packageSet("Pack3"))
        self.pack4.toggled.connect(lambda: self.packageSet("Pack4"))
        self.pack5.toggled.connect(lambda: self.packageSet("Pack5"))
        self.pack6.toggled.connect(lambda: self.packageSet("Pack6"))
        self.packNo.toggled.connect(lambda: self.packageSet("PackNo"))

        self.Service1.toggled.connect(self.serviceSet)
        self.Service2.toggled.connect(self.serviceSet)
        self.Service3.toggled.connect(self.serviceSet)
        self.Service4.toggled.connect(self.serviceSet)
        self.Service5.toggled.connect(self.serviceSet)
        self.Service6.toggled.connect(self.serviceSet)
        self.Service7.toggled.connect(self.serviceSet)

        self.pushExit.clicked.connect(self.showLogin)

        self.pushPay.clicked.connect(self.pay)

    def showLogin(self):
        self.parent().show()
        self.hide()

    def packageSet(self, Id):
        self.chosenPackage = Id

    def serviceSet(self):
        if self.Service1.isChecked(): self.activeServices[0] = True
        else: self.activeServices[0] = False

        if self.Service2.isChecked(): self.activeServices[1] = True
        else: self.activeServices[1] = False

        if self.Service3.isChecked(): self.activeServices[2] = True
        else: self.activeServices[2] = False

        if self.Service4.isChecked(): self.activeServices[3] = True
        else: self.activeServices[3] = False

        if self.Service5.isChecked(): self.activeServices[4] = True
        else: self.activeServices[4] = False

        if self.Service6.isChecked(): self.activeServices[5] = True
        else: self.activeServices[5] = False

        if self.Service7.isChecked(): self.activeServices[6] = True
        else: self.activeServices[6] = False

        print(self.activeServices)

    def pay(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Подтверждение")
        msg.setText("Вы уверены что хотите совершить покупку")
        msg.setIcon(QMessageBox.Information)
        msg.addButton(QMessageBox.Ok)

        res = msg.show()

        if res == QMessageBox.Ok:
            pass
            print('ok press')
        if self.chosenPackage == 'packNo':
            for i in range(len(self.activeServices)):
                if self.activeServices[i]:
                    pass
        else:
            self.sql.add_package(self.chosenPackage, self.ID)


    def closeEvent(self, a0):
        self.parent().close()
        self.close()