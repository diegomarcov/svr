from abstractmodel import AbstractModel

from PyQt4 import QtCore

class Reservas(AbstractModel):
	def __init__(self, conn):
		super(Tipo, self).__init__(conn)

		self.tableName = "reservas"
		self.id = "numero"
	
#	Metodos heredados:
#    def getModel(self)
#    def get(self, column)
#    def load(self, id)
#    def loadAll(self)
#    def delete(self, id)

	def save(self, id=-1, estado, precio, forma_de_pago, doc_nro, nombre_cliente, pasaporte, vuelo, diayhora):
		pass