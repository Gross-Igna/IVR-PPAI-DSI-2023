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
        print(f"fechas {fechas}")

        boton = Button(pantalla, "Buscar Llamadas")
        boton.pack()
        self.tomarFechaInicio(fechas)
        self.tomarFechaFin(fechas)
        llamadas_PyE = self.obtenerLlamadasPeriodoConEncuesta()
        print(llamadas_PyE)
        pantalla.mostrarLlamadaEncuestaRespondida(llamadas_PyE)

    def obtenerLlamadasPeriodoConEncuesta(self):
        llamadas_p_encuestas = []
        for llamada in llamadas:
            print('entro al for de obetener llamadas perdiod con encuetas')
            if llamada.esDePeriodo(self.__fechaInicioPeriodo, self.__fechaFinPeriodo):
                print('lo agrega al arreglo ')
                llamadas_p_encuestas.append(llamada.getFechaHoraInicio())

        return llamadas_p_encuestas

    def tomarSeleccionLlamada(self, llamada_seleccionada):
        self.setLlamadaSeleccionada(llamada_seleccionada)
