from PyQt4 import QtCore, QtGui

from ui.actualizacionReserva import Ui_actualizarReserva
from models.reservas         import Reservas

class AgregarReservasDialog(QtGui.QDialog):

    def setup(self):
        self.ui = Ui_actualizarReserva()
        self.ui.setupUi(self)
        
        self.ui.comboBoxEstado.addItems(['Pendiente', 'Confirmada', 'Finalizada', 'Vencida', 'Cancelada'])
        self.ui.comboBoxPago.addItems(['Efectivo', 'Tarjeta', 'Cheque'])
        
        self.connect(self.ui.buttonBox, QtCore.SIGNAL('accepted()'), self.agregarReserva)
    
    def setData(self, vuelo, dia_y_hora):
        self.vuelo = vuelo
        self.diayhora = dia_y_hora
        self.ui.lineEditNombreCliente.setText("")
        self.ui.lineEditDNI.setText("")
        self.ui.lineEditPasaporte.setText("")
        self.ui.comboBoxEstado.setCurrentIndex(0)
        self.ui.comboBoxPago.setCurrentIndex(0)
        self.ui.spinBoxPrecio.setValue(250)

        
    def __init__(self, parent, conn):
        super(AgregarReservasDialog, self).__init__(parent)
        self.conn = conn
        self.reserva = Reservas(self.conn)
        self.setup()

    # numero              INT(15) UNSIGNED AUTO_INCREMENT,
    # fecha_realizacion   DATE NOT NULL,
    # vencimiento         DATE NOT NULL,
    # estado              ENUM ('Finalizada','Pendiente', 'Confirmada', 'Vencida', 'Cancelada'),
    # precio              DECIMAL(10,2) NOT NULL,
    # forma_de_pago       ENUM ('Efectivo', 'Tarjeta', 'Cheque'),
    # doc_nro             INT(10) UNSIGNED NOT NULL,
    # nombre_cliente      VARCHAR(45) NOT NULL,
    # pasaporte           VARCHAR(45) NOT NULL,
    # vuelo               VARCHAR(30) NOT NULL,
    # diahora_sale        TIMESTAMP NOT NULL,
    # FOREIGN KEY (vuelo, diahora_sale)        REFERENCES salidas (vuelo, diahora_sale),
    # PRIMARY KEY (numero)
    def agregarReserva(self):
        self.reserva.save(estado = self.ui.comboBoxEstado.currentText(), precio = self.ui.spinBoxPrecio.cleanText(), forma_de_pago = self.ui.comboBoxPago.currentText(), doc_nro = self.ui.lineEditDNI.text(), nombre_cliente = self.ui.lineEditNombreCliente.text(), pasaporte = self.ui.lineEditPasaporte.text(), vuelo = self.vuelo, diayhora = self.diayhora)
        # def save(self, estado, precio, forma_de_pago, doc_nro, nombre_cliente, pasaporte, vuelo, diayhora, id=-1):
        
    #--------------------------------------------------------------------------#