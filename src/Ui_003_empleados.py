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
        Empleados.resize(850, 690)
        Empleados.setMinimumSize(QtCore.QSize(850, 690))
        Empleados.setMaximumSize(QtCore.QSize(16000, 16000))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/IconMenuEmpleados.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Empleados.setWindowIcon(icon)
        Empleados.setStyleSheet("background-color: rgb(191, 191, 191);")
        self.label = QtWidgets.QLabel(Empleados)
        self.label.setGeometry(QtCore.QRect(30, 20, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lblCedula = QtWidgets.QLabel(Empleados)
        self.lblCedula.setGeometry(QtCore.QRect(30, 80, 50, 20))
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
        self.lblCedula.setStyleSheet("font: 63 10pt \"Segoe UI Semibold\";")
        self.lblCedula.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblCedula.setObjectName("lblCedula")
        self.lblNombre = QtWidgets.QLabel(Empleados)
        self.lblNombre.setGeometry(QtCore.QRect(30, 119, 50, 20))
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
        self.lblNombre.setStyleSheet("font: 63 10pt \"Segoe UI Semibold\";")
        self.lblNombre.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblNombre.setObjectName("lblNombre")
        self.lblApellidos = QtWidgets.QLabel(Empleados)
        self.lblApellidos.setGeometry(QtCore.QRect(20, 160, 60, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblApellidos.sizePolicy().hasHeightForWidth())
        self.lblApellidos.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.lblApellidos.setFont(font)
        self.lblApellidos.setStyleSheet("font: 63 10pt \"Segoe UI Semibold\";")
        self.lblApellidos.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblApellidos.setObjectName("lblApellidos")
        self.lblDireccion = QtWidgets.QLabel(Empleados)
        self.lblDireccion.setGeometry(QtCore.QRect(30, 230, 60, 20))
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
        self.lblDireccion.setStyleSheet("font: 63 10pt \"Segoe UI Semibold\";")
        self.lblDireccion.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblDireccion.setObjectName("lblDireccion")
        self.lblDepartamento = QtWidgets.QLabel(Empleados)
        self.lblDepartamento.setGeometry(QtCore.QRect(230, 80, 90, 20))
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
        self.lblDepartamento.setStyleSheet("font: 63 10pt \"Segoe UI Semibold\";")
        self.lblDepartamento.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblDepartamento.setObjectName("lblDepartamento")
        self.lblIngreso = QtWidgets.QLabel(Empleados)
        self.lblIngreso.setGeometry(QtCore.QRect(270, 120, 50, 20))
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
        self.lblIngreso.setStyleSheet("font: 63 10pt \"Segoe UI Semibold\";")
        self.lblIngreso.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblIngreso.setObjectName("lblIngreso")
        self.lblJefatura = QtWidgets.QLabel(Empleados)
        self.lblJefatura.setGeometry(QtCore.QRect(270, 160, 50, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblJefatura.sizePolicy().hasHeightForWidth())
        self.lblJefatura.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.lblJefatura.setFont(font)
        self.lblJefatura.setStyleSheet("font: 63 10pt \"Segoe UI Semibold\";")
        self.lblJefatura.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblJefatura.setObjectName("lblJefatura")
        self.txtCedula = QtWidgets.QLineEdit(Empleados)
        self.txtCedula.setGeometry(QtCore.QRect(90, 80, 113, 20))
        self.txtCedula.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtCedula.setObjectName("txtCedula")
        self.txtNombre = QtWidgets.QLineEdit(Empleados)
        self.txtNombre.setGeometry(QtCore.QRect(90, 120, 113, 20))
        self.txtNombre.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.txtNombre.setObjectName("txtNombre")
        self.txtApellidos = QtWidgets.QLineEdit(Empleados)
        self.txtApellidos.setGeometry(QtCore.QRect(90, 160, 113, 20))
        self.txtApellidos.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtApellidos.setObjectName("txtApellidos")
        self.txtDireccion = QtWidgets.QLineEdit(Empleados)
        self.txtDireccion.setGeometry(QtCore.QRect(40, 260, 321, 61))
        self.txtDireccion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtDireccion.setObjectName("txtDireccion")
        self.txtDepartamento = QtWidgets.QLineEdit(Empleados)
        self.txtDepartamento.setGeometry(QtCore.QRect(330, 82, 110, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtDepartamento.sizePolicy().hasHeightForWidth())
        self.txtDepartamento.setSizePolicy(sizePolicy)
        self.txtDepartamento.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtDepartamento.setObjectName("txtDepartamento")
        self.txtIngreso = QtWidgets.QLineEdit(Empleados)
        self.txtIngreso.setGeometry(QtCore.QRect(330, 120, 110, 20))
        self.txtIngreso.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtIngreso.setObjectName("txtIngreso")
        self.bttCrearEmpleado = QtWidgets.QPushButton(Empleados)
        self.bttCrearEmpleado.setGeometry(QtCore.QRect(490, 80, 100, 30))
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/btnCrear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bttCrearEmpleado.setIcon(icon1)
        self.bttCrearEmpleado.setIconSize(QtCore.QSize(25, 25))
        self.bttCrearEmpleado.setObjectName("bttCrearEmpleado")
        self.label_3 = QtWidgets.QLabel(Empleados)
        self.label_3.setGeometry(QtCore.QRect(20, 198, 60, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 63 10pt \"Segoe UI Semibold\";")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.txtTelefono = QtWidgets.QLineEdit(Empleados)
        self.txtTelefono.setGeometry(QtCore.QRect(90, 200, 113, 20))
        self.txtTelefono.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtTelefono.setObjectName("txtTelefono")
        self.tblWidgetEmpleados = QtWidgets.QTableWidget(Empleados)
        self.tblWidgetEmpleados.setGeometry(QtCore.QRect(20, 360, 811, 301))
        self.tblWidgetEmpleados.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tblWidgetEmpleados.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblWidgetEmpleados.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
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
        self.bttModificarEmpleado = QtWidgets.QPushButton(Empleados)
        self.bttModificarEmpleado.setGeometry(QtCore.QRect(490, 120, 100, 30))
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/btnEdit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bttModificarEmpleado.setIcon(icon2)
        self.bttModificarEmpleado.setIconSize(QtCore.QSize(20, 20))
        self.bttModificarEmpleado.setObjectName("bttModificarEmpleado")
        self.bttEliminarEmpleado = QtWidgets.QPushButton(Empleados)
        self.bttEliminarEmpleado.setGeometry(QtCore.QRect(490, 160, 100, 30))
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/btnDelete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bttEliminarEmpleado.setIcon(icon3)
        self.bttEliminarEmpleado.setIconSize(QtCore.QSize(20, 20))
        self.bttEliminarEmpleado.setObjectName("bttEliminarEmpleado")
        self.bttLimpiarEmpleado = QtWidgets.QPushButton(Empleados)
        self.bttLimpiarEmpleado.setGeometry(QtCore.QRect(490, 200, 100, 30))
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/btnClear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bttLimpiarEmpleado.setIcon(icon4)
        self.bttLimpiarEmpleado.setIconSize(QtCore.QSize(20, 20))
        self.bttLimpiarEmpleado.setObjectName("bttLimpiarEmpleado")
        self.cmbJefatura = QtWidgets.QComboBox(Empleados)
        self.cmbJefatura.setGeometry(QtCore.QRect(330, 160, 110, 20))
        self.cmbJefatura.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cmbJefatura.setObjectName("cmbJefatura")
        self.cmbJefatura.addItem("")
        self.cmbJefatura.addItem("")

        self.retranslateUi(Empleados)
        QtCore.QMetaObject.connectSlotsByName(Empleados)

    def retranslateUi(self, Empleados):
        _translate = QtCore.QCoreApplication.translate
        Empleados.setWindowTitle(_translate("Empleados", "Empleados"))
        self.label.setText(_translate("Empleados", "Crear Empleados"))
        self.lblCedula.setText(_translate("Empleados", "Cedula"))
        self.lblNombre.setText(_translate("Empleados", "Nombre"))
        self.lblApellidos.setText(_translate("Empleados", "Apellidos"))
        self.lblDireccion.setText(_translate("Empleados", "Direccion"))
        self.lblDepartamento.setText(_translate("Empleados", "Departamento"))
        self.lblIngreso.setText(_translate("Empleados", "Ingreso"))
        self.lblJefatura.setText(_translate("Empleados", "Jefatura"))
        self.bttCrearEmpleado.setText(_translate("Empleados", "Crear"))
        self.label_3.setText(_translate("Empleados", "Telefono"))
        item = self.tblWidgetEmpleados.horizontalHeaderItem(0)
        item.setText(_translate("Empleados", "Cedula"))
        item = self.tblWidgetEmpleados.horizontalHeaderItem(1)
        item.setText(_translate("Empleados", "Nombre"))
        item = self.tblWidgetEmpleados.horizontalHeaderItem(2)
        item.setText(_translate("Empleados", "Apellidos"))
        item = self.tblWidgetEmpleados.horizontalHeaderItem(3)
        item.setText(_translate("Empleados", "Telefono"))
        item = self.tblWidgetEmpleados.horizontalHeaderItem(4)
        item.setText(_translate("Empleados", "Direccion"))
        item = self.tblWidgetEmpleados.horizontalHeaderItem(5)
        item.setText(_translate("Empleados", "Departamento"))
        item = self.tblWidgetEmpleados.horizontalHeaderItem(6)
        item.setText(_translate("Empleados", "Ingreso"))
        item = self.tblWidgetEmpleados.horizontalHeaderItem(7)
        item.setText(_translate("Empleados", "Jefatura"))
        self.bttModificarEmpleado.setText(_translate("Empleados", "Modificar"))
        self.bttEliminarEmpleado.setText(_translate("Empleados", "Eliminar"))
        self.bttLimpiarEmpleado.setText(_translate("Empleados", "Limpiar"))
        self.cmbJefatura.setItemText(0, _translate("Empleados", "Si"))
        self.cmbJefatura.setItemText(1, _translate("Empleados", "No"))
