from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class Llamada(Base):
    __tablename__ = 'Llamada'
    idLlamada = Column(Integer, primary_key=True)
    descripcion = Column(String)
    detalleAccionRequerida = Column(String)
    duracion = Column(String)
    encuestaEnviada = Column(String)
    cambioEstado = Column(String)
    respuestaDeEncuesta = Column(Integer)
    cliente = Column(Integer, ForeignKey('Cliente.dni'))
    cliente_rel = relationship("Cliente")


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
