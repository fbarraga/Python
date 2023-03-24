
CREATE DATABASE agenda;  CREATE DATABASE
CREATE USER usag WITH PASSWORD 'abcde';  
GRANT ALL PRIVILEGES ON DATABASE agenda TO usag;

CREATE TABLE persona (dni VARCHAR(9) PRIMARY KEY, data_naixement DATE, nom TEXT, cognoms TEXT);  
CREATE TABLE telefon (id SERIAL, id_persona VARCHAR(9) REFERENCES persona(dni), numero VARCHAR(9)); 
CREATE TABLE provincia (id VARCHAR(2) PRIMARY KEY, nom TEXT);
CREATE TABLE codi_postal (num VARCHAR(5) PRIMARY KEY, poblacio TEXT);
CREATE TABLE adreca (id SERIAL, id_persona VARCHAR(9) REFERENCES persona(dni), descripcio TEXT, cp  VARCHAR(5) REFERENCES codi_postal(num));

INSERT INTO provincia VALUES ('08', 'Barcelona'),('17', 'Girona'), ('25', 'Lleida'), ('43', 'Tarragona');
INSERT INTO codi_postal VALUES ('08370', 'Calella'), ('08380', 'Malgrat de Mar'), ('17300', 'Blanes');
INSERT INTO persona VALUES ('43564376j', '1977-09-11', 'Joan', 'Garcia Mas'), ('37897123m', '1980-07-21','Pere', 'Perez Suy');
INSERT INTO telefon(id_persona,numero) VALUES ('43564376j','972335746'), ('43564376j','650573882'),  ('37897123m','666435216');
INSERT INTO adreca(id_persona,descripcio,cp) VALUES ('43564376j', 'Carrer Ample 10, 1-1', '17300'),  ('37897123m', 'Carrer de la Industria 9, 2-3', '08370');
