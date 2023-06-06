from datetime import datetime


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

    def esDePeriodo(self, fechaInicio , fechaFin):
        fecha_inicio = datetime.strptime(fechaInicio, "%d-%m-%Y").date()
        fecha_fin = datetime.strptime(fechaFin, "%d-%m-%Y").date()
        fecha_llamada = datetime.strptime(self.__fechaHoraInicio, "%d-%m-%Y").date()
        if fecha_inicio <= fecha_llamada <= fecha_fin:
            tieneEncuesta = tieneEncuestaRespondida()
            if tieneEncuesta:
                return True

    def tieneEncuestaRespondida(self):
        return self.__encuestaEnviada

