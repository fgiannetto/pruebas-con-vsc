CREATE DATABASE IF NOT EXISTS master_python;
use master_python;

CREATE TABLE usuarios(
id          int(25) auto_increment NOT NULL,
nombre      VARCHAR(100),
apellidos   VARCHAR(255),
email       varchar(255) NOT NULL,
PASSWORD    VARCHAR (255) NOT NULL,
fecha       DATE NOT NULL,
CONSTRAINT  pk_usuarios PRIMARY KEY(id),
CONSTRAINT  uq_email UNIQUE(email)
) ENGINE = InnoDb;

CREATE TABLE notas(
id          int(25) auto_increment NOT NULL,
usuario_id  int(25) NOT NULL,
titulo      varchar(255) NOT NULL,
descripcion MEDIUMTEXT,
fecha       DATE NOT NULL,
CONSTRAINT  pk_notas PRIMARY KEY(id),
CONSTRAINT  fk_nota_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
) ENGINE = InnoDb;