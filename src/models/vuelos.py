# -*- coding: utf-8 -*-
from abstractmodel import AbstractModel

from PyQt4 import QtCore

class Vuelos(AbstractModel):
    def __init__(self, conn):
        super(Vuelos, self).__init__(conn)

        self.tableName = "vuelos"
        self.id = "id"

        
# CREATE TABLE vuelos (
    # id                  VARCHAR(30) NOT NULL,
    # aeropuerto_salida   VARCHAR(30) NOT NULL,
    # aeropuerto_llegada  VARCHAR(30) NOT NULL,
    # FOREIGN KEY (aeropuerto_salida)  REFERENCES aeropuertos (codigo),
    # FOREIGN KEY (aeropuerto_llegada) REFERENCES aeropuertos (codigo),
    # PRIMARY KEY (id)
# ) ENGINE=InnoDB; 
        
    def insert(self, id, salida, llegada):
        self.conn.update("insert into "+self.tableName+" (id, aeropuerto_salida, aeropuerto_llegada) values ('"+id+"', '"+salida+"', '"+llegada+"')")
    
    def update(self, oldid, newid, salida, llegada):
        self.conn.update("update "+self.tableName+" set id='"+newid+"', aeropuerto_salida='"+salida+"', aeropuerto_llegada='"+llegada+"' where id='"+oldid+"'")