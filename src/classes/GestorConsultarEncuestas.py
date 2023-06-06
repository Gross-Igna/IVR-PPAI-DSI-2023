import tkinter as tk
from ..classes.Llamada import Llamada

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

# Acceder a los atributos de otro objeto de la lista
llamada2 = llamadas[1]
llamada2.descripcionOperador = "Descripción del operador 2"
llamada2.detalleAccionRequerida = "Detalle de la acción requerida 2"
llamada2.duracion = 180
llamada2.encuestaEnviada = False
llamada2.observacionAuditor = "Observación del auditor 2"
llamada2.fechaHoraInicio = "2023-06-03 12:00:00"

# Acceder a los atributos de otro objeto de la lista
llamada3 = llamadas[2]
llamada3.descripcionOperador = "Descripción del operador 3"
llamada3.detalleAccionRequerida = "Detalle de la acción requerida 3"
llamada3.duracion = 90
llamada3.encuestaEnviada = True
llamada3.observacionAuditor = "Observación del auditor 3"
llamada3.fechaHoraInicio = "2023-06-03 14:00:00"


class GestorConsultarEncuestas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.__fechaFinPeriodo = None
        self.__fechaInicioPeriodo = None
        self.__llamadas = None
        self.__llamadaSeleccionada = None
        self.__opcionPresentacion = None

    def getFechaFinPeriodo(self):
        return self.fechaFinPeriodo

    def tomarFechaFin(self, fechas):
        self.__fechaFinPeriodo = fechas[1]

    def getFechaInicioPeriodo(self):
        return self.__fechaInicioPeriodo

    def tomarFechaInicio(self, fechas):
        self.__fechaInicioPeriodo = fechas[0]

    def getLlamadas(self):
        return self.__llamadas

    def setLlamadas(self, llamadas):
        self.__llamadas = llamadas

    def getLlamadaSeleccionada(self):
        return self.__llamadaSeleccionada

    def setLlamadaSeleccionada(self, llamada):
        self.__llamadaSeleccionada = llamada

    def getOpcionPresentacion(self):
        return self.__opcionPresentacion

    def setOpcionPresentacion(self, opcion):
        self.__opcionPresentacion = opcion

    def consultarEncuesta(self, pantalla):
        fechas = pantalla.solicitarSeleccionPeriodo()
        self.tomarFechaInicio(fechas)
        self.tomarFechaFin(fechas)
        self.obtenerLlamadasPeriodoConEncuesta()

    def obtenerLlamadasPeriodoConEncuesta(self):
        llamadas_p_encuestas = []
        for llamada in llamadas:
            if llamada.esDePeriodo(self.__fechaInicioPeriodo, self.__fechaFinPeriodo):
                llamadas_p_encuestas.append(llamada.getFechaHoraInicio)

        return llamadas_p_encuestas

