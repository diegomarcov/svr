# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'actualizacionVuelos.ui'
#
# Created: Thu Nov 04 17:39:12 2010
#      by: PyQt4 UI code generator 4.8
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ActualizarVuelo(object):
    def setupUi(self, ActualizarVuelo):
        ActualizarVuelo.setObjectName(_fromUtf8("ActualizarVuelo"))
        ActualizarVuelo.resize(500, 150)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ActualizarVuelo.sizePolicy().hasHeightForWidth())
        ActualizarVuelo.setSizePolicy(sizePolicy)
        ActualizarVuelo.setMinimumSize(QtCore.QSize(500, 150))
        ActualizarVuelo.setMaximumSize(QtCore.QSize(500, 150))
        self.buttonBox = QtGui.QDialogButtonBox(ActualizarVuelo)
        self.buttonBox.setGeometry(QtCore.QRect(0, 110, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.frame = QtGui.QFrame(ActualizarVuelo)
        self.frame.setGeometry(QtCore.QRect(10, 10, 482, 94))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.comboBoxDestino = QtGui.QComboBox(self.frame)
        self.comboBoxDestino.setObjectName(_fromUtf8("comboBoxDestino"))
        self.gridLayout_2.addWidget(self.comboBoxDestino, 0, 4, 1, 2)
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 5, 0, 1, 1)
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.lineEditNombreVuelo = QtGui.QLineEdit(self.frame)
        self.lineEditNombreVuelo.setObjectName(_fromUtf8("lineEditNombreVuelo"))
        self.gridLayout_2.addWidget(self.lineEditNombreVuelo, 5, 4, 1, 2)
        self.comboBoxOrigen = QtGui.QComboBox(self.frame)
        self.comboBoxOrigen.setObjectName(_fromUtf8("comboBoxOrigen"))
        self.gridLayout_2.addWidget(self.comboBoxOrigen, 2, 4, 1, 2)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.retranslateUi(ActualizarVuelo)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ActualizarVuelo.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ActualizarVuelo.reject)
        QtCore.QMetaObject.connectSlotsByName(ActualizarVuelo)

    def retranslateUi(self, ActualizarVuelo):
        ActualizarVuelo.setWindowTitle(QtGui.QApplication.translate("ActualizarVuelo", "Actualizar Vuelos", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ActualizarVuelo", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ActualizarVuelo", "Origen", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ActualizarVuelo", "Destino", None, QtGui.QApplication.UnicodeUTF8))

