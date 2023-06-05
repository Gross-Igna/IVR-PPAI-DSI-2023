import sqlite3

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
c.execute("""INSERT INTO RespuestaDeCliente VALUES ('2023-05-02 03:00:00')""")
c.execute("""INSERT INTO RespuestaDeCliente VALUES ('2023-06-02 03:00:00')""")
c.execute("""INSERT INTO RespuestaDeCliente VALUES ('2023-07-02 03:00:00')""")
c.execute("""INSERT INTO Cliente VALUES (39800000, 'Ana Lana', 351405560)""")
c.execute("""INSERT INTO Cliente VALUES (40000000, 'Facundo Quinteros', 351000000)""")
c.execute("""INSERT INTO Cliente VALUES (40000001, 'Esteban Quito', 351111111)""")
c.execute("""INSERT INTO Cliente VALUES (42000000, 'Maria Emilia', 351525141)""")

# Commit the changes
conn.commit()

# Close th
# Commit los cambios
conn.commit()

# Cerrar la conexión
conn.close()


conn.close()