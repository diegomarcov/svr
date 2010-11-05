USE svr;

#vuelos
insert into vuelos (id, aeropuerto_salida, aeropuerto_llegada) values ("vuelo 1", "TXL", "THF");
insert into vuelos (id, aeropuerto_salida, aeropuerto_llegada) values ("vuelo 2", "SXF", "CGN");
insert into vuelos (id, aeropuerto_salida, aeropuerto_llegada) values ("vuelo 3", "DUS", "FRA");
insert into vuelos (id, aeropuerto_salida, aeropuerto_llegada) values ("vuelo 4", "HAM", "MUC");

#salidas
insert into salidas (vuelo, diahora_sale, diahora_llega, estado) values ("vuelo 1", '2010-01-01 01:01:01', '2010-01-01 02:02:02', 'Demorado');
insert into salidas (vuelo, diahora_sale, diahora_llega, estado) values ("vuelo 1", '2010-02-02 02:02:02', '2010-02-02 03:03:03', 'Cancelado');

insert into salidas (vuelo, diahora_sale, diahora_llega, estado) values ("vuelo 2", '2010-01-01 01:01:01', '2010-01-01 02:02:02', 'En transito');
insert into salidas (vuelo, diahora_sale, diahora_llega, estado) values ("vuelo 2", '2010-02-02 02:02:02', '2010-02-02 03:03:03', 'Abordando');

insert into salidas (vuelo, diahora_sale, diahora_llega, estado) values ("vuelo 3", '2010-01-01 01:01:01', '2010-01-01 02:02:02', 'A tiempo');
insert into salidas (vuelo, diahora_sale, diahora_llega, estado) values ("vuelo 3", '2010-02-02 02:02:02', '2010-02-02 03:03:03', 'Demorado');

insert into salidas (vuelo, diahora_sale, diahora_llega, estado) values ("vuelo 4", '2010-01-01 01:01:01', '2010-01-01 02:02:02', 'Cancelado');
insert into salidas (vuelo, diahora_sale, diahora_llega, estado) values ("vuelo 4", '2010-02-02 02:02:02', '2010-02-02 03:03:03', 'Abordando');

#reservas
insert into reservas (numero, fecha_realizacion, vencimiento, estado, precio, forma_de_pago, doc_nro, nombre_cliente, pasaporte, vuelo, diahora_sale) values (1, '2010-01-01', '2011-02-02', 'Finalizada', 1000.00, 'Efectivo', 1234, 'juan', 'UTF 8', 'vuelo 1', '2010-01-01 01:01:01');
insert into reservas (numero, fecha_realizacion, vencimiento, estado, precio, forma_de_pago, doc_nro, nombre_cliente, pasaporte, vuelo, diahora_sale) values (2, '2010-01-01', '2011-02-02', 'Finalizada', 1000.00, 'Efectivo', 1234, 'juan', 'UTF 8', 'vuelo 2', '2010-01-01 01:01:01');
insert into reservas (numero, fecha_realizacion, vencimiento, estado, precio, forma_de_pago, doc_nro, nombre_cliente, pasaporte, vuelo, diahora_sale) values (3, '2010-01-01', '2011-02-02', 'Pendiente', 1000.00, 'Efectivo', 1234, 'juan', 'UTF 8', 'vuelo 3', '2010-01-01 01:01:01');
insert into reservas (numero, fecha_realizacion, vencimiento, estado, precio, forma_de_pago, doc_nro, nombre_cliente, pasaporte, vuelo, diahora_sale) values (4, '2010-01-01', '2011-02-02', 'Pendiente', 1000.00, 'Efectivo', 1234, 'juan', 'UTF 8', 'vuelo 4', '2010-01-01 01:01:01');
insert into reservas (numero, fecha_realizacion, vencimiento, estado, precio, forma_de_pago, doc_nro, nombre_cliente, pasaporte, vuelo, diahora_sale) values (5, '2010-01-01', '2011-02-02', 'Vencida', 1000.00, 'Efectivo', 1234, 'juan', 'UTF 8', 'vuelo 1', '2010-01-01 01:01:01');
insert into reservas (numero, fecha_realizacion, vencimiento, estado, precio, forma_de_pago, doc_nro, nombre_cliente, pasaporte, vuelo, diahora_sale) values (6, '2010-01-01', '2011-02-02', 'Vencida', 1000.00, 'Efectivo', 1234, 'juan', 'UTF 8', 'vuelo 2', '2010-01-01 01:01:01');