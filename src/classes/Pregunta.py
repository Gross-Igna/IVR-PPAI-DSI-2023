class Pregunta:
    def __init__(self):
        self.__pregunta = ""
        self.__respuestasPosibles = []

    def getPregunta(self):
        return self.__pregunta

    def setPregunta(self, pregunta):
        self.__pregunta = pregunta

    def getRespuestasPosibles(self):
        return self.__respuestasPosibles

    def setRespuestasPosibles(self, respuestas):
        self.__respuestasPosibles = respuestas
