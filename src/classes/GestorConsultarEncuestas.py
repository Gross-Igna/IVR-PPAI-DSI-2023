from 

class GestorConsultarEncuestas(tk.Tk):
    def __init__(self):
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

    def consultarEncuesta(pantalla):
        fechas = pantalla.solicitarSeleccionPeriodo()
        self.tomarFechaInicio()
        self.tomarFechaFin()
        self.obtenerLlamadasPeriodoConEncuesta()

    def obtenerLlamadasPeriodoConEncuesta():
    llamadas_p_encuestas = []
    for llamada in llamadas:
        if llamada.esDePeriodo(self.__fechaInicioPeriodo, self.__fechaFinPeriodo):
            llamadas_p_encuestas.append(llamada.getFechaHoraInicio)

    return llamadas_p_encuestas


    