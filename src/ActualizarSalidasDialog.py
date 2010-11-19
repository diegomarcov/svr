# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui

from ui.actualizacionInstanciasVuelo import Ui_ActualizarSalidas

class ActualizarSalidasDialog(QtGui.QDialog):

    def setup(self):
        self.ui = Ui_ActualizarSalidas()
        self.ui.setupUi(self)
        self.ui.comboBoxEstado.addItems(['Demorado', 'Cancelado', 'En tránsito', 'Abordando', 'A tiempo'])
    
    def setData(self, vuelo_id, horaSalida, horaLlegada, estado):
        self.vuelo_id = vuelo_id
        self.horaSalida = horaSalida
        self.horaLlegada = horaLlegada

        self.ui.labelIDVuelo.setText(self.vuelo_id)        
        self.ui.comboBoxEstado.setCurrentIndex(self.ui.comboBoxEstado.findText(estado))
        # falta setear los horarios de salida y llegada...
        # usar las funciones setDate y setTime del QDateTimeEdit!
    
    def __init__(self,parent = None):
        super(ActualizarSalidasDialog, self).__init__(parent)
        self.setup()