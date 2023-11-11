from datetime import datetime
from ..classes.Cliente import clientes
from ..classes.CambioEstado import cambios_estado
from ..classes.RespuestaDeCliente import respuestasSeleccionadas
from ..classes.GestorPersistencia import GestorPersistencia;
from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey, Boolean, ARRAY
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class Llamada(Base):

    "Es necesario que estos atributos se inicien aquí y no dentro del constructor para que sqlalchemy pueda acceder a ellos"
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

    # def __init__(self):
    #     self.__descripcionOperador = ""
    #     self.__detalleAccionRequerida = ""
    #     self.__duracion = 0
    #     self.__encuestaEnviada = False
    #     self.__observacionAuditor = ""
    #     self.__respuestasDeEncuesta = None
    #     self.__cambioEstado = None
    #     self.fechaHoraInicio = ''  # formato 03-06-23 dd-mm-aa
    #     self.__cliente = None

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


# Crear una lista de objetos de clase Llamada
llamadas = [
    Llamada(),
    Llamada(),
    Llamada()
]

# Acceder a los atributos de un objeto de la lista
llamada1 = llamadas[0]
llamada1.descripcionOperador = "Descripción del operador 1"
llamada1.detalleAccionRequerida = "Detalle de la acción requerida 1"
llamada1.setDuracion(120)
llamada1.setEncuestaEnviada(True)
llamada1.observacionAuditor = "Observación del auditor 1"
llamada1.setFechaHoraInicio("6/7/23")
llamada1.setCliente(clientes[0])
llamada1.setCambioEstado([cambios_estado[0], cambios_estado[1], cambios_estado[2]])
llamada1.setRespuestasDeEncuesta([respuestasSeleccionadas[0], respuestasSeleccionadas[1], respuestasSeleccionadas[2]])


# Acceder a los atributos de otro objeto de la lista
llamada2 = llamadas[1]
llamada2.setDescripcionOperador("Descripción del operador 2")
llamada2.setDetalleAccionRequerida("Detalle de la acción requerida 2")
llamada2.setDuracion(180)
llamada2.setEncuestaEnviada(True)
llamada2.setObservacionAuditor("Observación del auditor 2")
llamada2.setFechaHoraInicio("8/7/23")
llamada2.setCliente(clientes[1])
llamada2.setCambioEstado([cambios_estado[3], cambios_estado[4]])
llamada2.setRespuestasDeEncuesta([respuestasSeleccionadas[3], respuestasSeleccionadas[4], respuestasSeleccionadas[5]])

# Acceder a los atributos de otro objeto de la lista
llamada3 = llamadas[2]
llamada3.descripcionOperador = "Descripción del operador 3"
llamada3.detalleAccionRequerida = "Detalle de la acción requerida 3"
llamada3.setDuracion(90)
llamada3.setEncuestaEnviada(True)
llamada3.observacionAuditor = "Observación del auditor 3"
llamada3.setFechaHoraInicio("9/7/23")
llamada3.setCliente(clientes[2])
llamada3.setCambioEstado([cambios_estado[5], cambios_estado[6]])
llamada3.setRespuestasDeEncuesta([respuestasSeleccionadas[6], respuestasSeleccionadas[7], respuestasSeleccionadas[8]])
