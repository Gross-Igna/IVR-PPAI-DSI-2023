from ..classes.Pregunta import preguntas


class Encuesta:
    def __init__(self):
        self.__descripcion = ""
        self.__fechaInicioVigencia = ""
        self.__fechaFinVigencia = ""
        self.__preguntas = []

    def getDescripcion(self):
        return self.__descripcion

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


encuesta1 = Encuesta()
encuesta1.__descripcion = "Encuesta 1"
encuesta1.__fechaInicioVigencia = "2010-06-01 10:00:00"
encuesta1.__fechaFinVigencia = "2023-01-01 10:00:00"
encuesta1.__preguntas = [preguntas[1], preguntas[2], preguntas[3]]

encuesta2 = Encuesta()
encuesta2.__descripcion = "Encuesta 2"
encuesta2.__fechaInicioVigencia = "2023-01-01 10:00:00"
encuesta1.__preguntas = [preguntas[0], preguntas[1], preguntas[2]]

encuestas = [encuesta1, encuesta2]


