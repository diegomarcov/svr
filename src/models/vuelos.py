from abstractmodel import AbstractModel

from PyQt4 import QtCore

class Vuelos(AbstractModel):
    def __init__(self, conn):
        super(Vuelos, self).__init__(conn)

        self.tableName = "vuelos"
        self.id = "id"
