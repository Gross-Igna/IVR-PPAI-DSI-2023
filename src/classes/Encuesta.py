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
