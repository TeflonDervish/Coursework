# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Layout/ChangeStaff.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChangeStaff(object):
    def setupUi(self, ChangeStaff):
        ChangeStaff.setObjectName("ChangeStaff")
        ChangeStaff.resize(446, 372)
        ChangeStaff.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.formLayoutWidget = QtWidgets.QWidget(ChangeStaff)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 0, 431, 366))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.Surname = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Surname.setObjectName("Surname")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Surname)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.Name = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Name.setObjectName("Name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Name)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.phoneNumber = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.phoneNumber.setObjectName("phoneNumber")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.phoneNumber)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.Email = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Email.setObjectName("Email")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Email)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.LaborBook = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.LaborBook.setObjectName("LaborBook")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.LaborBook)
        self.MedicalBook = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.MedicalBook.setObjectName("MedicalBook")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.MedicalBook)
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.SpanningRole, self.pushButton)
        self.Login = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Login.setObjectName("Login")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.Login)
        self.Password = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Password.setObjectName("Password")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.Password)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_9)

        self.retranslateUi(ChangeStaff)
        QtCore.QMetaObject.connectSlotsByName(ChangeStaff)

    def retranslateUi(self, ChangeStaff):
        _translate = QtCore.QCoreApplication.translate
        ChangeStaff.setWindowTitle(_translate("ChangeStaff", "Добавить/Изменить сотрудника"))
        self.label.setText(_translate("ChangeStaff", "Фамилия"))
        self.label_2.setText(_translate("ChangeStaff", "Имя"))
        self.label_3.setText(_translate("ChangeStaff", "Тел. номер"))
        self.label_4.setText(_translate("ChangeStaff", "Email"))
        self.label_5.setText(_translate("ChangeStaff", "Номер трудовой"))
        self.pushButton.setText(_translate("ChangeStaff", "ОК"))
        self.label_6.setText(_translate("ChangeStaff", "Номер медицинской"))
        self.label_7.setText(_translate("ChangeStaff", "Логин"))
        self.label_8.setText(_translate("ChangeStaff", "Пароль"))
        self.comboBox.setItemText(0, _translate("ChangeStaff", "0"))
        self.comboBox.setItemText(1, _translate("ChangeStaff", "1"))
        self.label_9.setText(_translate("ChangeStaff", "Мод доступа"))
