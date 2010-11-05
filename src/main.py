import sys
from PyQt4 import QtCore, QtGui
from ui.mainWindow import Ui_MainWindow
from dialogAMInstanciasVuelo import actualizarSalidasDialog
from dialogAMVuelos import actualizarVuelosDialog

class Principal (QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        #creacion de la ventana principal
        self.ventana = Ui_MainWindow()
        self.ventana.setupUi(self)
        
        #creacion de la ventana para actualizacion de los vuelos
        self.ventanaActualizacionVuelos = actualizarVuelosDialog()
        
        #creacion del dialog ventana para la actualizacion de las salidas
        self.ventanaActualizacionSalida = actualizarSalidasDialog()
       
       #signals de los botones de la interface del sistema
        self.connect(self.ventana.btnVuelos, QtCore.SIGNAL('clicked()'), self.mostrarTabVuelos)
        self.connect(self.ventana.btnInstanciasVuelos, QtCore.SIGNAL('clicked()'), self.mostrarTabInstVuelos)
        self.connect(self.ventana.btnModificarInstVuelos, QtCore.SIGNAL('clicked()'), self.mostrarActualizacionInstanciasVuelos)
        # self.connect(self.ventana.btnEliminarInstVuelos, QtCore.SIGNAL('clicked()'), self.mostrarActualizacionInstanciasVuelos)
        self.connect(self.ventana.btnAgregarInstVuelos, QtCore.SIGNAL('clicked()'), self.mostrarActualizacionInstanciasVuelos)
        self.connect(self.ventana.btnAgregarVuelo, QtCore.SIGNAL('clicked()'), self.mostrarActualizacionVuelos)
        
    def mostrarTabVuelos(self):
        self.ventana.stackedWidget.setCurrentIndex(1)
    
    def mostrarTabInstVuelos(self):
        self.ventana.stackedWidget.setCurrentIndex(0)

    def mostrarActualizacionInstanciasVuelos(self):
        self.ventanaActualizacionSalida.exec_()
        
    def mostrarActualizacionVuelos(self):
        self.ventanaActualizacionVuelos.exec_()
            
def main ():
        app = QtGui.QApplication (sys.argv)
        ventana = Principal()
        ventana.show()
        sys.exit(app.exec_())
        
if __name__ == '__main__':
    main()
    