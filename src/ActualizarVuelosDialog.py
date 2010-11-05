from PyQt4 import QtCore, QtGui

from ui.actualizacionVuelos import Ui_ActualizarVuelo
from models.aeropuertos import Aeropuertos

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
        
    
    def __init__(self, parent = None, conn = None):
        super(ActualizarVuelosDialog, self).__init__(parent)
        self.conn = conn
        self.setup(self.conn)
        