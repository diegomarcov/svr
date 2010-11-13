from abstractmodel import AbstractModel

from PyQt4 import QtCore

# OJO: si se quiere usar algun metodo heredado de la superclase AbstractModel, 
# que utilize el atributo self.id, hay que reimplementarlo porque la tabla de
# salidas tiene dos atributos como clave primaria

class Salidas(AbstractModel):
    def __init__(self, conn):
        super(Salidas, self).__init__(conn)

        self.tableName = "salidas"
        self.id1 = "vuelo"
        self.id2 = "diahora_sale"

    def loadAll(self):
        self.model = self.conn.query("select * from "+self.tableName)
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Vuelo")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Dia y Hora de Salida")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Dia y Hora de Llegada")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Estado")
        
    def loadAllFlightInstances(self, vuelo):
        """
        Carga todas las instancias de vuelos asociadas a un vuelo. 
        """
        self.model = self.conn.query("select * from " + self.tableName + " where " + self.id1 + " = '" + str(vuelo) + "'")

    def delete(self, vuelo, diahora_sale):
        self.conn.update("delete from " + self.tableName + " where " + self.id1 + " = '" + str(vuelo) + "' and " + self.id2 + " = '" + str(diahora_sale) + "'")
        
    def deleteAll(self, vuelo):
        """
        Este metodo elimina todas las instancias de vuelos asociadas a un vuelo, 
        definido por el id del vuelo.
        """
        self.conn.update("delete from " + self.tableName + " where " + self.id1 + " = '" + str(vuelo) + "'")
