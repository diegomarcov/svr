import sys
from PyQt4 import QtCore, QtGui
from ui.mainWindow import Ui_MainWindow
from ui.actualizacionInstanciasVuelo import Ui_ActualizarSalidas
from ui.actualizacionVuelos import Ui_ActualizarVuelo

class Principal (QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        #creacion de la ventana principal
        self.ventana = Ui_MainWindow()
        self.ventana.setupUi(self)
        
        #creacion de la ventana para actualizacion de los vuelos
        self.ventanaActualizacionVuelos = Ui_ActualizarVuelo()
        
        #creacion de la ventana para la actualizacion de las salidas
        self.ventanaActualizacionSalida = Ui_ActualizarSalidas()
       
       #signals de los botones de la interface del sistema
        self.connect(self.ventana.btnVuelos, QtCore.SIGNAL('clicked()'), self.mostrarTabVuelos)
        self.connect(self.ventana.btnInstanciasVuelos, QtCore.SIGNAL('clicked()'), self.mostrarTabInstVuelos)
        self.connect(self.ventana.btnModificarInstVuelos, QtCore.SIGNAL('clicked()'), self.mostrarActualizacionInstanciasVuelos)
        self.connect(self.ventana.btnEliminarInstVuelos, QtCore.SIGNAL('clicked()'), self.mostrarActualizacionInstanciasVuelos)
        self.connect(self.ventana.btnAgregarInstVuelos, QtCore.SIGNAL('clicked()'), self.mostrarActualizacionInstanciasVuelos)
        
    def mostrarTabVuelos(self):
        self.ventana.stackedWidget.setCurrentIndex(1)
    
    def mostrarTabInstVuelos(self):
        self.ventana.stackedWidget.setCurrentIndex(0)

    def mostrarActualizacionInstanciasVuelos(self):
        #el problema esta en q la ventana no hereda de QtGui.QtDialog sino q hereda de object FFFUUU!
        self.ventanaActualizacionVuelos.exec_()
            
def main ():
        app = QtGui.QApplication (sys.argv)
        ventana = Principal()
        ventana.show()
        sys.exit(app.exec_())
        
if __name__ == '__main__':
    main()
    