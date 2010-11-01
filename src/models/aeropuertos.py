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

	def save(self, id=-1, nombre_cliente="", descripcion=""):
		if id != -1:
			print "update "+self.tableName+" set nombre='"+nombre+"', "+"costoTemporadaAlta="+str(costoTemporadaAlta)+", "+	"costoTemporadaBaja="+str(costoTemporadaBaja)+", "+	"descripcion='"+descripcion+"' "+				" where idTipo="+str(id)
			self.conn.update("update "+self.tableName+
				" set nombre='"+nombre+"', "+
					"costoTemporadaAlta="+str(costoTemporadaAlta)+", "+
					"costoTemporadaBaja="+str(costoTemporadaBaja)+", "+
					"descripcion='"+descripcion+"' "+
				" where idTipo="+str(id))
		else:
			self.conn.update("insert into "+self.tableName+
				"(nombre,costoTemporadaAlta,costoTemporadaBaja,descripcion) "+
				"values ('"+nombre+"',"+str(costoTemporadaAlta)+","+str(costoTemporadaBaja)+",'"+descripcion+"')")

	def loadAll(self):
		super(Tipo, self).loadAll()
		self.model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
		self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Nombre")
		self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Costo en Temporada Alta")
		self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Costo en Temporada Baja")
		self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Descripcion")
		
	def checkname(self, nombre=""):
		#print "select * from tipo where nombre = '" + nombre + "'"
		self.model = self.conn.query("select * from tipo where nombre = '" + nombre + "'")
		return self.model.rowCount()
		
	def checkelim(self, id=""):
		model = self.conn.query("select * from unidad where tipo = " + str(id))
		return model.rowCount()
