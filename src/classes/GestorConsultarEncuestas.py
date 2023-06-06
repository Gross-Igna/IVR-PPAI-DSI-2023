import tkinter as tk
from ..classes.Llamada import llamadas
from src.interface.button import Button

class GestorConsultarEncuestas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.__fechaFinPeriodo = None
        self.__fechaInicioPeriodo = None
        self.__llamadas = None
        self.__llamadaSeleccionada = None
        self.__opcionPresentacion = None

    def getFechaFinPeriodo(self):
        return self.__fechaFinPeriodo

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
        print("llego al consultar encuesta dentro de gestor")
        fechas = pantalla.solicitarSeleccionPeriodo()
        # fechas = [fecha1, fecha2]
        # ACTIVAR BOTON PARA QUE SE OPTENGAN LAS LALAMADAS Y LUEGO SE MUESTREN
        boton = Button(pantalla, "Buscar LLamadas")
        boton.pack()
        if boton.precionado:
            print("dnetro de if en consultar encuensta")
            self.tomarFechaInicio(fechas)
            self.tomarFechaFin(fechas)
            llamadas_PyE = self.obtenerLlamadasPeriodoConEncuesta()

            pantalla.mostrarLlamadaEncuestaRespondida(llamadas_PyE)

    def obtenerLlamadasPeriodoConEncuesta(self):
        llamadas_p_encuestas = []
        for llamada in llamadas:
            if llamada.esDePeriodo(self.__fechaInicioPeriodo, self.__fechaFinPeriodo):
                llamadas_p_encuestas.append(llamada.getFechaHoraInicio)

        return llamadas_p_encuestas

