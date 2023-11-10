from PyQt5 import QtWidgets
from PyQt5.QtCore import QTime, QDateTime
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

from Forms.StaffWindow import Ui_StaffWindow
from Forms.VisitorWindow import Ui_VisitorWindow


class VisitorWindow(QtWidgets.QMainWindow, Ui_VisitorWindow):
    def __init__(self, ID, sql, parent=None):
        super(VisitorWindow, self).__init__(parent)
        self.ID = ID
        self.sql = sql
        self.setupUi(self)

        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(8)
        self.tableWidget.setHorizontalHeaderLabels(['Услуга', 'Стоимость'])

        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        self.serviceTime.setDateTime(QDateTime.currentDateTime())

        self.activeServices = [False, False, False, False, False, False, False, False]
        self.chosenPackage = 'PackNo'

        self.pack1.toggled.connect(lambda: self.packageSet("Pack1"))
        self.pack2.toggled.connect(lambda: self.packageSet("Pack2"))
        self.pack3.toggled.connect(lambda: self.packageSet("Pack3"))
        self.pack4.toggled.connect(lambda: self.packageSet("Pack4"))
        self.pack5.toggled.connect(lambda: self.packageSet("Pack5"))
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
        self.tableWidget.clear()
        if Id == 'Pack1':
            item = QTableWidgetItem('Час батутов')
            self.tableWidget.setItem(0, 0, item)
            item = QTableWidgetItem('350')
            self.tableWidget.setItem(0, 1, item)

            item = QTableWidgetItem('Итого:')
            self.tableWidget.setItem(1, 0, item)
            item = QTableWidgetItem('350')
            self.tableWidget.setItem(1, 1, item)
        elif Id == 'Pack2':
            item = QTableWidgetItem('Анимация')
            self.tableWidget.setItem(0, 0, item)
            item = QTableWidgetItem('2200')
            self.tableWidget.setItem(0, 1, item)

            item = QTableWidgetItem('Час батутов')
            self.tableWidget.setItem(1, 0, item)
            item = QTableWidgetItem('350')
            self.tableWidget.setItem(1, 1, item)

            item = QTableWidgetItem('Комната для чаепития')
            self.tableWidget.setItem(2, 0, item)
            item = QTableWidgetItem('2200')
            self.tableWidget.setItem(2, 1, item)

            item = QTableWidgetItem('Итого:')
            self.tableWidget.setItem(3, 0, item)
            item = QTableWidgetItem('4750')
            self.tableWidget.setItem(3, 1, item)
        elif Id == 'Pack3':
            item = QTableWidgetItem('Анимация')
            self.tableWidget.setItem(0, 0, item)
            item = QTableWidgetItem('2200')
            self.tableWidget.setItem(0, 1, item)

            item = QTableWidgetItem('Гигапузыри')
            self.tableWidget.setItem(1, 0, item)
            item = QTableWidgetItem('999.99')
            self.tableWidget.setItem(1, 1, item)

            item = QTableWidgetItem('Час батутов')
            self.tableWidget.setItem(2, 0, item)
            item = QTableWidgetItem('350')
            self.tableWidget.setItem(2, 1, item)

            item = QTableWidgetItem('Комната для чаепития')
            self.tableWidget.setItem(3, 0, item)
            item = QTableWidgetItem('2000')
            self.tableWidget.setItem(3, 1, item)

            item = QTableWidgetItem('Итого:')
            self.tableWidget.setItem(4, 0, item)
            item = QTableWidgetItem(str(2200 + 999.99 + 350 + 2000))
            self.tableWidget.setItem(4, 1, item)
        elif Id == 'Pack4':
            item = QTableWidgetItem('Анимация')
            self.tableWidget.setItem(0, 0, item)
            item = QTableWidgetItem('2200')
            self.tableWidget.setItem(0, 1, item)

            item = QTableWidgetItem('Пиньята')
            self.tableWidget.setItem(1, 0, item)
            item = QTableWidgetItem('2200')
            self.tableWidget.setItem(1, 1, item)

            item = QTableWidgetItem('Час батутов')
            self.tableWidget.setItem(2, 0, item)
            item = QTableWidgetItem('350')
            self.tableWidget.setItem(2, 1, item)

            item = QTableWidgetItem('Комната для чаепития')
            self.tableWidget.setItem(3, 0, item)
            item = QTableWidgetItem('2000')
            self.tableWidget.setItem(3, 1, item)

            item = QTableWidgetItem('Итого:')
            self.tableWidget.setItem(4, 0, item)
            item = QTableWidgetItem(str(2200 + 2220 + 350 + 2000))
            self.tableWidget.setItem(4, 1, item)
        elif Id == 'Pack5':
            item = QTableWidgetItem('Анимация')
            self.tableWidget.setItem(0, 0, item)
            item = QTableWidgetItem('2200')
            self.tableWidget.setItem(0, 1, item)

            item = QTableWidgetItem('Гигапузыри')
            self.tableWidget.setItem(1, 0, item)
            item = QTableWidgetItem('999.99')
            self.tableWidget.setItem(1, 1, item)

            item = QTableWidgetItem('Пиньята')
            self.tableWidget.setItem(2, 0, item)
            item = QTableWidgetItem('2200')
            self.tableWidget.setItem(2, 1, item)

            item = QTableWidgetItem('Час батутов')
            self.tableWidget.setItem(3, 0, item)
            item = QTableWidgetItem('350')
            self.tableWidget.setItem(3, 1, item)

            item = QTableWidgetItem('Комната для чаепития')
            self.tableWidget.setItem(4, 0, item)
            item = QTableWidgetItem('2000')
            self.tableWidget.setItem(4, 1, item)

            item = QTableWidgetItem('Итого:')
            self.tableWidget.setItem(5, 0, item)
            item = QTableWidgetItem(str(2200 + 2220 + 350 + 2000 + 999.99))
            self.tableWidget.setItem(5, 1, item)
        elif Id == 'PackNo':
            self.serviceSet()

    def serviceSet(self):
        if self.chosenPackage == 'PackNo':
            self.tableWidget.clear()
            sum_service = 0
            index = 0
            if self.Service1.isChecked():
                item = QTableWidgetItem('Комната бабочки')
                self.tableWidget.setItem(index, 0, item)
                item = QTableWidgetItem('2000')
                self.tableWidget.setItem(index, 1, item)
                sum_service += 2000
                index += 1
            if self.Service2.isChecked():
                item = QTableWidgetItem('Комната радуги')
                self.tableWidget.setItem(index, 0, item)
                item = QTableWidgetItem('2000')
                self.tableWidget.setItem(index, 1, item)
                sum_service += 2000
                index += 1
            if self.Service3.isChecked():
                item = QTableWidgetItem('Комната тачки')
                self.tableWidget.setItem(index, 0, item)
                item = QTableWidgetItem('2000')
                self.tableWidget.setItem(index, 1, item)
                sum_service += 2000
                index += 1
            if self.Service4.isChecked():
                item = QTableWidgetItem('Комната шар')
                self.tableWidget.setItem(index, 0, item)
                item = QTableWidgetItem('2000')
                self.tableWidget.setItem(index, 1, item)
                sum_service += 2000
                index += 1
            if self.Service5.isChecked():
                item = QTableWidgetItem('Анимация')
                self.tableWidget.setItem(index, 0, item)
                item = QTableWidgetItem('2200')
                self.tableWidget.setItem(index, 1, item)
                sum_service += 2200
                index += 1
            if self.Service6.isChecked():
                item = QTableWidgetItem('Тренерство')
                self.tableWidget.setItem(index, 0, item)
                item = QTableWidgetItem('2200')
                self.tableWidget.setItem(index, 1, item)
                sum_service += 2200
                index += 1
            if self.Service7.isChecked():
                item = QTableWidgetItem('Квест')
                self.tableWidget.setItem(index, 0, item)
                item = QTableWidgetItem('1500')
                self.tableWidget.setItem(index, 1, item)
                sum_service += 1500
                index += 1
            if index > 0:
                item = QTableWidgetItem('Итого')
                self.tableWidget.setItem(index, 0, item)
                item = QTableWidgetItem(str(sum_service))
                self.tableWidget.setItem(index, 1, item)



    def pay(self):
        confirmation = QMessageBox.question(self, 'Подтверждение', 'Вы уверены что хотите совершить покупку', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if confirmation == QMessageBox.Yes:
            time = self.dateTimeEdit.dateTime().toString('yyyy-dd-MM hh:mm')

            if self.chosenPackage == 'PackNo':
                if self.Service1.isChecked():
                    self.sql.sql_insert('PurchasedService', [str(self.ID), 'NULL', '0', '2000', "'" + time + "'", "'" + time + "'"])
                if self.Service2.isChecked():
                    self.sql.sql_insert('PurchasedService', [str(self.ID), 'NULL', '1', '2000', "'" + time + "'", "'" + time + "'"])
                if self.Service3.isChecked():
                    self.sql.sql_insert('PurchasedService', [str(self.ID), 'NULL', '2', '2000', "'" + time + "'", "'" + time + "'"])
                if self.Service4.isChecked():
                    self.sql.sql_insert('PurchasedService', [str(self.ID), 'NULL', '3', '2000', "'" + time + "'", "'" + time + "'"])
                if self.Service5.isChecked():
                    self.sql.sql_insert('PurchasedService', [str(self.ID), 'NULL', '4', '2200', "'" + time + "'", "'" + time + "'"])
                if self.Service6.isChecked():
                    self.sql.sql_insert('PurchasedService', [str(self.ID), 'NULL', '5', '2200', "'" + time + "'", "'" + time + "'"])
                if self.Service7.isChecked():
                    self.sql.sql_insert('PurchasedService', [str(self.ID), 'NULL', '9', '1500', "'" + time + "'", "'" + time + "'"])
            else:
                self.sql.add_package(self.chosenPackage, self.ID, time)


    def closeEvent(self, a0):
        self.parent().close()
        self.close()