# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'agregarInstanciasVuelo.ui'
#
# Created: Sat Nov 13 15:20:44 2010
#      by: PyQt4 UI code generator 4.7.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AgregarSalidas(object):
    def setupUi(self, AgregarSalidas):
        AgregarSalidas.setObjectName(_fromUtf8("AgregarSalidas"))
        AgregarSalidas.setWindowModality(QtCore.Qt.NonModal)
        AgregarSalidas.resize(500, 150)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AgregarSalidas.sizePolicy().hasHeightForWidth())
        AgregarSalidas.setSizePolicy(sizePolicy)
        AgregarSalidas.setMinimumSize(QtCore.QSize(500, 150))
        AgregarSalidas.setMaximumSize(QtCore.QSize(500, 150))
        AgregarSalidas.setSizeGripEnabled(False)
        AgregarSalidas.setModal(False)
        self.gridLayout = QtGui.QGridLayout(AgregarSalidas)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(AgregarSalidas)
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
        self.dateTimeEditHoraSalida.setMinimumDate(QtCore.QDate(2010, 1, 1))
        self.dateTimeEditHoraSalida.setMinimumTime(QtCore.QTime(0, 0, 0))
        self.dateTimeEditHoraSalida.setCalendarPopup(False)
        self.dateTimeEditHoraSalida.setObjectName(_fromUtf8("dateTimeEditHoraSalida"))
        self.gridLayout_2.addWidget(self.dateTimeEditHoraSalida, 0, 1, 1, 1)
        self.dateTimeEditHoraLlegada = QtGui.QDateTimeEdit(self.frame)
        self.dateTimeEditHoraLlegada.setMinimumDate(QtCore.QDate(2010, 11, 1))
        self.dateTimeEditHoraLlegada.setCalendarPopup(False)
        self.dateTimeEditHoraLlegada.setObjectName(_fromUtf8("dateTimeEditHoraLlegada"))
        self.gridLayout_2.addWidget(self.dateTimeEditHoraLlegada, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 4)
        self.buttonBox = QtGui.QDialogButtonBox(AgregarSalidas)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.label = QtGui.QLabel(AgregarSalidas)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.comboBox = QtGui.QComboBox(AgregarSalidas)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout.addWidget(self.comboBox, 0, 2, 1, 2)

        self.retranslateUi(AgregarSalidas)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AgregarSalidas.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AgregarSalidas.reject)
        QtCore.QMetaObject.connectSlotsByName(AgregarSalidas)

    def retranslateUi(self, AgregarSalidas):
        AgregarSalidas.setWindowTitle(QtGui.QApplication.translate("AgregarSalidas", "Agregar Salidas", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AgregarSalidas", "Dia y Hora de Llegada", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AgregarSalidas", "Dia y Hora de Salida", None, QtGui.QApplication.UnicodeUTF8))
        self.dateTimeEditHoraSalida.setDisplayFormat(QtGui.QApplication.translate("AgregarSalidas", "dd/MM/yyyy h:mm AP", None, QtGui.QApplication.UnicodeUTF8))
        self.dateTimeEditHoraLlegada.setDisplayFormat(QtGui.QApplication.translate("AgregarSalidas", "dd/MM/yyyy h:mm AP", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AgregarSalidas", "Vuelo ID", None, QtGui.QApplication.UnicodeUTF8))

