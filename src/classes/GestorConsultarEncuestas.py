from tkinter import messagebox
from ..classes.Llamada import llamadas
from ..classes.Encuesta import encuestas
from ..utils.generadorCSV import GeneradorCSV


def no_hay_llamadas():
    messagebox.showinfo("No hay llamadas", "No se encontraron llamadas en este periodo.")
    # exit()


class GestorConsultarEncuestas:
    def __init__(self):
        super().__init__()
        self.__fechaFinPeriodo = ''
        self.__fechaInicioPeriodo = ''
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

    def tomarSeleccionLlamada(self, llamada):
        self.__llamadaSeleccionada = llamada

    def getOpcionPresentacion(self):
        return self.__opcionPresentacion

    def setOpcionPresentacion(self, opcion):
        self.__opcionPresentacion = opcion

    def consultarEncuesta(self, pantalla,window):
        pantalla.solicitarSeleccionPeriodo(self)

    def obtenerLlamadasPeriodoConEncuesta(self, pantalla):
        llamadas_p_encuestas = []
        fecha1 = self.getFechaInicioPeriodo()
        if fecha1 != '':
            for llamada in llamadas:
                if llamada.esDePeriodo(self.__fechaInicioPeriodo, self.__fechaFinPeriodo):
                    llamadas_p_encuestas.append(llamada.getFechaHoraInicio())
            if len(llamadas_p_encuestas) > 0:
                self.setLlamadas(llamadas_p_encuestas)
                pantalla.mostrarLlamadasEncuestaRespondida(llamadas_p_encuestas, self)
            else:
                no_hay_llamadas()

    def mostrarLlamadaSeleccionada(self, llamada_fecha, pantalla):
        indice = 0
        for i in range(len(llamadas)):
            fecha_iteradora = llamadas[i].getFechaHoraInicio()
            if fecha_iteradora == llamada_fecha:
                indice = i
                break
        LA_llamada = llamadas[indice]
        datos_seleccionada = LA_llamada.mostrarLlamada()
        #  return [nombre_cli, duracion, nombre_est, respuestas[]]
        datos_encuesta = []
        fecha_encuesta = LA_llamada.buscarFechaEncuesta()
        for encuesta in encuestas:
            es_vigente = encuesta.vigenteParaLaFecha(fecha_encuesta)
            if es_vigente:
                datos_encuesta = encuesta.getDescripcionEncuesta()
        if len(datos_encuesta):
            pantalla.mostrarLlamadaEncuesta(datos_seleccionada, datos_encuesta, self)

    def tomarOpcionDePresentacion(self, datos_seleccionada, datos_encuesta):
        generador = GeneradorCSV()
        generador.generarCSVdeLlamada(datos_seleccionada[0], datos_seleccionada[1], datos_seleccionada[2], datos_encuesta[1], datos_seleccionada[3])

        self.finDelCU()

    def finDelCU(self):
        exit()
