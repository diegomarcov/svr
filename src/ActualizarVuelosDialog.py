# -*- coding: utf-8 -*-
from PyQt4                  import QtCore, QtGui
from ui.actualizacionVuelos import Ui_ActualizarVuelo
from connection.error       import Error
from models.aeropuertos     import Aeropuertos
from models.vuelos          import Vuelos

class ActualizarVuelosDialog(QtGui.QDialog):

    #--------------------------------------------------------------------------#
    def __init__(self, parent = None, conn = None, current_name = None):
        super(ActualizarVuelosDialog, self).__init__(parent)
        self.conn = conn
        self.setup(self.conn)

    #--------------------------------------------------------------------------#
    def setup(self, conn):
        aeropuertos = Aeropuertos(self.conn)
        aeropuertos.loadAll()
        self.ui = Ui_ActualizarVuelo()
        self.ui.setupUi(self)
        self.ui.comboBoxOrigen.setModel(aeropuertos.model)
        self.ui.comboBoxDestino.setModel(aeropuertos.model)
        self.connect(self.ui.buttonBox, QtCore.SIGNAL('accepted()'), self.modificarVuelo)

    #--------------------------------------------------------------------------#
    def setData(self, vuelo_id, origen, destino):
        self.vuelo_id = vuelo_id
        self.origen   = origen
        self.destino  = destino
        self.ui.lineEditNombreVuelo.setText(self.vuelo_id)
        origen_index = self.ui.comboBoxOrigen.findText(self.origen)
        self.ui.comboBoxOrigen.setCurrentIndex(origen_index)
        destino_index = self.ui.comboBoxDestino.findText(destino)
        self.ui.comboBoxDestino.setCurrentIndex(destino_index)

    #--------------------------------------------------------------------------#
    def modificarVuelo(self):
        # recuperar los datos y modificar el vuelo 
        aeropuerto_origen   = self.ui.comboBoxOrigen.currentText()
        aeropuerto_destino  = self.ui.comboBoxDestino.currentText()
        nombre              = self.ui.lineEditNombreVuelo.text()
        vuelos              = Vuelos(self.conn)
        try:
            vuelos.update(self.vuelo_id, nombre, aeropuerto_origen, aeropuerto_destino)
        except Error:
            qmb = QtGui.QMessageBox().critical(self, "Error", "Hay salidas asociadas a este vuelo.", QtGui.QMessageBox.Ok)
