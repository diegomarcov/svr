# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'actualizacionReserva.ui'
#
# Created: Fri Nov 05 04:59:11 2010
#      by: PyQt4 UI code generator 4.7.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ActualizarReserva(object):
    def setupUi(self, ActualizarReserva):
        ActualizarReserva.setObjectName(_fromUtf8("ActualizarReserva"))
        ActualizarReserva.resize(500, 250)
        ActualizarReserva.setMaximumSize(QtCore.QSize(500, 250))
        self.gridLayout = QtGui.QGridLayout(ActualizarReserva)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(ActualizarReserva)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.formLayout_2 = QtGui.QFormLayout(self.frame)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_7 = QtGui.QLabel(self.frame)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_7)
        self.lineEditNombreCliente_2 = QtGui.QLineEdit(self.frame)
        self.lineEditNombreCliente_2.setObjectName(_fromUtf8("lineEditNombreCliente_2"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditNombreCliente_2)
        self.label_8 = QtGui.QLabel(self.frame)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_8)
        self.lineEditDNI_2 = QtGui.QLineEdit(self.frame)
        self.lineEditDNI_2.setObjectName(_fromUtf8("lineEditDNI_2"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditDNI_2)
        self.label_9 = QtGui.QLabel(self.frame)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_9)
        self.lineEditPasaporte_2 = QtGui.QLineEdit(self.frame)
        self.lineEditPasaporte_2.setObjectName(_fromUtf8("lineEditPasaporte_2"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEditPasaporte_2)
        self.label_10 = QtGui.QLabel(self.frame)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_10)
        self.spinBoxPrecio_2 = QtGui.QDoubleSpinBox(self.frame)
        self.spinBoxPrecio_2.setMaximum(10000.99)
        self.spinBoxPrecio_2.setProperty(_fromUtf8("value"), 250.0)
        self.spinBoxPrecio_2.setObjectName(_fromUtf8("spinBoxPrecio_2"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.spinBoxPrecio_2)
        self.label_11 = QtGui.QLabel(self.frame)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_11)
        self.comboBoxPago_2 = QtGui.QComboBox(self.frame)
        self.comboBoxPago_2.setObjectName(_fromUtf8("comboBoxPago_2"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.comboBoxPago_2)
        self.label_12 = QtGui.QLabel(self.frame)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_12)
        self.comboBoxEstado_2 = QtGui.QComboBox(self.frame)
        self.comboBoxEstado_2.setObjectName(_fromUtf8("comboBoxEstado_2"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.comboBoxEstado_2)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 3)
        self.buttonBox = QtGui.QDialogButtonBox(ActualizarReserva)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)

        self.retranslateUi(ActualizarReserva)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ActualizarReserva.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ActualizarReserva.reject)
        QtCore.QMetaObject.connectSlotsByName(ActualizarReserva)

    def retranslateUi(self, ActualizarReserva):
        ActualizarReserva.setWindowTitle(QtGui.QApplication.translate("ActualizarReserva", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ActualizarReserva", "Nombre del cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("ActualizarReserva", "DNI", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("ActualizarReserva", "Pasaporte", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("ActualizarReserva", "Precio", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("ActualizarReserva", "Forma de pago", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("ActualizarReserva", "Estado", None, QtGui.QApplication.UnicodeUTF8))

