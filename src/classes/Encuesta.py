class Encuesta:
    def __init__(self):
        self.__descripcion = ""
        self.__fechaVigencia = ""
        self.__preguntas = []

    def getDescripcion(self):
        return self.__descripcion

    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion

    def getFechaVigencia(self):
        return self.__fechaVigencia

    def setFechaVigencia(self, fecha):
        self.__fechaVigencia = fecha

    def getPreguntas(self):
        return self.__preguntas

    def setPreguntas(self, preguntas):
        self.__preguntas = preguntas
