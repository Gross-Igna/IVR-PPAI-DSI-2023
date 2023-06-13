from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

Base = declarative_base()


class Llamada(Base):
    __tablename__ = 'llamada'
    idLlamada = Column(Integer, primary_key=True)
    descripcion = Column(String)
    detalleAccionRequerida = Column(String)
    duracion = Column(String)
    encuestaEnviada = Column(String)
    cambioEstado = Column(String)
    respuestaDeEncuesta = Column(Integer)
    cliente = Column(Integer, ForeignKey('Cliente.dni'))
    fechaHoraInicio = Column(DateTime)
    cliente_rel = relationship("Cliente")

    def esDePeriodo(self, fechaInicio, fechaFin):
        fecha_inicio = datetime.strptime(fechaInicio, "%d/%m/%y").date()
        fecha_fin = datetime.strptime(fechaFin, "%d/%m/%y").date()
        fecha_llamada = self.fechaHoraInicio.date()
        if fecha_inicio <= fecha_llamada <= fecha_fin:
            tiene_encuesta = self.tieneEncuestaRespondida()
            if tiene_encuesta:
                return True

    def getDescripcionOperador(self):
        return self.descripcionOperador

    def setDescripcionOperador(self, descripcion):
        self.descripcionOperador = descripcion

    def getDetalleAccionRequerida(self):
        return self.detalleAccionRequerida

    def setDetalleAccionRequerida(self, detalle):
        self.detalleAccionRequerida = detalle

    def getDuracion(self):
        return self.duracion

    def setDuracion(self, duracion):
        self.duracion = duracion

    def getEncuestaEnviada(self):
        return self.encuestaEnviada

    def setEncuestaEnviada(self, encuesta):
        self.encuestaEnviada = encuesta

    def getObservacionAuditor(self):
        return self.observacionAuditor

    def setObservacionAuditor(self, observacion):
        self.observacionAuditor = observacion

    def getRespuestasDeEncuesta(self):
        return self.respuestasDeEncuesta

    def setRespuestasDeEncuesta(self, respuestas):
        self.respuestasDeEncuesta = respuestas

    def getCambioEstado(self):
        return self.cambioEstado

    def setCambioEstado(self, cambio):
        self.cambioEstado = cambio

    def getFechaHoraInicio(self):
        return self.fechaHoraInicio

    def setFechaHoraInicio(self, fecha):
        self.fechaHoraInicio = fecha

    def getCliente(self):
        return self.cliente

    def setCliente(self, cliente):
        self.cliente = cliente

    def tieneEncuestaRespondida(self):
        return self.encuestaEnviada

    def mostrarLlamada(self):
        cliente = self.getCliente()
        nombre_cli = cliente.getNombre()
        duracion = self.getDuracion()
        nombre_est = ""

        cambios = self.getCambioEstado()
        for i in cambios:
            es_ultimo = i.esUltimoCambioEstado()
            if es_ultimo:
                estado = i.getEstado()
                nombre_est = estado.getNombre()

        respuestas = self.getRespuestasDeEncuesta()
        descripciones = []
        for i in respuestas:
            desc = i.getDescripcionRta()
            descripciones.append(desc)

        return [nombre_cli, duracion, nombre_est, descripciones]

    def buscarFechaEncuesta(self):
        respuestas = self.getRespuestasDeEncuesta()
        fecha_encuesta = respuestas[0].getFechaEncuesta()
        return fecha_encuesta

class RespuestaDeCliente(Base):
    __tablename__ = 'RespuestaDeCliente'
    fechaEncuesta = Column(DateTime, primary_key=True)


class Cliente(Base):
    __tablename__ = 'Cliente'
    dni = Column(Integer, primary_key=True)
    nombreCompleto = Column(String)
    nroCelular = Column(Integer)


class Pregunta(Base):
    __tablename__ = 'Pregunta'
    idPregunta = Column(Integer, primary_key=True)
    descripcion = Column(String)


class RespuestaPosible(Base):
    __tablename__ = 'RespuestaPosible'
    idRespuestaPosible = Column(Integer, primary_key=True)
    descripcion = Column(String)
    valor = Column(Integer)


class Estado(Base):
    __tablename__ = 'Estado'
    idEstado = Column(Integer, primary_key=True)
    nombre = Column(String)


class Encuesta(Base):
    __tablename__ = 'Encuesta'
    idEncuesta = Column(Integer, primary_key=True)
    descripcion = Column(String)
    fechaFinVigencia = Column(DateTime, nullable=False)
    pregunta = Column(Integer, ForeignKey('Pregunta.idPregunta'))
    pregunta_rel = relationship("Pregunta")


class CambioEstado(Base):
    __tablename__ = 'CambioEstado'
    idCambioEstado = Column(Integer, primary_key=True)
    fechaHoraInicio = Column(DateTime)
    estado = Column(Integer, ForeignKey('Estado.idEstado'))
    estado_rel = relationship("Estado")
