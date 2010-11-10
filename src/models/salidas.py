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

    def delete(self, vuelo, diahora_sale):
        self.conn.update("delete from " + self.tableName + " where " + self.id1 + " = '" + str(vuelo) + "' and " + self.id2 + " = '" + str(diahora_sale) + "'")
        
    def deleteAll(self, vuelo):
        """
        Este metodo elimina todas las instancias de vuelos asociadas a un vuelo, 
        definido por el id del vuelo.
        """
        self.conn.update("delete from " + self.tableName + " where " + self.id1 + " = '" + str(vuelo) + "'")
