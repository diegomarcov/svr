from abstractmodel import AbstractModel
import datetime

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

	# este procedimiento se llama con un id particular si se desea modificar; 
	# para las inserciones, no se pone ningún ID, y por defecto se inserta con una nueva.
	def save(self, id=-1, estado, precio, forma_de_pago, doc_nro, nombre_cliente, pasaporte, vuelo, diayhora):
		if id != (-1):
		# es una modificacion
			self.conn.update("update "+self.tableName+" set estado="+estado+", precio="+precio+", forma_de_pago="+forma_de_pago+", doc_nro="+doc_nro+", nombre_cliente="+nombre_cliente+", pasaporte="+pasaporte+", vuelo="+vuelo+", diahora_sale="+diayhora+" where id="+id)
		else:
		#estoy insertando una reserva nueva
			#declaro la fecha y hora actual, y la de vencimiento (exactamente 48hs después); strftime la formatea "en SQL"
			fecha_realizacion =  datetime.datetime.now()
			vencimiento = fecha_realizacion + datetime.timedelta(days=2)
			fecha_realizacion = fecha_realizacion.strftime("%Y-%m-%d %H:%M:%S")
			vencimiento = vencimiento.strftime("%Y-%m-%d %H:%M:%S")
			# NOW DO IT!
			self.conn.update("insert into "+self.tableName+" (fecha_realizacion, vencimiento, estado, precio, forma_de_pago, doc_nro, nombre_cliente, pasaporte, vuelo, diayhora) values ("+fecha_realizacion+", "+vencimiento+", "+estado+", "+precio+", "+forma_de_pago+", "+ doc_nro+", "+nombre_cliente+", "+pasaporte+", "+vuelo+", "+diayhora)
			
	def loadAll(self, vuelo, dia_y_hora):
		self.conn.query("select * from reservas where vuelo = "+vuelo+", diahora_sale = "+dia_y_hora)