from ..classes.RespuestaPosible import respuestas_posibles


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


pregunta1 = Pregunta()
pregunta1.__pregunta = "Cuál es su nivel de satisfacción con nuestro servicio?"
pregunta1.__respuestasPosibles = [respuestas_posibles[0], respuestas_posibles[1], respuestas_posibles[2]]

pregunta2 = Pregunta()
pregunta2.__pregunta = "¿Recomendaría nuestros servicios a otras personas?"
pregunta2.__respuestasPosibles = [respuestas_posibles[3],respuestas_posibles[4]]

pregunta3 = Pregunta()
pregunta3.__pregunta = "¿Cómo evaluaría el tiempo de espera para ser atendido?"
pregunta3.__respuestasPosibles = [respuestas_posibles[5],respuestas_posibles[6]]

pregunta4 = Pregunta()
pregunta4.__pregunta = "¿En qué medida hemos resuelto su problema o necesidad?"
pregunta4.__respuestasPosibles = [respuestas_posibles[7], respuestas_posibles[8], respuestas_posibles[9]]

preguntas = [pregunta1, pregunta2, pregunta3, pregunta4]
