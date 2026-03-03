CREATE DATABASE saasia;

USE saasia;

CREATE TABLE clientes (
	id INT(255),
  nombre VARCHAR(255),
  apellidos VARCHAR(255),
  email VARCHAR(255),
  poblacion VARCHAR(255),
  fecha_de_nacimiento DATE()
);