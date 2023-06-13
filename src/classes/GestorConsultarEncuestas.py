from ..classes.Llamada import llamadas
from ..classes.Encuesta import encuestas


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

    def setLlamadaSeleccionada(self, llamada):
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
        print(fecha1)
        if fecha1 != '':
            for llamada in llamadas:
                if llamada.esDePeriodo(self.__fechaInicioPeriodo, self.__fechaFinPeriodo):
                    llamadas_p_encuestas.append(llamada.getFechaHoraInicio())
            self.setLlamadas(llamadas_p_encuestas)
            pantalla.mostrarLlamadasEncuestaRespondida(llamadas_p_encuestas, self)

    def tomarSeleccionLlamada(self, llamada_seleccionada, pantalla):
        self.setLlamadaSeleccionada(llamada_seleccionada)
        self.mostrarLlamadaSeleccionada(llamada_seleccionada, pantalla)

    def mostrarLlamadaSeleccionada(self, llamada_fecha, pantalla):
        indice = 0
        for i in range(len(llamadas)):
            fecha_iteradora = llamadas[i].getFechaHoraInicio()
            if fecha_iteradora == llamada_fecha:
                indice = i
        LA_llamada = llamadas[indice]
        datos_seleccionada = LA_llamada.mostrarLlamada()
        #  return [nombre_cli, duracion, nombre_est, descripciones[]]
        datos_encuesta = []
        fecha_encuesta = LA_llamada.buscarFechaEncuesta()
        for encuesta in encuestas:
            es_vigente = encuesta.vigenteParaLaFecha(fecha_encuesta)
            if es_vigente:
                datos_encuesta = encuesta.getDescripcionEncuesta()
        if len(datos_encuesta):
            pantalla.mostrarLlamadaEncuesta(datos_seleccionada, datos_encuesta)


    #def tomarSeleccionDePresentacion(self,opcion):
    #    self.setOpcionPresentacion(opcion)
    #    generador = GeneradorCSV()
    #    generador.generar_csv_de_llamada()
