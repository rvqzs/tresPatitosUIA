# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\rviqu\OneDrive - Universidad Internacional de las Américas (UIA)\UIA\2024\I\Programación II\Proyecto Final\tresPatitosUIA\src\000_mdi.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mdiWindow(object):
    def setupUi(self, mdiWindow):
        mdiWindow.setObjectName("mdiWindow")
        mdiWindow.resize(1158, 674)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mdiWindow.sizePolicy().hasHeightForWidth())
        mdiWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/iconMDI.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mdiWindow.setWindowIcon(icon)
        mdiWindow.setIconSize(QtCore.QSize(34, 34))
        mdiWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(mdiWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setEnabled(True)
        self.mdiArea.setGeometry(QtCore.QRect(0, 0, 1161, 611))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mdiArea.sizePolicy().hasHeightForWidth())
        self.mdiArea.setSizePolicy(sizePolicy)
        self.mdiArea.setMouseTracking(False)
        self.mdiArea.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.mdiArea.setAcceptDrops(True)
        self.mdiArea.setAutoFillBackground(False)
        self.mdiArea.setStyleSheet("background-color: rgb(71, 145, 140);")
        self.mdiArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mdiArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.mdiArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.mdiArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        brush = QtGui.QBrush(QtGui.QColor(191, 191, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.mdiArea.setBackground(brush)
        self.mdiArea.setViewMode(QtWidgets.QMdiArea.SubWindowView)
        self.mdiArea.setObjectName("mdiArea")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(950, 520, 91, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/iconMDI.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(850, 520, 91, 71))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/iconMDI.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1050, 520, 91, 71))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/iconMDI.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        mdiWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mdiWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1158, 22))
        self.menubar.setStyleSheet("background-color:rgb(85, 193, 250);")
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        self.menuMain = QtWidgets.QMenu(self.menubar)
        self.menuMain.setFocusPolicy(QtCore.Qt.TabFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/iconMenu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuMain.setIcon(icon1)
        self.menuMain.setObjectName("menuMain")
        self.menuBienes = QtWidgets.QMenu(self.menuMain)
        self.menuBienes.setGeometry(QtCore.QRect(796, 218, 170, 137))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.menuBienes.setFont(font)
        self.menuBienes.setFocusPolicy(QtCore.Qt.TabFocus)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/icons8-assets-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuBienes.setIcon(icon2)
        self.menuBienes.setObjectName("menuBienes")
        self.menuReportes = QtWidgets.QMenu(self.menuMain)
        self.menuReportes.setObjectName("menuReportes")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setTearOffEnabled(False)
        self.menuHelp.setTitle("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/iconHelp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuHelp.setIcon(icon3)
        self.menuHelp.setObjectName("menuHelp")
        mdiWindow.setMenuBar(self.menubar)
        self.mniUsuarios = QtWidgets.QAction(mdiWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/iconMenuUsers.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mniUsuarios.setIcon(icon4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mniUsuarios.setFont(font)
        self.mniUsuarios.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.mniUsuarios.setObjectName("mniUsuarios")
        self.mniEmpleados = QtWidgets.QAction(mdiWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/IconMenuEmpleados.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mniEmpleados.setIcon(icon5)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mniEmpleados.setFont(font)
        self.mniEmpleados.setObjectName("mniEmpleados")
        self.mniDepartamentos = QtWidgets.QAction(mdiWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/iconMenuDepartamentos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mniDepartamentos.setIcon(icon6)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mniDepartamentos.setFont(font)
        self.mniDepartamentos.setObjectName("mniDepartamentos")
        self.mniAsignar = QtWidgets.QAction(mdiWindow)
        self.mniAsignar.setObjectName("mniAsignar")
        self.mniDesligar = QtWidgets.QAction(mdiWindow)
        self.mniDesligar.setObjectName("mniDesligar")
        self.btn_logout = QtWidgets.QAction(mdiWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/iconLogout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_logout.setIcon(icon7)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_logout.setFont(font)
        self.btn_logout.setObjectName("btn_logout")
        self.mniRegistrarBienes = QtWidgets.QAction(mdiWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/iconMenuRegistrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mniRegistrarBienes.setIcon(icon8)
        self.mniRegistrarBienes.setObjectName("mniRegistrarBienes")
        self.mnuAsignar = QtWidgets.QAction(mdiWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/iconAsignar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mnuAsignar.setIcon(icon9)
        self.mnuAsignar.setObjectName("mnuAsignar")
        self.mnuDesligar = QtWidgets.QAction(mdiWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/iconDesligar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mnuDesligar.setIcon(icon10)
        self.mnuDesligar.setObjectName("mnuDesligar")
        self.submnuBienesAsignados = QtWidgets.QAction(mdiWindow)
        self.submnuBienesAsignados.setObjectName("submnuBienesAsignados")
        self.submnuBienes_no_Asignados = QtWidgets.QAction(mdiWindow)
        self.submnuBienes_no_Asignados.setObjectName("submnuBienes_no_Asignados")
        self.menuBienes.addAction(self.mniRegistrarBienes)
        self.menuBienes.addAction(self.mnuAsignar)
        self.menuBienes.addAction(self.mnuDesligar)
        self.menuReportes.addAction(self.submnuBienesAsignados)
        self.menuReportes.addAction(self.submnuBienes_no_Asignados)
        self.menuMain.addSeparator()
        self.menuMain.addAction(self.mniUsuarios)
        self.menuMain.addAction(self.mniEmpleados)
        self.menuMain.addAction(self.mniDepartamentos)
        self.menuMain.addAction(self.menuBienes.menuAction())
        self.menuMain.addAction(self.menuReportes.menuAction())
        self.menuMain.addSeparator()
        self.menuMain.addAction(self.btn_logout)
        self.menuMain.addSeparator()
        self.menubar.addAction(self.menuMain.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(mdiWindow)
        QtCore.QMetaObject.connectSlotsByName(mdiWindow)

    def retranslateUi(self, mdiWindow):
        _translate = QtCore.QCoreApplication.translate
        mdiWindow.setWindowTitle(_translate("mdiWindow", "Tres Patitos S.A"))
        self.menuMain.setTitle(_translate("mdiWindow", "Login"))
        self.menuBienes.setTitle(_translate("mdiWindow", "Bienes"))
        self.menuReportes.setTitle(_translate("mdiWindow", "Reportes"))
        self.mniUsuarios.setText(_translate("mdiWindow", "Usuarios"))
        self.mniEmpleados.setText(_translate("mdiWindow", "Empleados"))
        self.mniDepartamentos.setText(_translate("mdiWindow", "Departamentos"))
        self.mniAsignar.setText(_translate("mdiWindow", "Asignar"))
        self.mniDesligar.setText(_translate("mdiWindow", "Desligar"))
        self.btn_logout.setText(_translate("mdiWindow", "Log out"))
        self.mniRegistrarBienes.setText(_translate("mdiWindow", "Registrar"))
        self.mnuAsignar.setText(_translate("mdiWindow", "Asignar"))
        self.mnuDesligar.setText(_translate("mdiWindow", "Desligar"))
        self.submnuBienesAsignados.setText(_translate("mdiWindow", "Bienes Asignados"))
        self.submnuBienes_no_Asignados.setText(_translate("mdiWindow", "Bienes no Asignados"))
