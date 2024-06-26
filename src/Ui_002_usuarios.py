# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\aaron\OneDrive\Documentos\Python\tresPatitosUIA\src\002_usuarios.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Usuarios(object):
    def setupUi(self, Usuarios):
        Usuarios.setObjectName("Usuarios")
        Usuarios.resize(576, 735)
        Usuarios.setMinimumSize(QtCore.QSize(575, 700))
        Usuarios.setMaximumSize(QtCore.QSize(600, 1000))
        Usuarios.setFocusPolicy(QtCore.Qt.StrongFocus)
        Usuarios.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\aaron\\OneDrive\\Documentos\\Python\\tresPatitosUIA\\src\\../res/iconMenuUsers.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Usuarios.setWindowIcon(icon)
        Usuarios.setAutoFillBackground(False)
        Usuarios.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.labelAdminUsers = QtWidgets.QLabel(Usuarios)
        self.labelAdminUsers.setEnabled(True)
        self.labelAdminUsers.setGeometry(QtCore.QRect(62, 12, 171, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelAdminUsers.sizePolicy().hasHeightForWidth())
        self.labelAdminUsers.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(5)
        self.labelAdminUsers.setFont(font)
        self.labelAdminUsers.setStyleSheet("font: 43 10pt \"Segoe UI Semibold\";\n"
"border:none;\n"
"background-color: rgba(0,0,0,0%);")
        self.labelAdminUsers.setTextFormat(QtCore.Qt.RichText)
        self.labelAdminUsers.setScaledContents(True)
        self.labelAdminUsers.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelAdminUsers.setObjectName("labelAdminUsers")
        self.tblUsuarios = QtWidgets.QTableWidget(Usuarios)
        self.tblUsuarios.setGeometry(QtCore.QRect(20, 330, 541, 321))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tblUsuarios.setFont(font)
        self.tblUsuarios.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tblUsuarios.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tblUsuarios.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tblUsuarios.setLineWidth(2)
        self.tblUsuarios.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tblUsuarios.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblUsuarios.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblUsuarios.setWordWrap(False)
        self.tblUsuarios.setObjectName("tblUsuarios")
        self.tblUsuarios.setColumnCount(4)
        self.tblUsuarios.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblUsuarios.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblUsuarios.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblUsuarios.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblUsuarios.setHorizontalHeaderItem(3, item)
        self.frame = QtWidgets.QFrame(Usuarios)
        self.frame.setGeometry(QtCore.QRect(20, 40, 541, 251))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setStyleSheet("border:4px solid;\n"
"border-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.labelUsuario = QtWidgets.QLabel(self.frame)
        self.labelUsuario.setGeometry(QtCore.QRect(100, 30, 50, 17))
        self.labelUsuario.setStyleSheet("font: 63 10pt \"Segoe UI Semibold\";\n"
"border:none;")
        self.labelUsuario.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelUsuario.setObjectName("labelUsuario")
        self.labelNombre = QtWidgets.QLabel(self.frame)
        self.labelNombre.setGeometry(QtCore.QRect(100, 70, 50, 17))
        self.labelNombre.setStyleSheet("font: 63 10pt \"Segoe UI Semibold\";\n"
"border:none;")
        self.labelNombre.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelNombre.setObjectName("labelNombre")
        self.labelPassword = QtWidgets.QLabel(self.frame)
        self.labelPassword.setGeometry(QtCore.QRect(80, 110, 69, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.labelPassword.setFont(font)
        self.labelPassword.setStyleSheet("font: 63 10pt \"Segoe UI Semibold\";\n"
"border:none;")
        self.labelPassword.setTextFormat(QtCore.Qt.RichText)
        self.labelPassword.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelPassword.setObjectName("labelPassword")
        self.labelPassword_2 = QtWidgets.QLabel(self.frame)
        self.labelPassword_2.setGeometry(QtCore.QRect(10, 150, 141, 27))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.labelPassword_2.setFont(font)
        self.labelPassword_2.setStyleSheet("font: 63 10pt \"Segoe UI Semibold\";\n"
"border:none;")
        self.labelPassword_2.setTextFormat(QtCore.Qt.RichText)
        self.labelPassword_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelPassword_2.setObjectName("labelPassword_2")
        self.txtConfirmPassword = QtWidgets.QLineEdit(self.frame)
        self.txtConfirmPassword.setEnabled(True)
        self.txtConfirmPassword.setGeometry(QtCore.QRect(160, 154, 140, 20))
        self.txtConfirmPassword.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtConfirmPassword.setText("")
        self.txtConfirmPassword.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.txtConfirmPassword.setObjectName("txtConfirmPassword")
        self.txtName = QtWidgets.QLineEdit(self.frame)
        self.txtName.setEnabled(True)
        self.txtName.setGeometry(QtCore.QRect(160, 70, 140, 20))
        self.txtName.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtName.setText("")
        self.txtName.setObjectName("txtName")
        self.txtPassword = QtWidgets.QLineEdit(self.frame)
        self.txtPassword.setEnabled(True)
        self.txtPassword.setGeometry(QtCore.QRect(160, 110, 140, 20))
        self.txtPassword.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtPassword.setText("")
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.txtPassword.setObjectName("txtPassword")
        self.txtUsername = QtWidgets.QLineEdit(self.frame)
        self.txtUsername.setEnabled(True)
        self.txtUsername.setGeometry(QtCore.QRect(160, 30, 140, 20))
        self.txtUsername.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtUsername.setText("")
        self.txtUsername.setObjectName("txtUsername")
        self.chkBoxAdmin = QtWidgets.QCheckBox(self.frame)
        self.chkBoxAdmin.setEnabled(True)
        self.chkBoxAdmin.setGeometry(QtCore.QRect(310, 24, 91, 31))
        self.chkBoxAdmin.setStyleSheet("font: 63 10pt \"Segoe UI Semibold\";\n"
"border:none;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\aaron\\OneDrive\\Documentos\\Python\\tresPatitosUIA\\src\\../res/iconadminUser.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.chkBoxAdmin.setIcon(icon1)
        self.chkBoxAdmin.setIconSize(QtCore.QSize(18, 18))
        self.chkBoxAdmin.setChecked(False)
        self.chkBoxAdmin.setObjectName("chkBoxAdmin")
        self.labelUser = QtWidgets.QLabel(self.frame)
        self.labelUser.setGeometry(QtCore.QRect(10, 20, 81, 81))
        self.labelUser.setStyleSheet("border:none;\n"
"\n"
"")
        self.labelUser.setText("")
        self.labelUser.setPixmap(QtGui.QPixmap("c:\\Users\\aaron\\OneDrive\\Documentos\\Python\\tresPatitosUIA\\src\\../res/iconLoginUsername.png"))
        self.labelUser.setScaledContents(True)
        self.labelUser.setAlignment(QtCore.Qt.AlignCenter)
        self.labelUser.setObjectName("labelUser")
        self.btnLimpiar = QtWidgets.QPushButton(self.frame)
        self.btnLimpiar.setGeometry(QtCore.QRect(430, 150, 90, 30))
        self.btnLimpiar.setMaximumSize(QtCore.QSize(90, 30))
        self.btnLimpiar.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius:10px;\n"
"font: 63 10pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"border:2px solid #55C1FA;\n"
"border-radius:10px;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\aaron\\OneDrive\\Documentos\\Python\\tresPatitosUIA\\src\\../res/btnClear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLimpiar.setIcon(icon2)
        self.btnLimpiar.setIconSize(QtCore.QSize(18, 18))
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.btnModificarUsuario = QtWidgets.QPushButton(self.frame)
        self.btnModificarUsuario.setGeometry(QtCore.QRect(430, 70, 90, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnModificarUsuario.sizePolicy().hasHeightForWidth())
        self.btnModificarUsuario.setSizePolicy(sizePolicy)
        self.btnModificarUsuario.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius:10px;\n"
"font: 63 10pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"border:2px solid #55C1FA;\n"
"border-radius:10px;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("c:\\Users\\aaron\\OneDrive\\Documentos\\Python\\tresPatitosUIA\\src\\../res/btnEdit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnModificarUsuario.setIcon(icon3)
        self.btnModificarUsuario.setIconSize(QtCore.QSize(18, 18))
        self.btnModificarUsuario.setObjectName("btnModificarUsuario")
        self.btnCrearUsuario = QtWidgets.QPushButton(self.frame)
        self.btnCrearUsuario.setGeometry(QtCore.QRect(430, 30, 90, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCrearUsuario.sizePolicy().hasHeightForWidth())
        self.btnCrearUsuario.setSizePolicy(sizePolicy)
        self.btnCrearUsuario.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius:10px;\n"
"font: 63 10pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"border:2px solid #55C1FA;\n"
"border-radius:10px;\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("c:\\Users\\aaron\\OneDrive\\Documentos\\Python\\tresPatitosUIA\\src\\../res/btnCrear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCrearUsuario.setIcon(icon4)
        self.btnCrearUsuario.setIconSize(QtCore.QSize(25, 25))
        self.btnCrearUsuario.setObjectName("btnCrearUsuario")
        self.btnEliminarUsuario = QtWidgets.QPushButton(self.frame)
        self.btnEliminarUsuario.setGeometry(QtCore.QRect(430, 110, 90, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnEliminarUsuario.sizePolicy().hasHeightForWidth())
        self.btnEliminarUsuario.setSizePolicy(sizePolicy)
        self.btnEliminarUsuario.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius:10px;\n"
"font: 63 10pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"border:2px solid #55C1FA;\n"
"border-radius:10px;\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("c:\\Users\\aaron\\OneDrive\\Documentos\\Python\\tresPatitosUIA\\src\\../res/btnDelete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEliminarUsuario.setIcon(icon5)
        self.btnEliminarUsuario.setIconSize(QtCore.QSize(20, 20))
        self.btnEliminarUsuario.setObjectName("btnEliminarUsuario")
        self.isPassowordVisible = QtWidgets.QRadioButton(self.frame)
        self.isPassowordVisible.setGeometry(QtCore.QRect(160, 183, 91, 21))
        self.isPassowordVisible.setStyleSheet("font: 63 10pt \"Segoe UI Semibold\";\n"
"border:none;")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("c:\\Users\\aaron\\OneDrive\\Documentos\\Python\\tresPatitosUIA\\src\\../res/icons8-visible-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.isPassowordVisible.setIcon(icon6)
        self.isPassowordVisible.setObjectName("isPassowordVisible")
        self.labelHeader = QtWidgets.QLabel(Usuarios)
        self.labelHeader.setGeometry(QtCore.QRect(30, 10, 21, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelHeader.sizePolicy().hasHeightForWidth())
        self.labelHeader.setSizePolicy(sizePolicy)
        self.labelHeader.setStyleSheet("border:none;\n"
"background-color: rgba(0,0,0,0%);\n"
"")
        self.labelHeader.setText("")
        self.labelHeader.setPixmap(QtGui.QPixmap("c:\\Users\\aaron\\OneDrive\\Documentos\\Python\\tresPatitosUIA\\src\\../res/iconAddUser.png"))
        self.labelHeader.setScaledContents(True)
        self.labelHeader.setAlignment(QtCore.Qt.AlignCenter)
        self.labelHeader.setObjectName("labelHeader")

        self.retranslateUi(Usuarios)
        QtCore.QMetaObject.connectSlotsByName(Usuarios)

    def retranslateUi(self, Usuarios):
        _translate = QtCore.QCoreApplication.translate
        Usuarios.setWindowTitle(_translate("Usuarios", "Creacion de Usuarios"))
        self.labelAdminUsers.setText(_translate("Usuarios", "Administración de Usuarios"))
        self.tblUsuarios.setSortingEnabled(True)
        item = self.tblUsuarios.horizontalHeaderItem(0)
        item.setText(_translate("Usuarios", "Username"))
        item = self.tblUsuarios.horizontalHeaderItem(1)
        item.setText(_translate("Usuarios", "Nombre"))
        item = self.tblUsuarios.horizontalHeaderItem(2)
        item.setText(_translate("Usuarios", "Contraseña"))
        item = self.tblUsuarios.horizontalHeaderItem(3)
        item.setText(_translate("Usuarios", "Privilegios"))
        self.labelUsuario.setText(_translate("Usuarios", "Usuario "))
        self.labelNombre.setText(_translate("Usuarios", "Nombre"))
        self.labelPassword.setText(_translate("Usuarios", "Contraseña"))
        self.labelPassword_2.setText(_translate("Usuarios", "Confirmar Contraseña"))
        self.chkBoxAdmin.setText(_translate("Usuarios", "Admin"))
        self.btnLimpiar.setToolTip(_translate("Usuarios", "CTRL+R"))
        self.btnLimpiar.setText(_translate("Usuarios", "Limpiar"))
        self.btnLimpiar.setShortcut(_translate("Usuarios", "Ctrl+R"))
        self.btnModificarUsuario.setToolTip(_translate("Usuarios", "CNTRL+E"))
        self.btnModificarUsuario.setText(_translate("Usuarios", "Modificar"))
        self.btnModificarUsuario.setShortcut(_translate("Usuarios", "Ctrl+E"))
        self.btnCrearUsuario.setToolTip(_translate("Usuarios", "CNTRL+S"))
        self.btnCrearUsuario.setText(_translate("Usuarios", "Crear"))
        self.btnCrearUsuario.setShortcut(_translate("Usuarios", "Ctrl+S"))
        self.btnEliminarUsuario.setToolTip(_translate("Usuarios", "CNTRL+DEL"))
        self.btnEliminarUsuario.setText(_translate("Usuarios", "Eliminar"))
        self.btnEliminarUsuario.setShortcut(_translate("Usuarios", "Ctrl+Del"))
        self.isPassowordVisible.setText(_translate("Usuarios", "Mostrar"))
