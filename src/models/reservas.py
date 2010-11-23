# -*- coding: utf-8 -*-

from abstractmodel import AbstractModel
import datetime

from PyQt4 import QtCore

class Reservas(AbstractModel):
    def __init__(self, conn):
        super(Reservas, self).__init__(conn)

        self.tableName = "reservas"
        self.id = "numero"

#   Metodos heredados:
#    def getModel(self)
#    def get(self, column)
#    def load(self, id)
#    def loadAll(self)
#    def delete(self, id)

    # este procedimiento se llama con un id particular si se desea modificar; 
    # para las inserciones, no se pone ningun ID, y por defecto se inserta con una nueva.
    def save(self, estado, precio, forma_de_pago, doc_nro, nombre_cliente, pasaporte, vuelo, diayhora, id=-1):
        if id != (-1):
        # es una modificacion
            self.conn.update("update "+self.tableName+" set estado='"+estado+"', precio="+precio+", forma_de_pago='"+forma_de_pago+"', doc_nro="+doc_nro+", nombre_cliente='"+nombre_cliente+"', pasaporte="+pasaporte+", vuelo='"+vuelo+"', diahora_sale='"+diayhora+"' where numero="+id)
        else:
        #estoy insertando una reserva nueva
            #declaro la fecha y hora actual, y la de vencimiento (exactamente 48hs después); strftime la formatea "en SQL"
            fecha_realizacion =  datetime.datetime.now()
            vencimiento = fecha_realizacion + datetime.timedelta(days=2)
            fecha_realizacion = fecha_realizacion.strftime("%Y-%m-%d %H:%M:%S")
            vencimiento = vencimiento.strftime("%Y-%m-%d %H:%M:%S")
            # NOW DO IT!
            q = "insert into "+self.tableName+" (fecha_realizacion, vencimiento, estado, precio, forma_de_pago, doc_nro, nombre_cliente, pasaporte, vuelo, diahora_sale) values ('"+fecha_realizacion+"', '"+vencimiento+"', '"+estado+"', "+precio+", '"+forma_de_pago+"', "+ doc_nro+", '"+nombre_cliente+"', "+pasaporte+", '"+vuelo+"', '"+diayhora+"')"
            print q
            self.conn.update(q)

    def loadAll(self, vuelo, dia_y_hora):
        self.model = self.conn.query("select * from reservas where vuelo = '"+vuelo+"' and diahora_sale = '"+dia_y_hora+"'")
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Numero")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Fecha de realizacion")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Vencimiento")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Estado")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Precio")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Forma de Pago")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Doc Nro")
        self.model.setHeaderData(7, QtCore.Qt.Horizontal, "Nombre Cliente")
        self.model.setHeaderData(8, QtCore.Qt.Horizontal, "Pasaporte")
        self.model.setHeaderData(9, QtCore.Qt.Horizontal, "Vuelo")
        self.model.setHeaderData(10, QtCore.Qt.Horizontal, "Dia y Hora de Salida")
        
    def deleteAll(self, vuelo, diahora_sale):
        """
        Este metodo elimina todas las reservas asociadas a una instancia de vuelo, 
        definida por los dos atributos clave de la tabla salidas: el id del vuelo y el 
        dia y hora de salida.
        """
        self.conn.update("delete from " + self.tableName + " where (vuelo = '" + str(vuelo) + "') and (diahora_sale = '" + str(diahora_sale) + "')")

    def actualizarReservasVencidas(self):
        self.conn.update("update reservas set reservas.estado='Vencida' where (reservas.estado = 'Pendiente') and (vencimiento <= now())") 
