# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Layout/VisitorWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VisitorWindow(object):
    def setupUi(self, VisitorWindow):
        VisitorWindow.setObjectName("VisitorWindow")
        VisitorWindow.resize(942, 568)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VisitorWindow.sizePolicy().hasHeightForWidth())
        VisitorWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(VisitorWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 40, 941, 521))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.toolBox = QtWidgets.QToolBox(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.toolBox.setFont(font)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 548, 429))
        self.page.setObjectName("page")
        self.gridLayoutWidget = QtWidgets.QWidget(self.page)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 552, 431))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName("gridLayout")
        self.pack5 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pack5.sizePolicy().hasHeightForWidth())
        self.pack5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pack5.setFont(font)
        self.pack5.setObjectName("pack5")
        self.gridLayout.addWidget(self.pack5, 4, 0, 1, 1)
        self.pack2 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pack2.sizePolicy().hasHeightForWidth())
        self.pack2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pack2.setFont(font)
        self.pack2.setObjectName("pack2")
        self.gridLayout.addWidget(self.pack2, 1, 0, 1, 1)
        self.pack1 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pack1.sizePolicy().hasHeightForWidth())
        self.pack1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pack1.setFont(font)
        self.pack1.setObjectName("pack1")
        self.gridLayout.addWidget(self.pack1, 0, 0, 1, 1)
        self.pack3 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pack3.sizePolicy().hasHeightForWidth())
        self.pack3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pack3.setFont(font)
        self.pack3.setObjectName("pack3")
        self.gridLayout.addWidget(self.pack3, 2, 0, 1, 1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateTimeEdit.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit.setSizePolicy(sizePolicy)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout.addWidget(self.dateTimeEdit, 6, 0, 1, 1)
        self.packNo = QtWidgets.QRadioButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.packNo.sizePolicy().hasHeightForWidth())
        self.packNo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.packNo.setFont(font)
        self.packNo.setObjectName("packNo")
        self.gridLayout.addWidget(self.packNo, 5, 0, 1, 1)
        self.pack4 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pack4.sizePolicy().hasHeightForWidth())
        self.pack4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pack4.setFont(font)
        self.pack4.setObjectName("pack4")
        self.gridLayout.addWidget(self.pack4, 3, 0, 1, 1)
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 548, 429))
        self.page_2.setObjectName("page_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.page_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 541, 431))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Service4 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Service4.sizePolicy().hasHeightForWidth())
        self.Service4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Service4.setFont(font)
        self.Service4.setObjectName("Service4")
        self.gridLayout_2.addWidget(self.Service4, 3, 0, 1, 1)
        self.serviceTime = QtWidgets.QDateTimeEdit(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serviceTime.sizePolicy().hasHeightForWidth())
        self.serviceTime.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.serviceTime.setFont(font)
        self.serviceTime.setObjectName("serviceTime")
        self.gridLayout_2.addWidget(self.serviceTime, 7, 0, 1, 1)
        self.Service2 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Service2.sizePolicy().hasHeightForWidth())
        self.Service2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Service2.setFont(font)
        self.Service2.setObjectName("Service2")
        self.gridLayout_2.addWidget(self.Service2, 1, 0, 1, 1)
        self.Service6 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Service6.sizePolicy().hasHeightForWidth())
        self.Service6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Service6.setFont(font)
        self.Service6.setObjectName("Service6")
        self.gridLayout_2.addWidget(self.Service6, 5, 0, 1, 1)
        self.Service7 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Service7.sizePolicy().hasHeightForWidth())
        self.Service7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Service7.setFont(font)
        self.Service7.setObjectName("Service7")
        self.gridLayout_2.addWidget(self.Service7, 6, 0, 1, 1)
        self.Service3 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Service3.sizePolicy().hasHeightForWidth())
        self.Service3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Service3.setFont(font)
        self.Service3.setObjectName("Service3")
        self.gridLayout_2.addWidget(self.Service3, 2, 0, 1, 1)
        self.Service1 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Service1.sizePolicy().hasHeightForWidth())
        self.Service1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Service1.setFont(font)
        self.Service1.setObjectName("Service1")
        self.gridLayout_2.addWidget(self.Service1, 0, 0, 1, 1)
        self.Service5 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Service5.sizePolicy().hasHeightForWidth())
        self.Service5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Service5.setFont(font)
        self.Service5.setObjectName("Service5")
        self.gridLayout_2.addWidget(self.Service5, 4, 0, 1, 1)
        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 1)
        self.gridLayout_2.setRowStretch(2, 1)
        self.gridLayout_2.setRowStretch(3, 1)
        self.gridLayout_2.setRowStretch(4, 1)
        self.gridLayout_2.setRowStretch(5, 1)
        self.gridLayout_2.setRowStretch(6, 1)
        self.gridLayout_2.setRowStretch(7, 1)
        self.toolBox.addItem(self.page_2, "")
        self.gridLayout_3.addWidget(self.toolBox, 0, 0, 2, 1)
        self.pushPay = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushPay.setFont(font)
        self.pushPay.setObjectName("pushPay")
        self.gridLayout_3.addWidget(self.pushPay, 1, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(10, 30, 351, 421))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(70)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.gridLayout_3.addWidget(self.groupBox, 0, 1, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 3)
        self.gridLayout_3.setColumnStretch(1, 2)
        self.pushExit = QtWidgets.QPushButton(self.centralwidget)
        self.pushExit.setGeometry(QtCore.QRect(840, 0, 101, 41))
        self.pushExit.setObjectName("pushExit")
        VisitorWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(VisitorWindow)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(VisitorWindow)

    def retranslateUi(self, VisitorWindow):
        _translate = QtCore.QCoreApplication.translate
        VisitorWindow.setWindowTitle(_translate("VisitorWindow", "MainWindow"))
        self.pack5.setText(_translate("VisitorWindow", "5 пакет (аниматор + гигапузыри + пиньят + батуты + комната)"))
        self.pack2.setText(_translate("VisitorWindow", "2 пакет (аниматов + батутов + комната)"))
        self.pack1.setText(_translate("VisitorWindow", "Час батутов!!!"))
        self.pack3.setText(_translate("VisitorWindow", "3 пакет (аниматор + гигапузыри + батуты + комната)"))
        self.packNo.setText(_translate("VisitorWindow", "Без пакета"))
        self.pack4.setText(_translate("VisitorWindow", "4 пакет (аниматов + пиньят + батутв + комнатв)"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("VisitorWindow", "Выбрать готовый пакет"))
        self.Service4.setText(_translate("VisitorWindow", "Комната шар (40 мин)"))
        self.Service2.setText(_translate("VisitorWindow", "Комната радуга (40 мин)"))
        self.Service6.setText(_translate("VisitorWindow", "Тренерство (50 мин)"))
        self.Service7.setText(_translate("VisitorWindow", "Квест (30 мин)"))
        self.Service3.setText(_translate("VisitorWindow", "Комната тачки (40 мин)"))
        self.Service1.setText(_translate("VisitorWindow", "Комната бабочки (40 мин)"))
        self.Service5.setText(_translate("VisitorWindow", "Аниматор (50 мин)"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("VisitorWindow", "Собрать свой пакет"))
        self.pushPay.setText(_translate("VisitorWindow", "Оплатить"))
        self.groupBox.setTitle(_translate("VisitorWindow", "Ваш заказ"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("VisitorWindow", "Услуга"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("VisitorWindow", "Цена"))
        self.pushExit.setText(_translate("VisitorWindow", "Выход"))
