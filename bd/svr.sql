# DEFINICION DE BASES DE DATOS

DROP DATABASE IF EXISTS svr;

CREATE DATABASE svr;

USE svr;

# DEFINICION DE TABLAS 

CREATE TABLE aeropuertos (
	codigo    VARCHAR(3) NOT NULL,
	nombre    VARCHAR(45) NOT NULL,
	pais      VARCHAR(45) NOT NULL,
	ciudad    VARCHAR(45) NOT NULL,
	PRIMARY KEY (codigo)
) ENGINE=InnoDB;


CREATE TABLE vuelos (
	id					VARCHAR(30) NOT NULL,
	aeropuerto_salida	VARCHAR(30) NOT NULL,
	aeropuerto_llegada  VARCHAR(30) NOT NULL,
	FOREIGN KEY (aeropuerto_salida)  REFERENCES aeropuertos (codigo),
	FOREIGN KEY (aeropuerto_llegada) REFERENCES aeropuertos (codigo),
	PRIMARY KEY (id)
) ENGINE=InnoDB; 

CREATE TABLE salidas (
	vuelo        	VARCHAR(30) NOT NULL,
	diahora_sale    TIMESTAMP NOT NULL,
	diahora_llega   TIMESTAMP NOT NULL,
	estado			ENUM ('Demorado', 'Cancelado', 'En transito', 'Abordando', 'A tiempo'),
	FOREIGN KEY (vuelo)        REFERENCES vuelos (id),
	PRIMARY KEY (vuelo, diahora_sale)
) ENGINE=InnoDB;


CREATE TABLE reservas (
	numero      		INT(15) UNSIGNED AUTO_INCREMENT,
	fecha_realizacion   DATE NOT NULL,
	vencimiento 		DATE NOT NULL,
	estado      		ENUM ('Finalizada','Pendiente', 'Confirmada', 'Vencida', 'Cancelada'),
	precio				DECIMAL(10,2) NOT NULL,
	forma_de_pago		ENUM ('Efectivo', 'Tarjeta', 'Cheque'),
	doc_nro     		INT(10) UNSIGNED NOT NULL,
	nombre_cliente		VARCHAR(45) NOT NULL,
	pasaporte			VARCHAR(45) NOT NULL,
	vuelo				VARCHAR(30) NOT NULL,
	diahora_sale		TIMESTAMP NOT NULL,
	FOREIGN KEY (vuelo, diahora_sale)        REFERENCES salidas (vuelo, diahora_sale),
	PRIMARY KEY (numero)
) ENGINE=InnoDB;

# DEFINICION DE USUARIOS
GRANT ALL PRIVILEGES ON svr.* TO admin@localhost IDENTIFIED BY 'admin' WITH GRANT OPTION;

CREATE USER 'empleado'@localhost IDENTIFIED BY 'empleado';
GRANT SELECT ON svr.*          TO 'empleado';
GRANT INSERT ON svr.*          TO 'empleado';
