# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui

from ui.actualizacionInstanciasVuelo import Ui_ActualizarSalidas

class ActualizarSalidasDialog(QtGui.QDialog):

    def setup(self):
        self.ui = Ui_ActualizarSalidas()
        self.ui.setupUi(self)
        self.ui.comboBoxEstado.addItems(['Demorado', 'Cancelado', 'En transito', 'Abordando', 'A tiempo'])
    
    def setData(self, vuelo_id, horaSalida, horaLlegada, estado):
        self.vuelo_id    = vuelo_id
        self.horaSalida  = horaSalida
        self.horaLlegada = horaLlegada
        self.estado      = estado
        self.ui.labelIDVuelo.setText(self.vuelo_id)
        self.ui.comboBoxEstado.setCurrentIndex(self.ui.comboBoxEstado.findText(estado))
        
        year    = horaSalida[0:4]
        month   = horaSalida[5:7]
        day     = horaSalida[8:10]
        hours   = horaSalida[11:13]
        minutes = horaSalida[14:16]
        seconds = horaSalida[17:19]
        horaSalidaDate = QtCore.QDate(int(year),  int(month),   int(day))
        horaSalidaTime = QtCore.QTime(int(hours), int(minutes), int(seconds))

        year    = horaLlegada[0:4]
        month   = horaLlegada[5:7]
        day     = horaLlegada[8:10]
        hours   = horaLlegada[11:13]
        minutes = horaLlegada[14:16]
        seconds = horaLlegada[17:19]
        horaLlegadaDate = QtCore.QDate(int(year),  int(month),   int(day))
        horaLlegadaTime = QtCore.QTime(int(hours), int(minutes), int(seconds))
        
        self.ui.dateTimeEditHoraSalida.setDate(horaSalidaDate)
        self.ui.dateTimeEditHoraSalida.setTime(horaSalidaTime)
        
        self.ui.dateTimeEditHoraLlegada.setDate(horaLlegadaDate)
        self.ui.dateTimeEditHoraLlegada.setTime(horaLlegadaTime)
    
    def __init__(self,parent = None):
        super(ActualizarSalidasDialog, self).__init__(parent)
        self.setup()
