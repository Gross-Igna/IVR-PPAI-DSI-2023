import sqlite3
## Este archivo crea una nueva base de datos en caso de que no exista, y inserta datos de prueba.

conn = sqlite3.connect('bdIvr.db')
c = conn.cursor()

# Crear tabla RespuestaDeCliente
c.execute("""
    CREATE TABLE IF NOT EXISTS RespuestaDeCliente (
        fechaEncuesta DATETIME
    )
""")

# Crear tabla Cliente
c.execute("""
    CREATE TABLE IF NOT EXISTS Cliente (
        dni INTEGER NOT NULL,
        nombreCompleto TEXT,
        nroCelular INTEGER,
        PRIMARY KEY(dni)
    )
""")

# Crear tabla Pregunta
c.execute("""
    CREATE TABLE IF NOT EXISTS Pregunta (
        idPregunta INTEGER NOT NULL,
        descripcion TEXT,
        PRIMARY KEY(idPregunta)
    )
""")

# Crear tabla RespuestaPosible
c.execute("""
    CREATE TABLE IF NOT EXISTS RespuestaPosible (
        idRespuestaPosible INTEGER NOT NULL,
        descripcion TEXT,
        valor INTEGER,
        PRIMARY KEY(idRespuestaPosible)
    )
""")

# Crear tabla Llamada
c.execute("""
    CREATE TABLE IF NOT EXISTS Llamada (
        idLlamada INTEGER NOT NULL,
        descripcion TEXT,
        detalleAccionRequerida TEXT,
        duracion TEXT,
        encuestaEnviada TEXT,
        cambioEstado TEXT,
        respuestaDeEncuesta INTEGER,
        cliente INTEGER,
        fechaHoraInicio DATETIME,
        FOREIGN KEY(cliente) REFERENCES Cliente(dni),
        PRIMARY KEY(idLlamada)
    )
""")

# Crear tabla Estado
c.execute("""
    CREATE TABLE IF NOT EXISTS Estado (
        idEstado INTEGER NOT NULL,
        nombre TEXT,
        PRIMARY KEY(idEstado)
    )
""")

# Crear tabla Encuesta
c.execute("""
    CREATE TABLE IF NOT EXISTS Encuesta (
        idEncuesta INTEGER,
        descripcion TEXT,
        fechaFinVigencia DATETIME NOT NULL,
        pregunta INTEGER NOT NULL,
        FOREIGN KEY(pregunta) REFERENCES Pregunta(idPregunta),
        PRIMARY KEY(idEncuesta)
    )
""")

# Crear tabla CambioEstado
c.execute("""
    CREATE TABLE IF NOT EXISTS CambioEstado (
        idCambioEstado INTEGER NOT NULL,
        fechaHoraInicio DATETIME,
        estado INTEGER NOT NULL,
        FOREIGN KEY(estado) REFERENCES Estado(idEstado),
        PRIMARY KEY(idCambioEstado)
    )
""")
# Insert data
# c.execute("""INSERT INTO RespuestaDeCliente VALUES ('2023-05-02 03:00:00')""")
# c.execute("""INSERT INTO RespuestaDeCliente VALUES ('2023-06-02 03:00:00')""")
# c.execute("""INSERT INTO RespuestaDeCliente VALUES ('2023-07-02 03:00:00')""")
# c.execute("""INSERT INTO Cliente VALUES (39800000, 'Ana Lana', 351405560)""")
# c.execute("""INSERT INTO Cliente VALUES (40000000, 'Facundo Quinteros', 351000000)""")
# c.execute("""INSERT INTO Cliente VALUES (40000001, 'Esteban Quito', 351111111)""")
# c.execute("""INSERT INTO Cliente VALUES (42000000, 'Maria Emilia', 351525141)""")

# Insertar Llamadas
c.execute("""INSERT INTO "llamada" VALUES (1, 'llamada de ejemplo', 'detalle accion requerida', '120', 'encuestaEnviada', 'cambioEstado', 1, 16, '2021-01-15 09:30:00')""")
c.execute("""INSERT INTO "llamada" VALUES (2, 'llamada importante', 'atender problema urgente', '180', 'encuestaPendiente', 'cambioEstado', 2, 24, '2021-03-10 14:45:00')""")
c.execute("""INSERT INTO "llamada" VALUES (3, 'llamada de seguimiento', 'confirmar datos actualizados', '90', 'encuestaEnviada', 'cambioEstado', 3, 8, '2022-07-20 11:00:00')""")
c.execute("""INSERT INTO "llamada" VALUES (4, 'llamada de soporte', 'resolver incidencia técnica', '60', 'encuestaPendiente', 'cambioEstado', 4, 12, '2023-02-05 16:20:00')""")
c.execute("""INSERT INTO "llamada" VALUES (5, 'llamada informativa', 'brindar actualizaciones del proyecto', '150', 'encuestaEnviada', 'cambioEstado', 5, 20, '2021-05-12 10:15:00')""")
c.execute("""INSERT INTO "llamada" VALUES (6, 'llamada de seguimiento', 'verificar avance del cliente', '120', 'encuestaPendiente', 'cambioEstado', 6, 10, '2022-09-30 15:45:00')""")
c.execute("""INSERT INTO "llamada" VALUES (7, 'llamada de soporte', 'solucionar problema de conexión', '90', 'encuestaEnviada', 'cambioEstado', 7, 14, '2021-07-05 11:30:00')""")
c.execute("""INSERT INTO "llamada" VALUES (8, 'llamada importante', 'discutir cambios en el proyecto', '180', 'encuestaPendiente', 'cambioEstado', 8, 18, '2023-04-18 09:00:00')""")
c.execute("""INSERT INTO "llamada" VALUES (9, 'llamada de seguimiento', 'confirmar fecha de entrega', '120', 'encuestaEnviada', 'cambioEstado', 9, 8, '2022-06-12 13:20:00')""")
c.execute("""INSERT INTO "llamada" VALUES (10, 'llamada informativa', 'brindar actualizaciones del proyecto', '90', 'encuestaPendiente', 'cambioEstado', 10, 16, '2021-11-28 14:10:00')""")
c.execute("""INSERT INTO "llamada" VALUES (11, 'llamada de soporte', 'resolver incidencia técnica', '60', 'encuestaEnviada', 'cambioEstado', 11, 12, '2023-03-09 17:30:00')""")
c.execute("""INSERT INTO "llamada" VALUES (12, 'llamada importante', 'atender problema urgente', '150', 'encuestaPendiente', 'cambioEstado', 12, 24, '2021-02-14 11:45:00')""")
c.execute("""INSERT INTO "llamada" VALUES (13, 'llamada de seguimiento', 'confirmar datos actualizados', '120', 'encuestaEnviada', 'cambioEstado', 13, 8, '2022-08-20 15:30:00')""")
c.execute("""INSERT INTO "llamada" VALUES (14, 'llamada de soporte', 'resolver incidencia técnica', '90', 'encuestaPendiente', 'cambioEstado', 14, 12, '2023-01-25 09:40:00')""")
c.execute("""INSERT INTO "llamada" VALUES (15, 'llamada informativa', 'brindar actualizaciones del proyecto', '180', 'encuestaEnviada', 'cambioEstado', 15, 20, '2021-06-18 13:15:00')""")
c.execute("""INSERT INTO "llamada" VALUES (16, 'llamada de seguimiento', 'verificar avance del cliente', '120', 'encuestaPendiente', 'cambioEstado', 16, 10, '2022-10-10 10:45:00')""")
c.execute("""INSERT INTO "llamada" VALUES (17, 'llamada de soporte', 'solucionar problema de conexión', '90', 'encuestaEnviada', 'cambioEstado', 17, 14, '2021-08-25 16:20:00')""")
c.execute("""INSERT INTO "llamada" VALUES (18, 'llamada importante', 'discutir cambios en el proyecto', '120', 'encuestaPendiente', 'cambioEstado', 18, 18, '2023-05-05 11:10:00')""")
c.execute("""INSERT INTO "llamada" VALUES (19, 'llamada de seguimiento', 'confirmar fecha de entrega', '90', 'encuestaEnviada', 'cambioEstado', 19, 8, '2022-07-30 12:40:00')""")
c.execute("""INSERT INTO "llamada" VALUES (20, 'llamada informativa', 'brindar actualizaciones del proyecto', '150', 'encuestaPendiente', 'cambioEstado', 20, 16, '2021-12-05 15:50:00')""")
c.execute("""INSERT INTO "llamada" VALUES (21, 'llamada de soporte', 'resolver incidencia técnica', '120', 'encuestaEnviada', 'cambioEstado', 21, 12, '2023-03-15 10:30:00')""")

# Commit the changes
conn.commit()

# Close th
# Commit los cambios
conn.commit()

# Cerrar la conexión
conn.close()


conn.close()