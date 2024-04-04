# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\rviqu\OneDrive - Universidad Internacional de las Américas (UIA)\UIA\2024\I\Programación II\Proyecto Final\tresPatitosUIA\src\001_login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(400, 400)
        Login.setMinimumSize(QtCore.QSize(400, 400))
        Login.setMaximumSize(QtCore.QSize(400, 600))
        Login.setAutoFillBackground(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(Login)
        self.verticalLayout.setObjectName("verticalLayout")
        self.login_widget = QtWidgets.QWidget(Login)
        self.login_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.login_widget.setStyleSheet("background-color: rgb(191, 191, 191);")
        self.login_widget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStatesMinorOutlyingIslands))
        self.login_widget.setObjectName("login_widget")
        self.lbl_logIn = QtWidgets.QLabel(self.login_widget)
        self.lbl_logIn.setGeometry(QtCore.QRect(150, 40, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_logIn.setFont(font)
        self.lbl_logIn.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Zimbabwe))
        self.lbl_logIn.setText("")
        self.lbl_logIn.setPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/profile.png"))
        self.lbl_logIn.setScaledContents(True)
        self.lbl_logIn.setObjectName("lbl_logIn")
        self.btn_login = QtWidgets.QPushButton(self.login_widget)
        self.btn_login.setGeometry(QtCore.QRect(140, 260, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_login.setFont(font)
        self.btn_login.setStyleSheet("QPushButton{\n"
"\n"
"background-color:rgb(182, 217, 255);\n"
"border:none;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"border:3px solid #566eff;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/btnLogin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_login.setIcon(icon)
        self.btn_login.setIconSize(QtCore.QSize(15, 15))
        self.btn_login.setObjectName("btn_login")
        self.txt_password = QtWidgets.QLineEdit(self.login_widget)
        self.txt_password.setGeometry(QtCore.QRect(100, 210, 180, 20))
        self.txt_password.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid #566eff;\n"
"border-radius:10px;")
        self.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_password.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_password.setClearButtonEnabled(False)
        self.txt_password.setObjectName("txt_password")
        self.txt_username = QtWidgets.QLineEdit(self.login_widget)
        self.txt_username.setGeometry(QtCore.QRect(100, 140, 180, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_username.sizePolicy().hasHeightForWidth())
        self.txt_username.setSizePolicy(sizePolicy)
        self.txt_username.setMinimumSize(QtCore.QSize(20, 5))
        self.txt_username.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid #566eff;\n"
"border-radius:10px;")
        self.txt_username.setText("")
        self.txt_username.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_username.setObjectName("txt_username")
        self.label = QtWidgets.QLabel(self.login_widget)
        self.label.setGeometry(QtCore.QRect(70, 210, 21, 21))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0,0%);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/password2.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.login_widget)
        self.label_2.setGeometry(QtCore.QRect(70, 140, 21, 21))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/user2.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.login_widget)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Log In"))
        self.lbl_logIn.setWhatsThis(_translate("Login", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Log In</span></p></body></html>"))
        self.btn_login.setText(_translate("Login", " Log in"))
        self.txt_password.setPlaceholderText(_translate("Login", "Password"))
        self.txt_username.setPlaceholderText(_translate("Login", "Username"))
