from PyQt4 import QtCore, QtGui

from ui.agregarInstanciasVuelo import Ui_AgregarSalidas

class AgregarSalidasDialog(QtGui.QDialog):

    def setup(self):
        self.ui = Ui_AgregarSalidas()
        self.ui.setupUi(self)
    
    def __init__(self,parent = None):
        super(AgregarSalidasDialog, self).__init__(parent)
        self.setup()