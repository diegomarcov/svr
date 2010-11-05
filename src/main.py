import sys

from connection.connection import Connection

from PyQt4 import QtCore, QtGui
from ui.mainWindow import Ui_MainWindow
from ActualizarSalidasDialog import ActualizarSalidasDialog
from ActualizarVuelosDialog import ActualizarVuelosDialog
from models.vuelos import Vuelos
from models.salidas import Salidas

class Principal (QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        self.conn = Connection("svr")
        self.conn.open()
        print "-------------------------- Conexion OK! --------------------------\n"
        #creacion de la ventana principal
        self.ventana = Ui_MainWindow()
        self.ventana.setupUi(self)
        
        #cargar vuelos en la tabla principal
        todosLosVuelos = Vuelos(self.conn)
        todosLosVuelos.loadAll()
        self.ventana.tablaVuelos.setModel(todosLosVuelos.model)
        
        #cargar salidas en la tabla principal
        todasLasSalidas = Salidas(self.conn)
        todasLasSalidas.loadAll()
        self.ventana.tablaSalidas.setModel(todasLasSalidas.model)
        
        #creacion de la ventana para actualizacion de los vuelos
        self.ventanaActualizacionVuelos = ActualizarVuelosDialog(parent = self, conn = self.conn)
        
        #creacion del dialog ventana para la actualizacion de las salidas
        self.ventanaActualizacionSalida = ActualizarSalidasDialog()
       
       #signals de los botones de la interface del sistema
        self.connect(self.ventana.btnVuelos, QtCore.SIGNAL('clicked()'), self.mostrarTabVuelos)
        self.connect(self.ventana.btnInstanciasVuelos, QtCore.SIGNAL('clicked()'), self.mostrarTabInstVuelos)
        self.connect(self.ventana.btnAgregarInstVuelos, QtCore.SIGNAL('clicked()'), self.mostrarActualizacionInstanciasVuelos)
        self.connect(self.ventana.btnModificarInstVuelos, QtCore.SIGNAL('clicked()'), self.mostrarActualizacionInstanciasVuelos)
        self.connect(self.ventana.btnModificarVuelo, QtCore.SIGNAL('clicked()'), self.mostrarActualizacionVuelos)
        self.connect(self.ventana.btnAgregarVuelo, QtCore.SIGNAL('clicked()'), self.mostrarActualizacionVuelos)
        
    def mostrarTabVuelos(self):
        self.ventana.stackedWidget.setCurrentIndex(1)
    
    def mostrarTabInstVuelos(self):
        self.ventana.stackedWidget.setCurrentIndex(0)

    def mostrarActualizacionInstanciasVuelos(self):
        self.ventanaActualizacionSalida.exec_()
        
    def mostrarActualizacionVuelos(self):
        self.ventanaActualizacionVuelos.exec_()
            
def main():
        app = QtGui.QApplication (sys.argv)
        ventana = Principal()
        ventana.show()
        sys.exit(app.exec_())
        
if __name__ == '__main__':
    main()
