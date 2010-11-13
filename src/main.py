import sys

from connection.connection   import Connection

from PyQt4                   import QtCore, QtGui
from ui.mainWindow           import Ui_MainWindow
from ActualizarSalidasDialog import ActualizarSalidasDialog
from ActualizarVuelosDialog  import ActualizarVuelosDialog
from AgregarSalidasDialog    import AgregarSalidasDialog
from models.vuelos           import Vuelos
from models.salidas          import Salidas
from models.reservas         import Reservas

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
        
        # Creacion de la ventana para actualizacion de los vuelos
        self.ventanaActualizacionVuelos = ActualizarVuelosDialog(parent = self, conn = self.conn)
        
        # Creacion del dialog ventana para la actualizacion de las salidas
        self.ventanaActualizacionSalida = ActualizarSalidasDialog()
        
        # Creacion del dialog ventana para la alta de las salidas.
        self.ventanaAltaVuelos = AgregarSalidasDialog()

        # Signals de los botones de la interface del sistema
        self.connect(self.ventana.btnVuelos,              QtCore.SIGNAL('clicked()'), self.mostrarTabVuelos)
        self.connect(self.ventana.btnAgregarVuelo,        QtCore.SIGNAL('clicked()'), self.mostrarActualizacionVuelos)
        self.connect(self.ventana.btnModificarVuelo,      QtCore.SIGNAL('clicked()'), self.mostrarActualizacionVuelos)
        self.connect(self.ventana.btnEliminarVuelo,       QtCore.SIGNAL('clicked()'), self.eliminarVuelo)
        
        self.connect(self.ventana.btnInstanciasVuelos,    QtCore.SIGNAL('clicked()'), self.mostrarTabInstVuelos)
        self.connect(self.ventana.btnAgregarInstVuelos,   QtCore.SIGNAL('clicked()'), self.mostrarAltaInstanciasVuelos)
        self.connect(self.ventana.btnModificarInstVuelos, QtCore.SIGNAL('clicked()'), self.mostrarActualizacionInstanciasVuelos)
        self.connect(self.ventana.btnEliminarInstVuelos,  QtCore.SIGNAL('clicked()'), self.eliminarInstanciaVuelo)
    
    #--------------------------------------------------------------------------#
    def refreshTableViews(self):
        self.todosLosVuelos.loadAll()
        self.ventana.tablaVuelos.setModel(self.todosLosVuelos.model)
        self.todasLasSalidas.loadAll()
        self.ventana.tablaSalidas.setModel(self.todasLasSalidas.model)
        
    #--------------------------------------------------------------------------#
    def mostrarTabVuelos(self):
        self.refreshTableViews()
        self.ventana.stackedWidget.setCurrentIndex(1)
                                                                                            
    #--------------------------------------------------------------------------#
    def mostrarAltaInstanciasVuelos(self):
        self.ventanaAltaVuelos.exec_()

    #--------------------------------------------------------------------------#
    def mostrarActualizacionVuelos(self):
        self.ventanaActualizacionVuelos.exec_()
    
    #--------------------------------------------------------------------------#
    def eliminarVuelo(self):
        index = self.ventana.tablaVuelos.selectionModel().currentIndex().row()
        vuelo_id = self.todosLosVuelos.getModel().record(index).value(0).toString()
        print "Selected index: ", index, "ID: ", vuelo_id

        # Con el id del vuelo, eliminar todas las salidas con ese id de vuelo.
        modelo_reservas = Reservas(self.conn)
        salidas  = Salidas(self.conn)
        salidas.loadAllFlightInstances(vuelo_id)
        modelo_salidas = salidas.getModel()

        for salida in range(modelo_salidas.rowCount()):
            # Borrar todas las reservas asociadas a esta instancia de vuelo.
            diahora_sale = modelo_salidas.record(salida).value(1).toString()
            print "Eliminando reservas de la instancia de de vuelo: ", vuelo_id, diahora_sale
            modelo_reservas.deleteAll(vuelo_id, diahora_sale)

        print "Eliminando todas las instancias de este vuelo..."
        self.todasLasSalidas.deleteAll(vuelo_id)
        print "Eliminando el vuelo..."
        self.todosLosVuelos.delete(vuelo_id)
        print "Vuelo eliminado exitosamente."
        self.refreshTableViews()
    
    #--------------------------------------------------------------------------#
    def mostrarTabInstVuelos(self):
        # Al mostrar devuelta el tab de las instancias de vuelos, volver a 
        # cargar los datos en la tabla.
        self.refreshTableViews()
        self.ventana.stackedWidget.setCurrentIndex(0)
    
    #--------------------------------------------------------------------------#
    def mostrarActualizacionInstanciasVuelos(self):
        self.ventanaActualizacionSalida.exec_()
    
    #--------------------------------------------------------------------------#
    def eliminarInstanciaVuelo(self):
        # Obtener el id de la salida seleccionada
        index        = self.ventana.tablaSalidas.selectionModel().currentIndex().row()
        vuelo_id     = self.todasLasSalidas.getModel().record(index).value(0).toString()
        diahora_sale = self.todasLasSalidas.getModel().record(index).value(1).toString()

        # Borrar todas las reservas asociadas a esta instancia de vuelo.
        reservas = Reservas(self.conn)
        reservas.deleteAll(vuelo_id, diahora_sale)

        # Ahora que las restricciones de clave foraneas estan satisfechas, 
        # efectivamente borrar la instancia de vuelo.
        self.todasLasSalidas.delete(vuelo_id, diahora_sale)
        print "Instancia de vuelo eliminada exitosamente."
        self.refreshTableViews()
    
#------------------------------------------------------------------------------#
def main():
        app = QtGui.QApplication (sys.argv)
        ventana = Principal()
        ventana.show()
        sys.exit(app.exec_())
        
if __name__ == '__main__':
    main()
