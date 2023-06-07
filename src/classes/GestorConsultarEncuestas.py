import tkinter as tk
from ..classes.Llamada import llamadas
from src.interface.button import Button
from ..classes.Encuesta import encuestas
from ..utils.generadorCSV import GeneradorCSV


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

    def tomarFechaFin(self, fecha_fin):
        self.__fechaFinPeriodo = fecha_fin

    def getFechaInicioPeriodo(self):
        return self.__fechaInicioPeriodo

    def tomarFechaInicio(self, fecha_in):
        self.__fechaInicioPeriodo = fecha_in

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
        print("Para salir presione X")
        fecha_inicio = input("Ingrese la fecha de inicio del periodo dd/mm/aa: ")
        if fecha_inicio != "X":
            self.tomarFechaInicio(fecha_inicio)
        else:
            exit()

        fecha_fin = input("Ingrese la fecha de fin del periodo dd/mm/aa: ")
        if fecha_fin != "X":
            self.tomarFechaFin(fecha_fin)
        else:
            exit()
        llamadas_PyE = self.obtenerLlamadasPeriodoConEncuesta()
        if len(llamadas_PyE) == 0:
            print("No hay llamadas con encuesta respondida para el periodo")
            exit()
        pantalla.mostrarLlamadaEncuestaRespondida(llamadas_PyE, self)

    def obtenerLlamadasPeriodoConEncuesta(self):
        llamadas_p_encuestas = []
        for llamada in llamadas:
            if llamada.esDePeriodo(self.getFechaInicioPeriodo(), self.getFechaFinPeriodo()):
                llamadas_p_encuestas.append(llamada.getFechaHoraInicio())
        return llamadas_p_encuestas

    def tomarSeleccionLlamada(self, indice_seleccionada, pantalla):
        self.setLlamadaSeleccionada(indice_seleccionada)
        self.mostrarLlamadaSeleccionada(indice_seleccionada, pantalla)

    def mostrarLlamadaSeleccionada(self, indice_llamada, pantalla):
        # buscar la llamad
        LA_llamada = llamadas[indice_llamada]
        datos_seleccionada = LA_llamada.mostrarLlamada()
        #  return [nombre_cli, duracion, nombre_est, descripciones[]]
        datos_encuesta = []
        fecha_encuesta = LA_llamada.buscarFechaEncuesta()
        for encuesta in encuestas:
            es_vigente = encuesta.vigenteParaLaFecha(fecha_encuesta)
            if es_vigente:
                datos_encuesta = encuesta.getDescripcionEncuesta()
                # datos_encuesta = ["encuesta 1", ["¿como calificaria..."]]
        if len(datos_encuesta):
            pantalla.mostrarLlamadaEncuesta(datos_seleccionada, datos_encuesta, self)
        else:
            print('')


    def tomarSeleccionDePresentacion(self,opcion, datos_seleccionada, datos_encuesta):
        self.setOpcionPresentacion(opcion)
        generador = GeneradorCSV("")
        cliente = datos_seleccionada[0]
        estado = datos_seleccionada[2]
        duracion = datos_seleccionada[1]
        respuestas = datos_seleccionada[3]

        preguntas = datos_encuesta[1]

        generador.generarCSVdeLlamada(cliente,estado, duracion, preguntas,respuestas)
