# -*- coding: utf-8 -*-
from PyQt4                              import QtCore, QtGui
from ui.actualizacionInstanciasVuelo    import Ui_ActualizarSalidas
from connection.error                   import Error
from models.salidas                     import Salidas


class ActualizarSalidasDialog(QtGui.QDialog):

    #--------------------------------------------------------------------------#
    def __init__(self, parent = None, conn = None):
        super(ActualizarSalidasDialog, self).__init__(parent)
        self.conn = conn
        self.setup()

    #--------------------------------------------------------------------------#
    def setup(self):
        self.ui = Ui_ActualizarSalidas()
        self.ui.setupUi(self)
        self.ui.comboBoxEstado.addItems(['Demorado', 'Cancelado', 'En transito', 'Abordando', 'A tiempo'])
        self.connect(self.ui.buttonBox, QtCore.SIGNAL('accepted()'), self.modificarSalida)

    #--------------------------------------------------------------------------#
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

    #--------------------------------------------------------------------------#
    def modificarSalida(self):
        vuelo         = self.vuelo_id
        diahora_sale1 = self.horaSalida
        diahora_sale2 = self.ui.dateTimeEditHoraSalida.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        diahora_llega = self.ui.dateTimeEditHoraLlegada.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        estado        = self.ui.comboBoxEstado.currentText()
        salidas       = Salidas(self.conn)
        try:
            salidas.update(vuelo, diahora_sale1, diahora_sale2, diahora_llega, estado)
        except Error:
            qmb = QtGui.QMessageBox().critical(self, "Error", "No se pudo actualizar la salida.", QtGui.QMessageBox.Ok)
