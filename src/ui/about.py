# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created: Tue Nov 23 21:01:13 2010
#      by: PyQt4 UI code generator 4.7.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName(_fromUtf8("About"))
        About.resize(440, 289)
        self.gridLayout = QtGui.QGridLayout(About)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(About)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.buttonBox = QtGui.QDialogButtonBox(About)
        self.buttonBox.setMaximumSize(QtCore.QSize(75, 16777215))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)

        self.retranslateUi(About)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), About.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), About.reject)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        About.setWindowTitle(QtGui.QApplication.translate("About", "Acerca de svr", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("About", "svr - Sistema de Vuelos y Reservas\n"
"\n"
"Administracion y Gestion de Proyectos de Software\n"
"\n"
"Segundo cuatrimestre 2010 - Comisión 5\n"
"\n"
"\n"
"Integrantes:\n"
"\n"
"Garay, Iñaki - LU 67.380\n"
"Marcovecchio, Diego - LU 83.815\n"
"Molas, Leonardo - LU xx.xxx\n"
"Montenegro, Emiliano - LU 83.864", None, QtGui.QApplication.UnicodeUTF8))

