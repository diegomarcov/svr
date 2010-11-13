from abstractmodel import AbstractModel

from PyQt4 import QtCore

class Vuelos(AbstractModel):
    def __init__(self, conn):
        super(Vuelos, self).__init__(conn)

        self.tableName = "vuelos"
        self.id = "id"

    def loadAll(self):
        self.model = self.conn.query("select * from "+self.tableName)
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Identificador")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Aeropuerto de Salida")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Aeropuerto de Llegada")
