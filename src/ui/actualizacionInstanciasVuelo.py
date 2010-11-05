# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'actualizacionInstanciasVuelo.ui'
#
# Created: Fri Nov 05 14:53:40 2010
#      by: PyQt4 UI code generator 4.8
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ActualizarSalidas(object):
    def setupUi(self, ActualizarSalidas):
        ActualizarSalidas.setObjectName(_fromUtf8("ActualizarSalidas"))
        ActualizarSalidas.setWindowModality(QtCore.Qt.NonModal)
        ActualizarSalidas.resize(500, 150)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ActualizarSalidas.sizePolicy().hasHeightForWidth())
        ActualizarSalidas.setSizePolicy(sizePolicy)
        ActualizarSalidas.setMinimumSize(QtCore.QSize(500, 150))
        ActualizarSalidas.setMaximumSize(QtCore.QSize(500, 150))
        ActualizarSalidas.setSizeGripEnabled(False)
        ActualizarSalidas.setModal(False)
        self.gridLayout = QtGui.QGridLayout(ActualizarSalidas)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.labelIDVuelo = QtGui.QLabel(ActualizarSalidas)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelIDVuelo.sizePolicy().hasHeightForWidth())
        self.labelIDVuelo.setSizePolicy(sizePolicy)
        self.labelIDVuelo.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.labelIDVuelo.setObjectName(_fromUtf8("labelIDVuelo"))
        self.gridLayout.addWidget(self.labelIDVuelo, 0, 2, 1, 2)
        self.frame = QtGui.QFrame(ActualizarSalidas)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.dateTimeEditHoraSalida = QtGui.QDateTimeEdit(self.frame)
        self.dateTimeEditHoraSalida.setMinimumDate(QtCore.QDate(2010, 11, 1))
        self.dateTimeEditHoraSalida.setMinimumTime(QtCore.QTime(0, 0, 0))
        self.dateTimeEditHoraSalida.setCalendarPopup(True)
        self.dateTimeEditHoraSalida.setObjectName(_fromUtf8("dateTimeEditHoraSalida"))
        self.gridLayout_2.addWidget(self.dateTimeEditHoraSalida, 0, 1, 1, 1)
        self.dateTimeEditHoraLlegada = QtGui.QDateTimeEdit(self.frame)
        self.dateTimeEditHoraLlegada.setMinimumDate(QtCore.QDate(2010, 11, 1))
        self.dateTimeEditHoraLlegada.setCalendarPopup(True)
        self.dateTimeEditHoraLlegada.setObjectName(_fromUtf8("dateTimeEditHoraLlegada"))
        self.gridLayout_2.addWidget(self.dateTimeEditHoraLlegada, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 4)
        self.buttonBox = QtGui.QDialogButtonBox(ActualizarSalidas)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.label = QtGui.QLabel(ActualizarSalidas)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.retranslateUi(ActualizarSalidas)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ActualizarSalidas.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ActualizarSalidas.reject)
        QtCore.QMetaObject.connectSlotsByName(ActualizarSalidas)

    def retranslateUi(self, ActualizarSalidas):
        ActualizarSalidas.setWindowTitle(QtGui.QApplication.translate("ActualizarSalidas", "Actualizar Salidas", None, QtGui.QApplication.UnicodeUTF8))
        self.labelIDVuelo.setText(QtGui.QApplication.translate("ActualizarSalidas", "ID DEL VUELOOORR", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ActualizarSalidas", "Dia y Hora de Llegada", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ActualizarSalidas", "Dia y Hora de Salida", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ActualizarSalidas", "Vuelo ID", None, QtGui.QApplication.UnicodeUTF8))

