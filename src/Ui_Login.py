# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\rviqu\OneDrive - Universidad Internacional de las Américas (UIA)\UIA\2024\I\Programación II\Proyecto Final\tresPatitosUIA\src\Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(422, 600)
        Login.setMinimumSize(QtCore.QSize(400, 600))
        Login.setMaximumSize(QtCore.QSize(16777215, 600))
        Login.setAutoFillBackground(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(Login)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Login)
        self.widget.setObjectName("widget")
        self.lbl_logIn = QtWidgets.QLabel(self.widget)
        self.lbl_logIn.setGeometry(QtCore.QRect(140, 50, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_logIn.setFont(font)
        self.lbl_logIn.setObjectName("lbl_logIn")
        self.btn_login = QtWidgets.QPushButton(self.widget)
        self.btn_login.setGeometry(QtCore.QRect(130, 520, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_login.setFont(font)
        self.btn_login.setObjectName("btn_login")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 120, 341, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setSpacing(25)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.txt_user = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.txt_user.setBaseSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.txt_user.setFont(font)
        self.txt_user.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.txt_user.setAutoFillBackground(False)
        self.txt_user.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.txt_user.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.txt_user.setLineWidth(5)
        self.txt_user.setMidLineWidth(-1)
        self.txt_user.setTabChangesFocus(True)
        self.txt_user.setReadOnly(False)
        self.txt_user.setObjectName("txt_user")
        self.verticalLayout_2.addWidget(self.txt_user)
        self.txt_password = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.txt_password.setBaseSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.txt_password.setFont(font)
        self.txt_password.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.txt_password.setAutoFillBackground(False)
        self.txt_password.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.txt_password.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.txt_password.setLineWidth(5)
        self.txt_password.setMidLineWidth(-1)
        self.txt_password.setTabChangesFocus(True)
        self.txt_password.setReadOnly(False)
        self.txt_password.setObjectName("txt_password")
        self.verticalLayout_2.addWidget(self.txt_password)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Log In"))
        self.lbl_logIn.setWhatsThis(_translate("Login", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Log In</span></p></body></html>"))
        self.lbl_logIn.setText(_translate("Login", "Log In"))
        self.btn_login.setText(_translate("Login", "Log In"))
        self.txt_user.setPlaceholderText(_translate("Login", "Usuario"))
        self.txt_password.setPlaceholderText(_translate("Login", "Contraseña"))
