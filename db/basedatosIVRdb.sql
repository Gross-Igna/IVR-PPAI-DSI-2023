BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "RespuestaDeCliente" (
	"fechaEncuesta"	DATETIME
);
CREATE TABLE IF NOT EXISTS "Cliente" (
	"dni"	INTEGER NOT NULL,
	"nombreCompleto"	TEXT,
	"nroCelular"	INTEGER,
	PRIMARY KEY("dni")
);
CREATE TABLE IF NOT EXISTS "Pregunta" (
	"idPregunta"	INTEGER NOT NULL,
	"descripcion"	TEXT,
	PRIMARY KEY("idPregunta")
);
CREATE TABLE IF NOT EXISTS "RespuestaPosible" (
	"idRespuestaPosible"	INTEGER NOT NULL,
	"descripcion"	TEXT,
	"valor"	INTEGER,
	PRIMARY KEY("idRespuestaPosible")
);
CREATE TABLE IF NOT EXISTS "Llamada" (
	"idLlamada"	INTEGER NOT NULL,
	"descripcion"	TEXT,
	"detalleAccionRequerida"	TEXT,
	"duracion"	TEXT,
	"encuestaEnviada"	TEXT,
	"cambioEstado"	TEXT,
	"respuestaDeEncuesta"	INTEGER,
	"cliente"	INTEGER,
	FOREIGN KEY("cliente") REFERENCES "Cliente",
	PRIMARY KEY("idLlamada")
);
CREATE TABLE IF NOT EXISTS "Estado" (
	"idEstado"	INTEGER NOT NULL,
	"nombre"	TEXT,
	PRIMARY KEY("idEstado")
);
CREATE TABLE IF NOT EXISTS "Encuesta" (
	"idEncuesta"	INTEGER,
	"descripcion"	TEXT,
	"fechaFinVigencia"	DATETIME NOT NULL,
	"pregunta"	INTEGER NOT NULL,
	FOREIGN KEY("pregunta") REFERENCES "Pregunta"("idPregunta"),
	PRIMARY KEY("idEncuesta")
);
CREATE TABLE IF NOT EXISTS "CambioEstado" (
	"idCambioEstado"	INTEGER NOT NULL,
	"fechaHoraInicio"	DATETIME,
	"estado"	INTEGER NOT NULL,
	FOREIGN KEY("estado") REFERENCES "Estado"("idEstado"),
	PRIMARY KEY("idCambioEstado")
);
INSERT INTO "RespuestaDeCliente" VALUES ('''2023-05-02 03:00:00''');
INSERT INTO "RespuestaDeCliente" VALUES ('''2023-06-02 03:00:00''');
INSERT INTO "RespuestaDeCliente" VALUES ('''2023-07-02 03:00:00''');
INSERT INTO "Cliente" VALUES (39800000,'Ana Lana',351405560);
INSERT INTO "Cliente" VALUES (40000000,'Facundo Quinteros',351000000);
INSERT INTO "Cliente" VALUES (40000001,'Esteban Quito',351111111);
INSERT INTO "Cliente" VALUES (42000000,'Maria Emilia',351525141);
COMMIT;
