# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\rviqu\OneDrive - Universidad Internacional de las Américas (UIA)\UIA\2024\I\Programación II\Proyecto Final\desligar.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Desligar_Bienes(object):
    def setupUi(self, Desligar_Bienes):
        Desligar_Bienes.setObjectName("Desligar_Bienes")
        Desligar_Bienes.resize(500, 355)
        self.label = QtWidgets.QLabel(Desligar_Bienes)
        self.label.setGeometry(QtCore.QRect(190, 20, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Desligar_Bienes)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(Desligar_Bienes)
        self.comboBox.setGeometry(QtCore.QRect(10, 120, 171, 21))
        self.comboBox.setEditable(False)
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.tableView = QtWidgets.QTableView(Desligar_Bienes)
        self.tableView.setGeometry(QtCore.QRect(230, 120, 256, 192))
        self.tableView.setObjectName("tableView")
        self.pushButton = QtWidgets.QPushButton(Desligar_Bienes)
        self.pushButton.setGeometry(QtCore.QRect(10, 170, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Desligar_Bienes)
        self.comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Desligar_Bienes)

    def retranslateUi(self, Desligar_Bienes):
        _translate = QtCore.QCoreApplication.translate
        Desligar_Bienes.setWindowTitle(_translate("Desligar_Bienes", "Desligar Bienes"))
        self.label.setText(_translate("Desligar_Bienes", "Desligar Bienes"))
        self.label_2.setText(_translate("Desligar_Bienes", "Seleccione el empelado:"))
        self.comboBox.setPlaceholderText(_translate("Desligar_Bienes", "Seleccione"))
        self.comboBox.setItemText(0, _translate("Desligar_Bienes", "Luis"))
        self.comboBox.setItemText(1, _translate("Desligar_Bienes", "Maria"))
        self.comboBox.setItemText(2, _translate("Desligar_Bienes", "Luisa"))
        self.comboBox.setItemText(3, _translate("Desligar_Bienes", "Carlos"))
        self.pushButton.setText(_translate("Desligar_Bienes", "Desligar"))
