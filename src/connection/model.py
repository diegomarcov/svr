# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore,QtSql
from error import Error

"""
Clase que hereda de QSqlQueryModel implementando metodos para retornar datos especificos de una consulta
"""
class Model(QtSql.QSqlQueryModel):
	
	"""
    Metodo para retornar el contenido de una celda correspondiente a la ultima consulta.
    *Parametros:	1)	columnName:	QString, nombre de la columns.
    				2)	rowIndex:	integer, valor por defecto=0, numero de fila.
    *Retorno:	QVariable (QString), contenido de la consulta en una dada columna para una fila determinada.
    *Excepciones: nada.
    
    ''' Esta misma función se puede usar con la columna mandandose enteros. Como la función record y isNull está sobrecargada, no hay que cambiar nada. Lo único que hice fue cambiarle los nombres para que se entienda que es más general. by leos
    '''
	"""
	def getItem(self,column=0,row=0):
		if row<0 or self.rowCount()<=row:
			raise Error("Error al intentar acceder a la fila "+QtCore.QString.number(row),"Error de acceso a la tabla.")
		row=self.record(row)
		if row.isNull(column):
			raise Error("Error al intentar acceder a la columna '"+column+"'","Error de acceso a la tabla.")
		return  row.value(column) #.toString()

