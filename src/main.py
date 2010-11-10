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
        
        # Creacion de la ventana principal
        self.ventana = Ui_MainWindow()
        self.ventana.setupUi(self)
        
        # Cargar vuelos en la tabla principal
        self.todosLosVuelos = Vuelos(self.conn)
        self.todosLosVuelos.loadAll()
        self.ventana.tablaVuelos.setModel(self.todosLosVuelos.model)
        
        # Cargar salidas en la tabla principal
        self.todasLasSalidas = Salidas(self.conn)
        self.todasLasSalidas.loadAll()
        self.ventana.tablaSalidas.setModel(self.todasLasSalidas.model)
        
        # creacion de la ventana para actualizacion de los vuelos
        self.ventanaActualizacionVuelos = ActualizarVuelosDialog(parent = self, conn = self.conn)
        
        # Creacion del dialog ventana para la actualizacion de las salidas
        self.ventanaActualizacionSalida = ActualizarSalidasDialog()
        
        # Signals de los botones de la interface del sistema
        self.connect(self.ventana.btnVuelos,              QtCore.SIGNAL('clicked()'), self.mostrarTabVuelos)
        self.connect(self.ventana.btnAgregarVuelo,        QtCore.SIGNAL('clicked()'), self.mostrarActualizacionVuelos)
        self.connect(self.ventana.btnModificarVuelo,      QtCore.SIGNAL('clicked()'), self.mostrarActualizacionVuelos)
        self.connect(self.ventana.btnEliminarVuelo,       QtCore.SIGNAL('clicked()'), self.eliminarVuelo)
        
        self.connect(self.ventana.btnInstanciasVuelos,    QtCore.SIGNAL('clicked()'), self.mostrarTabInstVuelos)
        self.connect(self.ventana.btnAgregarInstVuelos,   QtCore.SIGNAL('clicked()'), self.mostrarActualizacionInstanciasVuelos)
        self.connect(self.ventana.btnModificarInstVuelos, QtCore.SIGNAL('clicked()'), self.mostrarActualizacionInstanciasVuelos)
        self.connect(self.ventana.btnEliminarInstVuelos,  QtCore.SIGNAL('clicked()'), self.eliminarInstanciaVuelo)
        
    def mostrarTabVuelos(self):
        self.ventana.stackedWidget.setCurrentIndex(1)
    
    def mostrarActualizacionVuelos(self):
        self.ventanaActualizacionVuelos.exec_()
    
    def eliminarVuelo(self):
        # No se puede eliminar un vuelo asi nomas porque fallan los foreign
        # key constraints de otras tablas. Hay que eliminar todas las instancias
        # de vuelos que hacen referencia al vuelo a ser eliminado, y luego 
        # eliminar el vuelo.
        index = self.ventana.tablaVuelos.selectionModel().currentIndex().row()
        vuelo_id = self.todosLosVuelos.getModel().record(index).value(0).toString()
        print index, vuelo_id
        self.todosLosVuelos.delete(vuelo_id)
        print "Vuelo eliminado exitosamente."
    
    def mostrarTabInstVuelos(self):
        # Al mostrar devuelta el tab de las instancias de vuelos, volver a 
        # cargar los datos en la tabla.
        self.todasLasSalidas = Salidas(self.conn)
        self.todasLasSalidas.loadAll()
        self.ventana.tablaSalidas.setModel(todasLasSalidas.model)
        self.ventana.stackedWidget.setCurrentIndex(0)
    
    def mostrarActualizacionInstanciasVuelos(self):
        self.ventanaActualizacionSalida.exec_()
    
    def eliminarInstanciaVuelo(self):
        # Obtener el id de la salida seleccionada
        index = self.ventana.tablaSalidas.selectionModel().currentIndex().row()
        vuelo_id = self.todasLasSalidas.getModel().record(index).value(0).toString()
        diahora_sale = self.todasLasSalidas.getModel().record(index).value(1).toString()
        self.todasLasSalidas.delete(vuelo_id, diahora_sale)
        print "Instancia de vuelo eliminada exitosamente."
    
def main():
        app = QtGui.QApplication (sys.argv)
        ventana = Principal()
        ventana.show()
        sys.exit(app.exec_())
        
if __name__ == '__main__':
    main()
