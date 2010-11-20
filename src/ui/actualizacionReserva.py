# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'actualizacionReserva.ui'
#
# Created: Sat Nov 20 16:27:23 2010
#      by: PyQt4 UI code generator 4.7.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_actualizarReserva(object):
    def setupUi(self, actualizarReserva):
        actualizarReserva.setObjectName(_fromUtf8("actualizarReserva"))
        actualizarReserva.resize(500, 250)
        actualizarReserva.setMaximumSize(QtCore.QSize(500, 250))
        self.gridLayout = QtGui.QGridLayout(actualizarReserva)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(actualizarReserva)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.frame = QtGui.QFrame(actualizarReserva)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.formLayout_2 = QtGui.QFormLayout(self.frame)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_7 = QtGui.QLabel(self.frame)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_7)
        self.lineEditNombreCliente = QtGui.QLineEdit(self.frame)
        self.lineEditNombreCliente.setObjectName(_fromUtf8("lineEditNombreCliente"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditNombreCliente)
        self.label_8 = QtGui.QLabel(self.frame)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_8)
        self.lineEditDNI = QtGui.QLineEdit(self.frame)
        self.lineEditDNI.setObjectName(_fromUtf8("lineEditDNI"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditDNI)
        self.label_9 = QtGui.QLabel(self.frame)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_9)
        self.lineEditPasaporte = QtGui.QLineEdit(self.frame)
        self.lineEditPasaporte.setObjectName(_fromUtf8("lineEditPasaporte"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEditPasaporte)
        self.label_10 = QtGui.QLabel(self.frame)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_10)
        self.spinBoxPrecio = QtGui.QDoubleSpinBox(self.frame)
        self.spinBoxPrecio.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.spinBoxPrecio.setMaximum(10000.99)
        self.spinBoxPrecio.setProperty(_fromUtf8("value"), 250.0)
        self.spinBoxPrecio.setObjectName(_fromUtf8("spinBoxPrecio"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.spinBoxPrecio)
        self.label_11 = QtGui.QLabel(self.frame)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_11)
        self.comboBoxPago = QtGui.QComboBox(self.frame)
        self.comboBoxPago.setObjectName(_fromUtf8("comboBoxPago"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.comboBoxPago)
        self.label_12 = QtGui.QLabel(self.frame)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_12)
        self.comboBoxEstado = QtGui.QComboBox(self.frame)
        self.comboBoxEstado.setObjectName(_fromUtf8("comboBoxEstado"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.comboBoxEstado)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 3)

        self.retranslateUi(actualizarReserva)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), actualizarReserva.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), actualizarReserva.reject)
        QtCore.QMetaObject.connectSlotsByName(actualizarReserva)

    def retranslateUi(self, actualizarReserva):
        actualizarReserva.setWindowTitle(QtGui.QApplication.translate("actualizarReserva", "Agregar Reserva", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("actualizarReserva", "Nombre del cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("actualizarReserva", "DNI", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("actualizarReserva", "Pasaporte", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("actualizarReserva", "Precio", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("actualizarReserva", "Forma de pago", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("actualizarReserva", "Estado", None, QtGui.QApplication.UnicodeUTF8))

