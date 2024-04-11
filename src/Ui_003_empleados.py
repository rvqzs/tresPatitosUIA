# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\rviqu\OneDrive - Universidad Internacional de las Américas (UIA)\UIA\2024\I\Programación II\Proyecto Final\tresPatitosUIA\src\003_empleados.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Empleados(object):
    def setupUi(self, Empleados):
        Empleados.setObjectName("Empleados")
        Empleados.resize(860, 690)
        Empleados.setMinimumSize(QtCore.QSize(860, 690))
        Empleados.setMaximumSize(QtCore.QSize(16000, 16000))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/IconMenuEmpleados.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Empleados.setWindowIcon(icon)
        Empleados.setStyleSheet("background-color: rgb(191, 191, 191);")
        self.label_header = QtWidgets.QLabel(Empleados)
        self.label_header.setGeometry(QtCore.QRect(60, 10, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(5)
        self.label_header.setFont(font)
        self.label_header.setStyleSheet("font: 43 10pt \"Segoe UI Semibold\";\n"
"border:none;\n"
"background-color: rgba(0,0,0,0%);")
        self.label_header.setScaledContents(True)
        self.label_header.setObjectName("label_header")
        self.tblWidgetEmpleados = QtWidgets.QTableWidget(Empleados)
        self.tblWidgetEmpleados.setGeometry(QtCore.QRect(20, 340, 811, 311))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.tblWidgetEmpleados.sizePolicy().hasHeightForWidth())
        self.tblWidgetEmpleados.setSizePolicy(sizePolicy)
        self.tblWidgetEmpleados.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tblWidgetEmpleados.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblWidgetEmpleados.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblWidgetEmpleados.setWordWrap(False)
        self.tblWidgetEmpleados.setObjectName("tblWidgetEmpleados")
        self.tblWidgetEmpleados.setColumnCount(8)
        self.tblWidgetEmpleados.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblWidgetEmpleados.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblWidgetEmpleados.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblWidgetEmpleados.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblWidgetEmpleados.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblWidgetEmpleados.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblWidgetEmpleados.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblWidgetEmpleados.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblWidgetEmpleados.setHorizontalHeaderItem(7, item)
        self.label_headerIcon = QtWidgets.QLabel(Empleados)
        self.label_headerIcon.setGeometry(QtCore.QRect(20, 10, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_headerIcon.setFont(font)
        self.label_headerIcon.setStyleSheet("border:none;\n"
"background-color: rgba(0,0,0,0%);")
        self.label_headerIcon.setText("")
        self.label_headerIcon.setPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/iconEmpleadoHeader.png"))
        self.label_headerIcon.setScaledContents(True)
        self.label_headerIcon.setObjectName("label_headerIcon")
        self.frame = QtWidgets.QFrame(Empleados)
        self.frame.setGeometry(QtCore.QRect(20, 50, 671, 241))
        self.frame.setStyleSheet("border:4px solid;\n"
"border-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_usuario = QtWidgets.QLabel(self.frame)
        self.label_usuario.setGeometry(QtCore.QRect(60, 30, 47, 16))
        self.label_usuario.setStyleSheet("font: 63 10pt \"Segoe UI Semibold\";\n"
"border:none;")
        self.label_usuario.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_usuario.setObjectName("label_usuario")
        self.cmbBoxUsuarios = QtWidgets.QComboBox(self.frame)
        self.cmbBoxUsuarios.setGeometry(QtCore.QRect(120, 30, 100, 20))
        self.cmbBoxUsuarios.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:none;")
        self.cmbBoxUsuarios.setObjectName("cmbBoxUsuarios")
        self.lblCedula = QtWidgets.QLabel(self.frame)
        self.lblCedula.setGeometry(QtCore.QRect(280, 30, 41, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblCedula.sizePolicy().hasHeightForWidth())
        self.lblCedula.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.lblCedula.setFont(font)
        self.lblCedula.setStyleSheet("font: 63 10pt \"Segoe UI Semibold\";\n"
"border:none;")
        self.lblCedula.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblCedula.setObjectName("lblCedula")
        self.lblNombre = QtWidgets.QLabel(self.frame)
        self.lblNombre.setGeometry(QtCore.QRect(270, 70, 50, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblNombre.sizePolicy().hasHeightForWidth())
        self.lblNombre.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.lblNombre.setFont(font)
        self.lblNombre.setStyleSheet("font: 63 10pt \"Segoe UI Semibold\";\n"
"border:none;")
        self.lblNombre.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblNombre.setObjectName("lblNombre")
        self.txtCedula = QtWidgets.QLineEdit(self.frame)
        self.txtCedula.setGeometry(QtCore.QRect(330, 30, 100, 20))
        self.txtCedula.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtCedula.setObjectName("txtCedula")
        self.txtNombre = QtWidgets.QLineEdit(self.frame)
        self.txtNombre.setGeometry(QtCore.QRect(330, 70, 100, 20))
        self.txtNombre.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.txtNombre.setObjectName("txtNombre")
        self.label_phone = QtWidgets.QLabel(self.frame)
        self.label_phone.setGeometry(QtCore.QRect(270, 110, 51, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_phone.sizePolicy().hasHeightForWidth())
        self.label_phone.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_phone.setFont(font)
        self.label_phone.setStyleSheet("font: 63 10pt \"Segoe UI Semibold\";\n"
"border:none;")
        self.label_phone.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_phone.setObjectName("label_phone")
        self.txtTelefono = QtWidgets.QLineEdit(self.frame)
        self.txtTelefono.setGeometry(QtCore.QRect(330, 110, 100, 20))
        self.txtTelefono.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtTelefono.setObjectName("txtTelefono")
        self.lblDepartamento = QtWidgets.QLabel(self.frame)
        self.lblDepartamento.setGeometry(QtCore.QRect(20, 69, 90, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDepartamento.sizePolicy().hasHeightForWidth())
        self.lblDepartamento.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.lblDepartamento.setFont(font)
        self.lblDepartamento.setStyleSheet("font: 63 10pt \"Segoe UI Semibold\";\n"
"border:none;")
        self.lblDepartamento.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblDepartamento.setObjectName("lblDepartamento")
        self.lblIngreso = QtWidgets.QLabel(self.frame)
        self.lblIngreso.setGeometry(QtCore.QRect(60, 110, 50, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblIngreso.sizePolicy().hasHeightForWidth())
        self.lblIngreso.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.lblIngreso.setFont(font)
        self.lblIngreso.setStyleSheet("font: 63 10pt \"Segoe UI Semibold\";\n"
"border:none;")
        self.lblIngreso.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblIngreso.setObjectName("lblIngreso")
        self.txtDate = QtWidgets.QDateEdit(self.frame)
        self.txtDate.setGeometry(QtCore.QRect(120, 113, 121, 20))
        self.txtDate.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtDate.setWrapping(True)
        self.txtDate.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.txtDate.setDateTime(QtCore.QDateTime(QtCore.QDate(2024, 4, 8), QtCore.QTime(0, 0, 0)))
        self.txtDate.setMinimumDate(QtCore.QDate(2024, 4, 8))
        self.txtDate.setCurrentSection(QtWidgets.QDateTimeEdit.MonthSection)
        self.txtDate.setCalendarPopup(True)
        self.txtDate.setTimeSpec(QtCore.Qt.LocalTime)
        self.txtDate.setObjectName("txtDate")
        self.chckBoxIsSupervisor = QtWidgets.QCheckBox(self.frame)
        self.chckBoxIsSupervisor.setGeometry(QtCore.QRect(120, 190, 91, 17))
        self.chckBoxIsSupervisor.setStyleSheet("font: 63 10pt \"Segoe UI Semibold\";\n"
"border:none;")
        self.chckBoxIsSupervisor.setObjectName("chckBoxIsSupervisor")
        self.cmbBoxDepartamento = QtWidgets.QComboBox(self.frame)
        self.cmbBoxDepartamento.setGeometry(QtCore.QRect(120, 70, 121, 20))
        self.cmbBoxDepartamento.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:none;")
        self.cmbBoxDepartamento.setObjectName("cmbBoxDepartamento")
        self.lblDireccion = QtWidgets.QLabel(self.frame)
        self.lblDireccion.setGeometry(QtCore.QRect(50, 150, 60, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDireccion.sizePolicy().hasHeightForWidth())
        self.lblDireccion.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.lblDireccion.setFont(font)
        self.lblDireccion.setStyleSheet("font: 63 10pt \"Segoe UI Semibold\";\n"
"border:none;")
        self.lblDireccion.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblDireccion.setObjectName("lblDireccion")
        self.bttLimpiarEmpleado = QtWidgets.QPushButton(self.frame)
        self.bttLimpiarEmpleado.setGeometry(QtCore.QRect(480, 180, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.bttLimpiarEmpleado.setFont(font)
        self.bttLimpiarEmpleado.setStyleSheet("QPushButton{\n"
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/btnClear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bttLimpiarEmpleado.setIcon(icon1)
        self.bttLimpiarEmpleado.setIconSize(QtCore.QSize(20, 20))
        self.bttLimpiarEmpleado.setObjectName("bttLimpiarEmpleado")
        self.bttEliminarEmpleado = QtWidgets.QPushButton(self.frame)
        self.bttEliminarEmpleado.setGeometry(QtCore.QRect(480, 130, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.bttEliminarEmpleado.setFont(font)
        self.bttEliminarEmpleado.setStyleSheet("QPushButton{\n"
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
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/btnDelete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bttEliminarEmpleado.setIcon(icon2)
        self.bttEliminarEmpleado.setIconSize(QtCore.QSize(20, 20))
        self.bttEliminarEmpleado.setObjectName("bttEliminarEmpleado")
        self.bttCrearEmpleado = QtWidgets.QPushButton(self.frame)
        self.bttCrearEmpleado.setGeometry(QtCore.QRect(480, 30, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.bttCrearEmpleado.setFont(font)
        self.bttCrearEmpleado.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius:10px;\n"
"font: 63 10pt \"Segoe UI Semibold\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"border:2px solid #55C1FA;\n"
"border-radius:10px;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/btnCrear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bttCrearEmpleado.setIcon(icon3)
        self.bttCrearEmpleado.setIconSize(QtCore.QSize(25, 25))
        self.bttCrearEmpleado.setAutoDefault(False)
        self.bttCrearEmpleado.setObjectName("bttCrearEmpleado")
        self.bttModificarEmpleado = QtWidgets.QPushButton(self.frame)
        self.bttModificarEmpleado.setGeometry(QtCore.QRect(480, 80, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.bttModificarEmpleado.setFont(font)
        self.bttModificarEmpleado.setStyleSheet("QPushButton{\n"
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
        icon4.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/btnEdit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bttModificarEmpleado.setIcon(icon4)
        self.bttModificarEmpleado.setIconSize(QtCore.QSize(20, 20))
        self.bttModificarEmpleado.setObjectName("bttModificarEmpleado")
        self.txtDireccion = QtWidgets.QLineEdit(self.frame)
        self.txtDireccion.setGeometry(QtCore.QRect(120, 152, 311, 21))
        self.txtDireccion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtDireccion.setObjectName("txtDireccion")

        self.retranslateUi(Empleados)
        QtCore.QMetaObject.connectSlotsByName(Empleados)

    def retranslateUi(self, Empleados):
        _translate = QtCore.QCoreApplication.translate
        Empleados.setWindowTitle(_translate("Empleados", "Empleados"))
        self.label_header.setText(_translate("Empleados", "Administración de Empleados"))
        self.tblWidgetEmpleados.setSortingEnabled(True)
        item = self.tblWidgetEmpleados.horizontalHeaderItem(0)
        item.setText(_translate("Empleados", "Fecha Ingreso"))
        item = self.tblWidgetEmpleados.horizontalHeaderItem(1)
        item.setText(_translate("Empleados", "Usuario"))
        item = self.tblWidgetEmpleados.horizontalHeaderItem(2)
        item.setText(_translate("Empleados", "Cedula"))
        item = self.tblWidgetEmpleados.horizontalHeaderItem(3)
        item.setText(_translate("Empleados", "Nombre"))
        item = self.tblWidgetEmpleados.horizontalHeaderItem(4)
        item.setText(_translate("Empleados", "Departamento"))
        item = self.tblWidgetEmpleados.horizontalHeaderItem(5)
        item.setText(_translate("Empleados", "Telefono"))
        item = self.tblWidgetEmpleados.horizontalHeaderItem(6)
        item.setText(_translate("Empleados", "Direccion"))
        item = self.tblWidgetEmpleados.horizontalHeaderItem(7)
        item.setText(_translate("Empleados", "Puesto"))
        self.label_usuario.setText(_translate("Empleados", "Usuario"))
        self.lblCedula.setText(_translate("Empleados", "Cedula"))
        self.lblNombre.setText(_translate("Empleados", "Nombre"))
        self.label_phone.setText(_translate("Empleados", "Telefono"))
        self.lblDepartamento.setText(_translate("Empleados", "Departamento"))
        self.lblIngreso.setText(_translate("Empleados", "Ingreso"))
        self.txtDate.setDisplayFormat(_translate("Empleados", "MM/dd/yyyy"))
        self.chckBoxIsSupervisor.setText(_translate("Empleados", "Supervisor"))
        self.lblDireccion.setText(_translate("Empleados", "Direccion"))
        self.bttLimpiarEmpleado.setText(_translate("Empleados", "Limpiar"))
        self.bttEliminarEmpleado.setText(_translate("Empleados", "Eliminar"))
        self.bttCrearEmpleado.setText(_translate("Empleados", "Crear"))
        self.bttModificarEmpleado.setText(_translate("Empleados", "Modificar"))
