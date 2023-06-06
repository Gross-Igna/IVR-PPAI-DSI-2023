from datetime import datetime

from ..classes.Cliente import clientes
from ..classes.CambioEstado import cambios_estado
from ..classes.RespuestaDelCliente import respuestasSeleccionadas

class Llamada:
    """En el constructor se inicializan los atributos"""
    """El doble guión es para encapsular el atributo (name mangling)"""
    def __init__(self):
        self.__descripcionOperador = ""
        self.__detalleAccionRequerida = ""
        self.__duracion = 0
        self.__encuestaEnviada = False
        self.__observacionAuditor = ""
        self.__respuestasDeEncuesta = None
        self.__cambioEstado = None
        self.__fechaHoraInicio = ''  # formato 2023-06-03
        self.__cliente = None

    """Getters y Setters"""
    def getDescripcionOperador(self):
        return self.__descripcionOperador

    def setDescripcionOperador(self, descripcion):
        self.__descripcionOperador = descripcion

    def getDetalleAccionRequerida(self):
        return self.__detalleAccionRequerida

    def setDetalleAccionRequerida(self, detalle):
        self.__detalleAccionRequerida = detalle

    def getDuracion(self):
        return self.__duracion

    def setDuracion(self, duracion):
        self.__duracion = duracion

    def getEncuestaEnviada(self):
        return self.__encuestaEnviada

    def setEncuestaEnviada(self, encuesta):
        self.__encuestaEnviada = encuesta

    def getObservacionAuditor(self):
        return self.__observacionAuditor

    def setObservacionAuditor(self, observacion):
        self.__observacionAuditor = observacion

    def getRespuestasDeEncuesta(self):
        return self.__respuestasDeEncuesta

    def setRespuestasDeEncuesta(self, respuestas):
        self.__respuestasDeEncuesta = respuestas

    def getCambioEstado(self):
        return self.__cambioEstado

    def setCambioEstado(self, cambio):
        self.__cambioEstado = cambio

    def getFechaHoraInicio(self):
        return self.__fechaHoraInicio

    def setFechaHoraInicio(self, fecha):
        self.__fechaHoraInicio = fecha

    def getCliente(self):
        return self.__cliente
    
    def setCliente(self,cliente):
        self.__cliente = cliente

    def esDePeriodo(self, fechaInicio , fechaFin):
        fecha_inicio = datetime.strptime(fechaInicio, "%Y-%m-%d %H:%M:%S").date()
        fecha_fin = datetime.strptime(fechaFin, "%Y-%m-%d %H:%M:%S").date()
        fecha_llamada = datetime.strptime(self.__fechaHoraInicio, "%Y-%m-%d %H:%M:%S").date()
        if fecha_inicio <= fecha_llamada <= fecha_fin:
            tiene_encuesta = self.tieneEncuestaRespondida()
            if tiene_encuesta:
                return True

    def tieneEncuestaRespondida(self):
        return self.__encuestaEnviada

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
llamada1.duracion = 120
llamada1.encuestaEnviada = True
llamada1.observacionAuditor = "Observación del auditor 1"
llamada1.fechaHoraInicio = "2023-06-03 10:00:00"
llamada1.cliente = clientes[0]
llamada1.cambios_estado = [cambios_estado[0], cambios_estado[1], cambios_estado[2]]
llamada1.respuestasDeEncuesta = [respuestasSeleccionadas[0],respuestasSeleccionadas[1],respuestasSeleccionadas[2]]


# Acceder a los atributos de otro objeto de la lista
llamada2 = llamadas[1]
llamada2.descripcionOperador = "Descripción del operador 2"
llamada2.detalleAccionRequerida = "Detalle de la acción requerida 2"
llamada2.duracion = 180
llamada2.encuestaEnviada = True
llamada2.observacionAuditor = "Observación del auditor 2"
llamada2.fechaHoraInicio = "2023-06-03 12:00:00"
llamada2.cliente = clientes[1]
llamada2.cambios_estado = [cambios_estado[3], cambios_estado[4]]
llamada1.respuestasDeEncuesta = [respuestasSeleccionadas[3],respuestasSeleccionadas[4],respuestasSeleccionadas[5]]

# Acceder a los atributos de otro objeto de la lista
llamada3 = llamadas[2]
llamada3.descripcionOperador = "Descripción del operador 3"
llamada3.detalleAccionRequerida = "Detalle de la acción requerida 3"
llamada3.duracion = 90
llamada3.encuestaEnviada = False
llamada3.observacionAuditor = "Observación del auditor 3"
llamada3.fechaHoraInicio = "2023-06-03 14:00:00"
llamada3.cliente = clientes[2]
llamada2.cambios_estado = [cambios_estado[5], cambios_estado[6]]
