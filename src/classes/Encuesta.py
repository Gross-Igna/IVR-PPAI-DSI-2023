from datetime import datetime

from ..classes.Pregunta import preguntas


class Encuesta:
    def __init__(self):
        self.__descripcion = ""
        self.__fechaInicioVigencia = ""
        self.__fechaFinVigencia = ""
        self.__preguntas = []

    def getDescripcionEncuesta(self):
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
        fechaInicio = self.getFechaInicioVigencia()
        fechaFin = self.getFechaFinVigencia()

        fecha_inicio = datetime.strptime(fechaInicio, "%d/%m/%y").date()
        fecha_fin = datetime.strptime(fechaFin, "%d/%m/%y").date()
        fecha_encuesta = datetime.strptime(fecha, "%d/%m/%y").date()

        print(f"fechainicio: {fechaInicio} - fecha: {fecha} - fechafin: {fechaFin}")
        if fecha_inicio == '' or fecha_encuesta == '' or fecha_fin == '':
            pass
        elif fecha_inicio <= fecha_encuesta <= fecha_fin:
            return True
        else:
            return False


encuesta1 = Encuesta()
encuesta1.setDescripcion("Encuesta 1")
encuesta1.setFechaInicioVigencia("2/7/23")
encuesta1.setFechaFinVigencia("12/7/23")
encuesta1.setPreguntas([preguntas[1], preguntas[2], preguntas[3]])

encuesta2 = Encuesta()
encuesta2.setDescripcion('Encuesta 2')
encuesta2.setFechaInicioVigencia("23/10/23")
encuesta2.setFechaFinVigencia("17/7/23")

encuesta1.setPreguntas([preguntas[0], preguntas[1], preguntas[2]])

encuestas = [encuesta1, encuesta2]


