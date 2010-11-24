from PyQt4 import QtCore, QtGui

from ui.about import Ui_About

class About(QtGui.QDialog):

    def __init__(self):
        super(About, self).__init__()
        self.setup()
        
    def setup(self):
        self.ui = Ui_About()
        self.ui.setupUi(self)