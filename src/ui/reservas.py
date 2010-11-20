# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reservas.ui'
#
# Created: Sat Nov 20 13:45:35 2010
#      by: PyQt4 UI code generator 4.7.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_VentanaReservas(object):
    def setupUi(self, VentanaReservas):
        VentanaReservas.setObjectName(_fromUtf8("VentanaReservas"))
        VentanaReservas.resize(800, 520)
        VentanaReservas.setMinimumSize(QtCore.QSize(800, 520))
        VentanaReservas.setMaximumSize(QtCore.QSize(800, 520))
        self.verticalLayout = QtGui.QVBoxLayout(VentanaReservas)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelIDVuelo = QtGui.QLabel(VentanaReservas)
        self.labelIDVuelo.setObjectName(_fromUtf8("labelIDVuelo"))
        self.verticalLayout.addWidget(self.labelIDVuelo)
        self.tablaReservas = QtGui.QTableView(VentanaReservas)
        self.tablaReservas.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tablaReservas.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tablaReservas.setObjectName(_fromUtf8("tablaReservas"))
        self.verticalLayout.addWidget(self.tablaReservas)
        self.frame = QtGui.QFrame(VentanaReservas)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnAgregarReserva = QtGui.QPushButton(self.frame)
        self.btnAgregarReserva.setObjectName(_fromUtf8("btnAgregarReserva"))
        self.horizontalLayout.addWidget(self.btnAgregarReserva)
        self.btnModificarReserva = QtGui.QPushButton(self.frame)
        self.btnModificarReserva.setObjectName(_fromUtf8("btnModificarReserva"))
        self.horizontalLayout.addWidget(self.btnModificarReserva)
        self.btnEliminarReserva = QtGui.QPushButton(self.frame)
        self.btnEliminarReserva.setObjectName(_fromUtf8("btnEliminarReserva"))
        self.horizontalLayout.addWidget(self.btnEliminarReserva)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(VentanaReservas)
        QtCore.QMetaObject.connectSlotsByName(VentanaReservas)

    def retranslateUi(self, VentanaReservas):
        VentanaReservas.setWindowTitle(QtGui.QApplication.translate("VentanaReservas", "Reservas", None, QtGui.QApplication.UnicodeUTF8))
        self.labelIDVuelo.setText(QtGui.QApplication.translate("VentanaReservas", "Reservas para el vuelo", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAgregarReserva.setText(QtGui.QApplication.translate("VentanaReservas", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnModificarReserva.setText(QtGui.QApplication.translate("VentanaReservas", "Modificar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnEliminarReserva.setText(QtGui.QApplication.translate("VentanaReservas", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))

