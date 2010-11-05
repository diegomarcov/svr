from abstractmodel import AbstractModel

from PyQt4 import QtCore

class Aeropuertos(AbstractModel):
    def __init__(self, conn):
        super(Aeropuertos, self).__init__(conn)

        self.tableName = "aeropuertos"
        self.id = "codigo"

#	Metodos heredados:
#    def getModel(self)
#    def get(self, column)
#    def load(self, id)
#    def loadAll(self)
#    def delete(self, id)
