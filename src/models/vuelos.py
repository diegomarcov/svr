# -*- coding: utf-8 -*-
from PyQt4          import QtCore
from abstractmodel  import AbstractModel

class Vuelos(AbstractModel):
    def __init__(self, conn):
        super(Vuelos, self).__init__(conn)
        self.tableName = "vuelos"
        self.id = "id"

    def insert(self, id, salida, llegada):
        self.conn.update("insert into "+self.tableName+" (id, aeropuerto_salida, aeropuerto_llegada) values ('"+id+"', '"+salida+"', '"+llegada+"')")

    def update(self, oldid, newid, salida, llegada):
        self.conn.update("update "+self.tableName+" set id='"+newid+"', aeropuerto_salida='"+salida+"', aeropuerto_llegada='"+llegada+"' where id='"+oldid+"'")

    def loadAll(self):
        self.model = self.conn.query("select * from "+self.tableName)
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Identificador")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Aeropuerto de Salida")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Aeropuerto de Llegada")

