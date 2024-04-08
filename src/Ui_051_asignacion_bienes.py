# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\rviqu\OneDrive - Universidad Internacional de las Américas (UIA)\UIA\2024\I\Programación II\Proyecto Final\tresPatitosUIA\src\051_asignacion_bienes.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Asignacion(object):
    def setupUi(self, Asignacion):
        Asignacion.setObjectName("Asignacion")
        Asignacion.setEnabled(True)
        Asignacion.resize(820, 820)
        Asignacion.setMinimumSize(QtCore.QSize(770, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/iconAsignar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Asignacion.setWindowIcon(icon)
        Asignacion.setStyleSheet("background-color: rgb(191, 191, 191);")
        self.formLayoutWidget = QtWidgets.QWidget(Asignacion)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 50, 191, 131))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lblCedula = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblCedula.setFont(font)
        self.lblCedula.setObjectName("lblCedula")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblCedula)
        self.lblNombre = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblNombre.setFont(font)
        self.lblNombre.setObjectName("lblNombre")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblNombre)
        self.txtNombre = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtNombre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtNombre.setObjectName("txtNombre")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtNombre)
        self.lblApellidos = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblApellidos.setFont(font)
        self.lblApellidos.setObjectName("lblApellidos")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblApellidos)
        self.txtApellidos = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtApellidos.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtApellidos.setObjectName("txtApellidos")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtApellidos)
        self.lblTelefono = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblTelefono.setFont(font)
        self.lblTelefono.setObjectName("lblTelefono")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblTelefono)
        self.txtTelefono = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtTelefono.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtTelefono.setObjectName("txtTelefono")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtTelefono)
        self.lblBienAsignado = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblBienAsignado.setFont(font)
        self.lblBienAsignado.setObjectName("lblBienAsignado")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lblBienAsignado)
        self.cbxCedulaEmpleados = QtWidgets.QComboBox(self.formLayoutWidget)
        self.cbxCedulaEmpleados.setObjectName("cbxCedulaEmpleados")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cbxCedulaEmpleados)
        self.cbxBienes = QtWidgets.QComboBox(self.formLayoutWidget)
        self.cbxBienes.setObjectName("cbxBienes")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.cbxBienes)
        self.label = QtWidgets.QLabel(Asignacion)
        self.label.setGeometry(QtCore.QRect(30, 20, 211, 16))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnGuardar = QtWidgets.QPushButton(Asignacion)
        self.btnGuardar.setGeometry(QtCore.QRect(60, 200, 51, 41))
        self.btnGuardar.setStyleSheet("QPushButton{\n"
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
        self.btnGuardar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/btnSave.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnGuardar.setIcon(icon1)
        self.btnGuardar.setIconSize(QtCore.QSize(27, 27))
        self.btnGuardar.setObjectName("btnGuardar")
        self.btnModificar = QtWidgets.QPushButton(Asignacion)
        self.btnModificar.setGeometry(QtCore.QRect(140, 200, 51, 41))
        self.btnModificar.setStyleSheet("QPushButton{\n"
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
        self.btnModificar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/btnEdit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnModificar.setIcon(icon2)
        self.btnModificar.setIconSize(QtCore.QSize(27, 27))
        self.btnModificar.setObjectName("btnModificar")
        self.btnEliminar = QtWidgets.QPushButton(Asignacion)
        self.btnEliminar.setGeometry(QtCore.QRect(220, 200, 51, 41))
        self.btnEliminar.setStyleSheet("QPushButton{\n"
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
        self.btnEliminar.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/btnDelete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEliminar.setIcon(icon3)
        self.btnEliminar.setIconSize(QtCore.QSize(27, 27))
        self.btnEliminar.setCheckable(True)
        self.btnEliminar.setChecked(False)
        self.btnEliminar.setAutoExclusive(False)
        self.btnEliminar.setObjectName("btnEliminar")
        self.btnCancelar = QtWidgets.QPushButton(Asignacion)
        self.btnCancelar.setGeometry(QtCore.QRect(300, 200, 51, 41))
        self.btnCancelar.setStyleSheet("QPushButton{\n"
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
        self.btnCancelar.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/btnClear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancelar.setIcon(icon4)
        self.btnCancelar.setIconSize(QtCore.QSize(27, 27))
        self.btnCancelar.setObjectName("btnCancelar")
        self.tblAsignados = QtWidgets.QTableWidget(Asignacion)
        self.tblAsignados.setGeometry(QtCore.QRect(50, 260, 361, 192))
        self.tblAsignados.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tblAsignados.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblAsignados.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblAsignados.setObjectName("tblAsignados")
        self.tblAsignados.setColumnCount(0)
        self.tblAsignados.setRowCount(0)

        self.retranslateUi(Asignacion)
        QtCore.QMetaObject.connectSlotsByName(Asignacion)

    def retranslateUi(self, Asignacion):
        _translate = QtCore.QCoreApplication.translate
        Asignacion.setWindowTitle(_translate("Asignacion", "Asignacion de bienes"))
        self.lblCedula.setText(_translate("Asignacion", "Cédula"))
        self.lblNombre.setText(_translate("Asignacion", "Nombre"))
        self.lblApellidos.setText(_translate("Asignacion", "Apellidos"))
        self.lblTelefono.setText(_translate("Asignacion", "Teléfono"))
        self.lblBienAsignado.setText(_translate("Asignacion", "Bien Asignado"))
        self.label.setText(_translate("Asignacion", "Asignación de Bienes"))
