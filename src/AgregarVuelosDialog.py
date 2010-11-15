from PyQt4 import QtCore, QtGui

from ui.actualizacionVuelos import Ui_ActualizarVuelo
from models.aeropuertos     import Aeropuertos
from models.vuelos          import Vuelos

class AgregarVuelosDialog(QtGui.QDialog):

    def setup(self, conn):
        self.ui = Ui_ActualizarVuelo()
        self.ui.setupUi(self)
        aeropuertos = Aeropuertos(self.conn)
        aeropuertos.loadAll()
        
        print "-------------------------- Lista de aeropuertos! --------------------------\n"
        print aeropuertos.model
        self.ui.comboBoxOrigen.setModel(aeropuertos.model)
        self.ui.comboBoxDestino.setModel(aeropuertos.model)
        
        self.connect(self.ui.buttonBox, QtCore.SIGNAL('accepted()'), self.agregarVuelo)
    
    def __init__(self, parent = None, conn = None):
        super(AgregarVuelosDialog, self).__init__(parent)
        self.conn = conn
        self.setup(self.conn)

    #--------------------------------------------------------------------------#
    def agregarVuelo(self):
        # recuperar los datos y modificar el vuelo 
        aeropuerto_origen   = self.ui.comboBoxOrigen.currentText()
        aeropuerto_destino  = self.ui.comboBoxDestino.currentText()
        nombre              = self.ui.lineEditNombreVuelo.text()
        vuelos              = Vuelos(self.conn)
        if aeropuerto_destino != aeropuerto_origen:
            vuelos.insert(nombre, aeropuerto_origen, aeropuerto_destino)
            print "Nueva ruta de vuelo agregada!"
        else:
            QtGui.QMessageBox.critical(self, u"Error al agregar vuelo", u"Los aeropuertos de origen y destino deben ser diferentes!")