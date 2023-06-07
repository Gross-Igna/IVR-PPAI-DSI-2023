from ..classes.Pregunta import preguntas
from datetime import datetime, date

class Encuesta:
    def __init__(self):
        self.__descripcion = ""
        self.__fechaInicioVigencia = ""
        self.__fechaFinVigencia = ""
        self.__preguntas = []

    def getDescripcionEncuesta(self):
        # dudoso: 29 va dentro de 28?
        preguntas = self.getPreguntas()
        desc_preguntas = []
        for pregunta in preguntas:  # array de objetos pregunta
            desc_una_pregunta = pregunta.getDescripcionPregunta()
            desc_preguntas.append(desc_una_pregunta)
        return [self.__descripcion, desc_preguntas]

    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion

    def getFechaInicioVigencia(self):
        return self.__fechaInicioVigencia

    def setFechaInicioVigencia(self, fecha):
        self.__fechaInicioVigencia = fecha

    def getFechaFinVigencia(self):
        return self.__fechaFinVigencia

    def setFechaFinVigencia(self, fecha):
        self.__fechaFinVigencia = fecha

    def getPreguntas(self):
        return self.__preguntas

    def setPreguntas(self, preguntas):
        self.__preguntas = preguntas

    def vigenteParaLaFecha(self, fecha):
        fecha_inicio = self.getFechaInicioVigencia()
        fecha_inicio_date = datetime.strptime(fecha_inicio, "%d/%m/%y").date()
        fecha_fin = self.getFechaFinVigencia()
        fecha_fin_date = datetime.strptime(fecha_fin, "%d/%m/%y").date()
        fecha_encuesta_date = datetime.strptime(fecha, "%d/%m/%y").date()

        if fecha_inicio_date <= fecha_encuesta_date <= fecha_fin_date:
            return True

encuesta1 = Encuesta()
encuesta1.setDescripcion("Encuesta para medir la satisfaccion del cliente")
encuesta1.setFechaInicioVigencia("1/1/10")
encuesta1.setFechaFinVigencia("1/1/23")
encuesta1.setPreguntas([preguntas[1], preguntas[2], preguntas[3]])

encuesta2 = Encuesta()
encuesta2.setDescripcion("Encuesta que mide el nivel de satisfaccion del cliente")
encuesta2.setFechaInicioVigencia("1/1/20")
encuesta2.setFechaFinVigencia("7/6/23")
encuesta2.setPreguntas([preguntas[0], preguntas[1], preguntas[2]])

encuestas = [encuesta1, encuesta2]


