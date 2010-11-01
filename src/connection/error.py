import exceptions

"""
Clase que modela excepciones definidas por el usuario.
"""
class Error(Exception):

	"""
	*Constructor de la clase.
	*Parametros:
		1)	msg:	string, mensaje de error de la excepcion.
	*Excepciones: nada.
	"""
	def __init__(self, msg,type):
		self.msg = msg
		self.type = type
	"""
	Metodo para retornar mensaje de error de la excepcion.
	*Parametros: nada.
	*Excepciones: nada.
	*Retorno: nada.
	"""
	def getMsg(self):
		return self.msg
		
	"""
	Metodo para retornar el tipo de la excepcion.
	*Parametros: nada.
	*Excepciones: nada.
	*Retorno: nada.
	"""
	def getType(self):
		return self.type

	"""
	Metodo para imprimir el mensaje de error de la excepcion.
	Se ejecuta automaticamante cuando la excepcion no es capturada, 
	antes de interrumpir la ejecucion del programa.
	*Parametros: nada.
	*Excepciones: nada.
	*Retorno: nada.
	"""
	def __str__(self):
		print "",self.msg
