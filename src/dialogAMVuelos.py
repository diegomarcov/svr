from PyQt4 import QtCore, QtGui

from ui.actualizacionVuelos import Ui_ActualizarVuelo

class actualizarVuelosDialog(QtGui.QDialog):

    def setup(self):
        self.ui = Ui_ActualizarVuelo()
        self.ui.setupUi(self)
    
    def __init__(self,parent = None):
        super(actualizarVuelosDialog, self).__init__(parent)
        self.setup()