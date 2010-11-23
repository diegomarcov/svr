# -*- coding: utf-8 -*-
from PyQt4 import QtCore
from abstractmodel import AbstractModel

# OJO: si se quiere usar algun metodo heredado de la superclase AbstractModel, 
# que utilize el atributo self.id, hay que reimplementarlo porque la tabla de
# salidas tiene dos atributos como clave primaria

class Salidas(AbstractModel):
    def __init__(self, conn):
        super(Salidas, self).__init__(conn)
        self.tableName = "salidas"
        self.id1 = "vuelo"
        self.id2 = "diahora_sale"

    def setHeaders(self):
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Vuelo")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Dia y Hora de Salida")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Dia y Hora de Llegada")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Estado")
        
    def loadAll(self):
        self.model = self.conn.query("select * from " + self.tableName)
        self.setHeaders()

    def loadAllFlightInstances(self, vuelo):
        """
        Carga todas las instancias de vuelos asociadas a un vuelo. 
        """
        self.model = self.conn.query("select * from " + self.tableName + " where " + self.id1 + " = '" + str(vuelo) + "'")
        self.setHeaders()

    def delete(self, vuelo, diahora_sale):
        self.conn.update("delete from " + self.tableName + " where " + self.id1 + " = '" + str(vuelo) + "' and " + self.id2 + " = '" + str(diahora_sale) + "'")

    def deleteAll(self, vuelo):
        """
        Este metodo elimina todas las instancias de vuelos asociadas a un vuelo, 
        definido por el id del vuelo.
        """
        self.conn.update("delete from " + self.tableName + " where " + self.id1 + " = '" + str(vuelo) + "'")

    def insert(self, vuelo_id, diahora_sale, diahora_llega, estado):
        self.conn.update("insert into " + self.tableName + " (vuelo, diahora_sale, diahora_llega, estado) values ('"+ vuelo_id + "', '"+ diahora_sale +"', '" + diahora_llega + "', '" + estado + "')")

    def update(self, vuelo1, diahora_sale1, diahora_sale2, diahora_llega, estado):
        print            "update " + self.tableName + " set diahora_sale = '" + diahora_sale2 + "', diahora_llega = '" + diahora_llega + "', estado = '" + estado + "' where (vuelo = '" + vuelo1 + "') and (diahora_sale = '" + diahora_sale1 + "')"
        self.conn.update("update " + self.tableName + " set diahora_sale = '" + diahora_sale2 + "', diahora_llega = '" + diahora_llega + "', estado = '" + estado + "' where (vuelo = '" + vuelo1 + "') and (diahora_sale = '" + diahora_sale1 + "')")

    def loadByDate(self, date):
        self.model = self.conn.query("select * from salidas where date(diahora_sale) = '%s'" % date)
        self.setHeaders()