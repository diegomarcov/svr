# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from ui.reservas            import Ui_VentanaReservas
from models.reservas        import Reservas
from AgregarReservasDialog  import AgregarReservasDialog
from ActualizarReservasDialog  import ActualizarReservasDialog

class ReservasDialog(QtGui.QDialog):

    def setup(self):
        self.ui = Ui_VentanaReservas()
        self.ui.setupUi(self)
        self.reservas = Reservas(self.conn)
        
        self.ventanaAgregarReservas = AgregarReservasDialog(self, self.conn)
        
        self.ventanaActualizarReservas = ActualizarReservasDialog(self, self.conn)
        
        self.connect(self.ui.btnAgregarReserva, QtCore.SIGNAL('clicked()'), self.mostrarAgregarReserva)
        self.connect(self.ui.btnModificarReserva, QtCore.SIGNAL('clicked()'), self.mostrarModificarReserva)
        self.connect(self.ui.btnEliminarReserva, QtCore.SIGNAL('clicked()'), self.eliminarReserva)
    
    def setData(self, vuelo, dia_y_hora):
        self.ui.labelIDVuelo.setText("Reservas para \""+vuelo+"\"")
        self.vuelo = vuelo
        self.dia_y_hora = dia_y_hora
        self.reservas.loadAll(self.vuelo, self.dia_y_hora)
        print "Reservas cargadas!!!!!!!!"
        self.ui.tablaReservas.setModel(self.reservas.model)
    
    def __init__(self, parent, conn):
        super(ReservasDialog, self).__init__(parent)
        self.conn = conn
        self.setup()

    #--------------------------------------------------------------------------#
    def mostrarAgregarReserva(self):
        self.ventanaAgregarReservas.setData(self.vuelo, self.dia_y_hora)
        self.ventanaAgregarReservas.exec_()
        #reload table
        self.setData(self.vuelo, self.dia_y_hora)
        
    def mostrarModificarReserva(self):
        if (self.ui.tablaReservas.selectedIndexes()):
            rowIndex = self.ui.tablaReservas.selectionModel().currentIndex().row()
            currentRow = self.reservas.getModel().record(rowIndex)
            id = currentRow.value(0).toString()
            dni = currentRow.value(6).toString()
            nombre = currentRow.value(7).toString()
            pasaporte = currentRow.value(8).toString()
            estado = currentRow.value(3).toString()
            forma_de_pago = currentRow.value(5).toString()
            precio = currentRow.value(4).toString()
            self.ventanaActualizarReservas.setData(self.vuelo, self.dia_y_hora, id, dni, pasaporte, estado, forma_de_pago, nombre, precio)
            self.ventanaActualizarReservas.exec_()
            # reload table
            self.setData(self.vuelo, self.dia_y_hora)
            
    
    def eliminarReserva(self):
        # si hay al menos una reserva seleccionada
        
        if (self.ui.tablaReservas.selectedIndexes()):
            rowIndex = self.ui.tablaReservas.selectionModel().currentIndex().row()
            if rowIndex>=0:
                reply = QtGui.QMessageBox.question(self, "Mensaje", "¿Está seguro que desea eliminar ese registro?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

                if reply == QtGui.QMessageBox.Yes:
                    numeroReserva = self.reservas.getModel().record(rowIndex).value(0).toString()
                    self.reservas.delete(numeroReserva)
                    #reload table
                    self.setData(self.vuelo, self.dia_y_hora)
