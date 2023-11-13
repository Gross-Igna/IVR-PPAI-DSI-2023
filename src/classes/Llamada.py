from datetime import datetime
from ..classes.RespuestaDeCliente import respuestasSeleccionadas
from ..classes.GestorPersistencia import GestorPersistencia
from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey, Boolean, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from ..database.repositorioDeClientes import RepositorioDeClientes
from ..database.repositorioDeCambiosDeEstado import RepositorioDeCambiosDeEstado
from ..database.repositorioDeEstados import RepositorioDeEstados

Base = declarative_base()
class Llamada(Base):

    __tablename__ = 'llamadas'
    id = Column(Integer, Sequence('llamadas_id_seq'), primary_key=True)
    descripcionOperador = Column(String)
    detalleAccionRequerida = Column(String)
    duracion = Column(Integer)
    encuestaEnviada = Column(Boolean)
    observacionAuditor = Column(String)
    respuestasDeEncuesta = Column(ARRAY(Integer))
    cambioEstado = Column(Integer)
    fechaHoraInicio = Column(String)
    cliente = Column(Integer)

    def __init__(self, descripcionOperador, detalleAccionRequerida, duracion, encuestaEnviada,
                 observacionAuditor, respuestasDeEncuesta, cambioEstado, fechaHoraInicio, cliente):
        self.descripcionOperador = descripcionOperador
        self.detalleAccionRequerida = detalleAccionRequerida
        self.duracion = duracion
        self.encuestaEnviada = encuestaEnviada
        self.observacionAuditor = observacionAuditor
        self.respuestasDeEncuesta = respuestasSeleccionadas
        self.cambioEstado = cambioEstado
        self.fechaHoraInicio = fechaHoraInicio
        self.cliente = cliente

    """Getters y Setters"""
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
    
    def setCliente(self,cliente):
        self.cliente = cliente

    def esDePeriodo(self, fechaInicio , fechaFin):
        fecha_inicio = datetime.strptime(fechaInicio, "%d/%m/%y").date()
        fecha_fin = datetime.strptime(fechaFin, "%d/%m/%y").date()
        fecha_llamada = datetime.strptime(self.fechaHoraInicio, "%d/%m/%y").date()
        if fecha_inicio <= fecha_llamada <= fecha_fin:
            return True

    def tieneEncuestaRespondida(self):
        return self.encuestaEnviada

    def mostrarLlamada(self):
        repositorioDeClientes = RepositorioDeClientes()
        cliente = repositorioDeClientes.buscarPorDni(self.getCliente())
        nombre_cli = cliente.getNombre()
        duracion = self.getDuracion()
        nombre_est = ""

        cambios = self.getCambioEstado()
        repositorioDeCambiosDeEstado = RepositorioDeCambiosDeEstado()
        cambios_estado = repositorioDeCambiosDeEstado.obtenerTodos()
        print(cambios_estado)
        for i in cambios_estado:
            print(i)
            if i.getLlamada_id() != self.id:
                continue
            es_ultimo = i.esUltimoCambioEstado()
            if es_ultimo:
                id_estado = i.getEstado_id()
                repositorioDeEstados = RepositorioDeEstados()
                nombre_est = repositorioDeEstados.obtenerPorId(id_estado).getNombre()

        respuestas = self.getRespuestasDeEncuesta()
        descripciones = []
        for i in respuestasSeleccionadas:
            desc = i.getDescripcionRta()
            descripciones.append(desc)

        return [nombre_cli, duracion, nombre_est, descripciones]

    def buscarFechaEncuesta(self):
        respuestas = respuestasSeleccionadas
        fecha_encuesta = respuestas[0].getFechaEncuesta()
        return fecha_encuesta