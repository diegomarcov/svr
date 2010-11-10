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
        # Y para eliminar una instancia de vuelo hay que eliminar todas las 
        # reservas asociadas a ella.

        # Traceback (most recent call last):
        #   File "main.py", line 65, in eliminarVuelo
        #     self.todosLosVuelos.delete(vuelo_id)
        #   File "/home/igaray/Documents/Personal/uns/materias actuales/agps/2010/proyecto/implementacion/svr/src/models/abstractmodel.py", line 28, in delete
        #     self.conn.update("delete from " + self.tableName + " where " + self.id + " = '" + str(id) + "'")
        #   File "/home/igaray/Documents/Personal/uns/materias actuales/agps/2010/proyecto/implementacion/svr/src/connection/connection.py", line 107, in update
        #     raise Error(msg,"Error de conexion.")
        # connection.error.Error Error al intentar actualizar la Base de Datos: Cannot delete or update a parent row: a foreign key constraint fails (`svr`.`salidas`, CONSTRAINT `salidas_ibfk_1` FOREIGN KEY (`vuelo`) REFERENCES `vuelos` (`id`)) QMYSQL3: Unable to execute statement

        # y ademas:
        
        # Traceback (most recent call last):
        #   File "main.py", line 80, in eliminarVuelo
        #     self.todasLasSalidas.deleteAll(vuelo_id)
        #   File "/home/igaray/Documents/Personal/uns/materias actuales/agps/2010/proyecto/implementacion/svr/src/models/salidas.py", line 25, in deleteAll
        #     self.conn.update("delete from " + self.tableName + " where " + self.id1 + " = '" + str(vuelo) + "'")
        #   File "/home/igaray/Documents/Personal/uns/materias actuales/agps/2010/proyecto/implementacion/svr/src/connection/connection.py", line 107, in update
        #     raise Error(msg,"Error de conexion.")
        # connection.error.Error Error al intentar actualizar la Base de Datos: Cannot delete or update a parent row: a foreign key constraint fails (`svr`.`reservas`, CONSTRAINT `reservas_ibfk_1` FOREIGN KEY (`vuelo`, `diahora_sale`) REFERENCES `salidas` (`vuelo`, `diahora_sale`)) QMYSQL3: Unable to execute statement

        # Lo mismo hay que corregir en el metodo eliminarInstanciaVuelo, a 
        # veces tiene exito porque justo se selecciona una instancia de vuelo 
        # que no tiene reservas asociadas.
        
        # - Aki

        index = self.ventana.tablaVuelos.selectionModel().currentIndex().row()
        vuelo_id = self.todosLosVuelos.getModel().record(index).value(0).toString()
        print "Selected index: ", index, "ID: ", vuelo_id

        # Con el id del vuelo, eliminar todas las salidas con ese id de vuelo.
        # OJO: hay que eliminar todas las reservas asociadas con cada instancia de vuelo antes de poder borrar una instancia. 
        # Agregue un metodo en el modelo de reservas para hacer esto, deleteAll
        print "Eliminando todas las instancias de este vuelo..."
        self.todasLasSalidas.deleteAll(vuelo_id)
        print "Eliminando el vuelo..."
        #self.todosLosVuelos.delete(vuelo_id)
        print "Vuelo eliminado exitosamente."
    
    def mostrarTabInstVuelos(self):
        # Al mostrar devuelta el tab de las instancias de vuelos, volver a 
        # cargar los datos en la tabla.
        self.todasLasSalidas = Salidas(self.conn)
        self.todasLasSalidas.loadAll()
        self.ventana.tablaSalidas.setModel(self.todasLasSalidas.model)
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
