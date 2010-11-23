from PyQt4                      import QtCore, QtGui
from models.vuelos              import Vuelos
from models.salidas             import Salidas
from ui.agregarInstanciasVuelo  import Ui_AgregarSalidas

class AgregarSalidasDialog(QtGui.QDialog):

    def setup(self, conn):
        self.ui = Ui_AgregarSalidas()
        self.ui.setupUi(self)
        vuelos = Vuelos(self.conn)
        vuelos.loadAll()
        self.ui.comboBoxVuelos.setModel(vuelos.getModel())
        self.connect(self.ui.buttonBox, QtCore.SIGNAL('accepted()'), self.agregarSalida)

    def __init__(self, parent = None, conn = None):
        super(AgregarSalidasDialog, self).__init__(parent)
        self.conn = conn
        self.setup(self.conn)

    def agregarSalida(self):
        vuelo_id    = self.ui.comboBoxVuelos.currentText()
        horaSalida  = self.ui.dateTimeEditHoraSalida.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        horaLlegada = self.ui.dateTimeEditHoraLlegada.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        estado      = "A tiempo"
        salidas     = Salidas(self.conn)
        salidas.insert(vuelo_id, horaSalida, horaLlegada, estado)
        print "Nueva salida de vuelo agregada!"
