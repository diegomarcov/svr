from abstractmodel import AbstractModel

from PyQt4 import QtCore

class Salidas(AbstractModel):
    def __init__(self, conn):
        super(Salidas, self).__init__(conn)

        self.tableName = "salidas"
        self.id = "id"