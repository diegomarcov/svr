from PyQt4 import QtCore, QtGui

from ui.actualizacionVuelos import Ui_ActualizarVuelo
from models.aeropuertos     import Aeropuertos
from models.vuelos          import Vuelos

class ActualizarVuelosDialog(QtGui.QDialog):

    def setup(self, conn):
        self.ui = Ui_ActualizarVuelo()
        self.ui.setupUi(self)
        aeropuertos = Aeropuertos(self.conn)
        # listaAeropuertos = aeropuertos.loadAll()
        # listaStrAeropuertos = QtCore.QStringList()
        # print "-------------------------- Lista de aeropuertos! --------------------------\n"
        # print listaAeropuertos
        # for aeropuerto in listaAeropuertos:
            # current = aeropuerto.get(0) + aeropuerto.get(1) + aeropuerto.get(2) + aeropuerto.get(3)
            # print current
            # listaStrAeropuertos = listaStrAeropuertos << current
            
        # self.ui.comboBoxOrigen.addItems(listaStrAeropuertos)
        # self.ui.comboBoxDestino.addItems(listaStrAeropuertos)
        aeropuertos.loadAll()
        
        print "-------------------------- Lista de aeropuertos! --------------------------\n"
        print aeropuertos.model
        self.ui.comboBoxOrigen.setModel(aeropuertos.model)
        self.ui.comboBoxDestino.setModel(aeropuertos.model)
        
        self.connect(self.ui.buttonBox, QtCore.SIGNAL('accepted()'), self.modificarVuelo)
    
    def __init__(self, parent = None, conn = None, current_name = None):
        super(ActualizarVuelosDialog, self).__init__(parent)
        self.conn = conn
        self.setup(self.conn)
        
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
        vuelos.update(self.vuelo_id, nombre, aeropuerto_origen, aeropuerto_destino)


