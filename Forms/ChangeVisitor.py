# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Layout/ChangeVisitor.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChangeVisitor(object):
    def setupUi(self, ChangeVisitor):
        ChangeVisitor.setObjectName("ChangeVisitor")
        ChangeVisitor.resize(366, 286)
        ChangeVisitor.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.formLayoutWidget = QtWidgets.QWidget(ChangeVisitor)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 361, 275))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.pushButton)
        self.Email = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Email.setObjectName("Email")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Email)
        self.phoneNumber = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.phoneNumber.setObjectName("phoneNumber")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.phoneNumber)
        self.Name = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Name.setObjectName("Name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Name)
        self.Surname = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Surname.setObjectName("Surname")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Surname)
        self.Login = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Login.setObjectName("Login")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.Login)
        self.Password = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Password.setObjectName("Password")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.Password)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)

        self.retranslateUi(ChangeVisitor)
        QtCore.QMetaObject.connectSlotsByName(ChangeVisitor)

    def retranslateUi(self, ChangeVisitor):
        _translate = QtCore.QCoreApplication.translate
        ChangeVisitor.setWindowTitle(_translate("ChangeVisitor", "Добавить/Изменить посетителя"))
        self.label.setText(_translate("ChangeVisitor", "Фамилия"))
        self.label_2.setText(_translate("ChangeVisitor", "Имя"))
        self.label_3.setText(_translate("ChangeVisitor", "Тел. номер"))
        self.label_4.setText(_translate("ChangeVisitor", "Email"))
        self.pushButton.setText(_translate("ChangeVisitor", "ОК"))
        self.label_5.setText(_translate("ChangeVisitor", "Логин"))
        self.label_6.setText(_translate("ChangeVisitor", "Пароль"))
