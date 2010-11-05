from PyQt4 import QtCore, QtGui

from ui.actualizacionInstanciasVuelo import Ui_ActualizarSalidas

class actualizarSalidasDialog(QtGui.QDialog):

    def setup(self):
        self.ui = Ui_ActualizarSalidas()
        self.ui.setupUi(self)
    
    def __init__(self,parent = None):
        super(actualizarSalidasDialog, self).__init__(parent)
        self.setup()