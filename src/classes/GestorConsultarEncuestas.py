from tkinter import messagebox
##NO USAR HARDCODE DE LLAMADAS from ..classes.Llamada import llamadas
from ..classes.Encuesta import encuestas
from ..utils.generadorCSV import GeneradorCSV
from abc import ABC, abstractmethod
from ..classes.IteradorLlamadas import IteratorLlamadas
from ..database.repositorioDeLlamadas import RepositorioDeLlamadas

class IAgregado(ABC):
    @abstractmethod
    def create_iterator(self):
        pass


class GestorConsultarEncuestas(IAgregado):

    def __init__(self):
        self.__repositorioDeLlamadas = RepositorioDeLlamadas()
        super().__init__()
        self.__fechaFinPeriodo = ''
        self.__fechaInicioPeriodo = ''
        self.__llamadas = []
        self.__llamadaSeleccionada = None
        self.__opcionPresentacion = None

        ## CARGAR LLAMADAS DE LA BASE DE DATOS
        self.__llamadas = self.__repositorioDeLlamadas.obtenerTodas()

    def create_iterator(self):
        fechas = [self.__fechaInicioPeriodo, self.__fechaFinPeriodo]
        return IteratorLlamadas(fechas, self.__llamadas)

    def getFechaFinPeriodo(self):
        return self.__fechaFinPeriodo

    def tomarFechaFin(self, fecha_fin):
        self.__fechaFinPeriodo = fecha_fin
        # todo desde aca buscar las llamadas

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

    def obtenerLlamadasPeriodoConEncuesta(self, pantalla):  # TODO revisar nombre es de periodo
        iterador = self.create_iterator()
        iterador.primero()
        llamadas_p_encuestas = []
        while not iterador.ha_terminado():
            llamada = iterador.actual()
            if llamada is not None:
                llamadas_p_encuestas.append(llamada)
            iterador.siguiente()
        if len(llamadas_p_encuestas) > 0:
            self.setLlamadas(llamadas_p_encuestas)
            pantalla.mostrarLlamadasEncuestaRespondida(llamadas_p_encuestas, self)
        else:
            pantalla.no_hay_llamadas()

    def mostrarLlamadaSeleccionada(self, llamada_fecha, pantalla):
        indice = 0
        for i in range(len(self.__llamadas)):
            fecha_iteradora = self.__llamadas[i].getFechaHoraInicio()
            if fecha_iteradora == llamada_fecha:
                indice = i
                break
        LA_llamada = self.__llamadas[indice]
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
        generador.generarCSVdeLlamada(datos_seleccionada[0], datos_seleccionada[2], datos_seleccionada[1], datos_encuesta[1], datos_seleccionada[3])

        self.finDelCU()

    def finDelCU(self):
        exit()
