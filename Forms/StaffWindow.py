# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Layout/StaffWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StaffWindow(object):
    def setupUi(self, StaffWindow):
        StaffWindow.setObjectName("StaffWindow")
        StaffWindow.resize(904, 561)
        self.centralwidget = QtWidgets.QWidget(StaffWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushExit = QtWidgets.QPushButton(self.centralwidget)
        self.pushExit.setGeometry(QtCore.QRect(760, 0, 141, 31))
        self.pushExit.setObjectName("pushExit")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 30, 901, 531))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setObjectName("tableWidget")
        StaffWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(StaffWindow)
        QtCore.QMetaObject.connectSlotsByName(StaffWindow)

    def retranslateUi(self, StaffWindow):
        _translate = QtCore.QCoreApplication.translate
        StaffWindow.setWindowTitle(_translate("StaffWindow", "Сотрудник"))
        self.pushExit.setText(_translate("StaffWindow", "Выход"))
