# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Thu Nov 04 17:32:09 2010
#      by: PyQt4 UI code generator 4.8
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(686, 483)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnVuelos = QtGui.QPushButton(self.groupBox)
        self.btnVuelos.setObjectName(_fromUtf8("btnVuelos"))
        self.horizontalLayout.addWidget(self.btnVuelos)
        self.btnInstanciasVuelos = QtGui.QPushButton(self.groupBox)
        self.btnInstanciasVuelos.setObjectName(_fromUtf8("btnInstanciasVuelos"))
        self.horizontalLayout.addWidget(self.btnInstanciasVuelos)
        self.verticalLayout.addWidget(self.groupBox)
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.gridLayout = QtGui.QGridLayout(self.page)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tablaVuelos = QtGui.QTableView(self.page)
        self.tablaVuelos.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tablaVuelos.setObjectName(_fromUtf8("tablaVuelos"))
        self.gridLayout.addWidget(self.tablaVuelos, 0, 1, 1, 2)
        self.calendarioVuelos = QtGui.QCalendarWidget(self.page)
        self.calendarioVuelos.setMaximumSize(QtCore.QSize(250, 200))
        self.calendarioVuelos.setObjectName(_fromUtf8("calendarioVuelos"))
        self.gridLayout.addWidget(self.calendarioVuelos, 0, 0, 1, 1)
        self.frame = QtGui.QFrame(self.page)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btnAgregarInstVuelos = QtGui.QPushButton(self.frame)
        self.btnAgregarInstVuelos.setObjectName(_fromUtf8("btnAgregarInstVuelos"))
        self.horizontalLayout_2.addWidget(self.btnAgregarInstVuelos)
        self.btnModificarInstVuelos = QtGui.QPushButton(self.frame)
        self.btnModificarInstVuelos.setObjectName(_fromUtf8("btnModificarInstVuelos"))
        self.horizontalLayout_2.addWidget(self.btnModificarInstVuelos)
        self.btnEliminarInstVuelos = QtGui.QPushButton(self.frame)
        self.btnEliminarInstVuelos.setObjectName(_fromUtf8("btnEliminarInstVuelos"))
        self.horizontalLayout_2.addWidget(self.btnEliminarInstVuelos)
        self.gridLayout.addWidget(self.frame, 2, 0, 1, 3)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.page_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tableView = QtGui.QTableView(self.page_2)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.gridLayout_2.addWidget(self.tableView, 0, 0, 1, 3)
        self.frame_2 = QtGui.QFrame(self.page_2)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.btnAgregarVuelo = QtGui.QPushButton(self.frame_2)
        self.btnAgregarVuelo.setObjectName(_fromUtf8("btnAgregarVuelo"))
        self.horizontalLayout_3.addWidget(self.btnAgregarVuelo)
        self.btnModificarVuelo = QtGui.QPushButton(self.frame_2)
        self.btnModificarVuelo.setObjectName(_fromUtf8("btnModificarVuelo"))
        self.horizontalLayout_3.addWidget(self.btnModificarVuelo)
        self.btnEliminarVuelo = QtGui.QPushButton(self.frame_2)
        self.btnEliminarVuelo.setObjectName(_fromUtf8("btnEliminarVuelo"))
        self.horizontalLayout_3.addWidget(self.btnEliminarVuelo)
        self.gridLayout_2.addWidget(self.frame_2, 1, 0, 1, 3)
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 686, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMen = QtGui.QMenu(self.menubar)
        self.menuMen.setObjectName(_fromUtf8("menuMen"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionDesloguearse = QtGui.QAction(MainWindow)
        self.actionDesloguearse.setObjectName(_fromUtf8("actionDesloguearse"))
        self.actionAcerca_de = QtGui.QAction(MainWindow)
        self.actionAcerca_de.setObjectName(_fromUtf8("actionAcerca_de"))
        self.menuMen.addAction(self.actionDesloguearse)
        self.menuMen.addSeparator()
        self.menuMen.addAction(self.actionAcerca_de)
        self.menubar.addAction(self.menuMen.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "svr - Sistema de Vuelos y Reservas", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Administración", None, QtGui.QApplication.UnicodeUTF8))
        self.btnVuelos.setText(QtGui.QApplication.translate("MainWindow", "Vuelos", None, QtGui.QApplication.UnicodeUTF8))
        self.btnInstanciasVuelos.setText(QtGui.QApplication.translate("MainWindow", "Instancias de vuelos", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAgregarInstVuelos.setText(QtGui.QApplication.translate("MainWindow", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnModificarInstVuelos.setText(QtGui.QApplication.translate("MainWindow", "Modificar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnEliminarInstVuelos.setText(QtGui.QApplication.translate("MainWindow", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAgregarVuelo.setText(QtGui.QApplication.translate("MainWindow", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnModificarVuelo.setText(QtGui.QApplication.translate("MainWindow", "Modificar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnEliminarVuelo.setText(QtGui.QApplication.translate("MainWindow", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMen.setTitle(QtGui.QApplication.translate("MainWindow", "Menú", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDesloguearse.setText(QtGui.QApplication.translate("MainWindow", "Log out", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAcerca_de.setText(QtGui.QApplication.translate("MainWindow", "Acerca de...", None, QtGui.QApplication.UnicodeUTF8))
