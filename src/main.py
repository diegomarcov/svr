import sys
from PyQt4 import QtCore, QtGui
from ui.mainWindow import Ui_MainWindow

class Principal (QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        self.ventana = Ui_MainWindow()
        self.ventana.setupUi(self)
        
        self.connect(self.ventana.btnVuelos, QtCore.SIGNAL('clicked()'), self.mostrarTabVuelos)
        self.connect(self.ventana.btnInstanciasVuelos, QtCore.SIGNAL('clicked()'), self.mostrarTabInstVuelos)
        
        
    def mostrarTabVuelos(self):
        self.ventana.stackedWidget.setCurrentIndex(1)
    
    def mostrarTabInstVuelos(self):
        self.ventana.stackedWidget.setCurrentIndex(0)
        
def main ():
        app = QtGui.QApplication (sys.argv)
        ventana = Principal()
        ventana.show()
        sys.exit(app.exec_())
        
if __name__ == '__main__':
    main()
    