# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Layout/LoginWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(300, 250)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginWindow.sizePolicy().hasHeightForWidth())
        LoginWindow.setSizePolicy(sizePolicy)
        LoginWindow.setStyleSheet("")
        self.pushLogin = QtWidgets.QPushButton(LoginWindow)
        self.pushLogin.setGeometry(QtCore.QRect(80, 150, 141, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushLogin.setFont(font)
        self.pushLogin.setObjectName("pushLogin")
        self.Login = QtWidgets.QLineEdit(LoginWindow)
        self.Login.setGeometry(QtCore.QRect(50, 60, 200, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Login.setFont(font)
        self.Login.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.Login.setInputMask("")
        self.Login.setText("")
        self.Login.setObjectName("Login")
        self.Password = QtWidgets.QLineEdit(LoginWindow)
        self.Password.setGeometry(QtCore.QRect(50, 110, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Password.setFont(font)
        self.Password.setInputMask("")
        self.Password.setText("")
        self.Password.setObjectName("Password")
        self.pushReg = QtWidgets.QPushButton(LoginWindow)
        self.pushReg.setGeometry(QtCore.QRect(80, 200, 141, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushReg.setFont(font)
        self.pushReg.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushReg.setToolTipDuration(0)
        self.pushReg.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushReg.setObjectName("pushReg")
        self.labelLogin = QtWidgets.QLabel(LoginWindow)
        self.labelLogin.setGeometry(QtCore.QRect(50, 10, 201, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.labelLogin.setFont(font)
        self.labelLogin.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelLogin.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLogin.setObjectName("labelLogin")
        self.line = QtWidgets.QFrame(LoginWindow)
        self.line.setGeometry(QtCore.QRect(20, 180, 261, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Вход"))
        self.pushLogin.setText(_translate("LoginWindow", "Войти"))
        self.Login.setPlaceholderText(_translate("LoginWindow", "Login"))
        self.Password.setPlaceholderText(_translate("LoginWindow", "Password"))
        self.pushReg.setText(_translate("LoginWindow", "Регистрация"))
        self.labelLogin.setText(_translate("LoginWindow", "Войти"))
