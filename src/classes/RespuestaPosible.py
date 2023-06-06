class RespuestaPosible:
    def __init__(self):
        self.__descripcion = ""
        self.__valor = None

    def getDescripcion(self):
        return self.__descripcion

    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion

    def getValor(self):
        return self.__valor

    def setValor(self, valor):
        self.__valor = valor


respuestas_p1 = RespuestaPosible()
respuestas_p1.descripcion = "Satisfecho"
respuestas_p1.valor = 0

respuestas_p2 = RespuestaPosible()
respuestas_p2.descripcion = "Neutral"
respuestas_p2.valor = 1

respuestas_p3 = RespuestaPosible()
respuestas_p3.descripcion = "Insatisfecho"
respuestas_p3.valor = 2

respuestas_p4 = RespuestaPosible()
respuestas_p4.descripcion = "Si"
respuestas_p4.valor = 0

respuestas_p5 = RespuestaPosible()
respuestas_p5.descripcion = "No"
respuestas_p5.valor = 1

respuestas_p6 = RespuestaPosible()
respuestas_p6.descripcion = "Aceptable"
respuestas_p6.valor = 0

respuestas_p7 = RespuestaPosible()
respuestas_p7.descripcion = "Largo"
respuestas_p7.valor = 1

respuestas_p8 = RespuestaPosible()
respuestas_p8.descripcion = "Completamente resulta"
respuestas_p8.valor = 0

respuestas_p9 = RespuestaPosible()
respuestas_p9.descripcion = "Parcialmente resuelta"
respuestas_p9.valor = 1

respuestas_p10 = RespuestaPosible()
respuestas_p10.descripcion = "No resuelta"
respuestas_p10.valor = 2

respuestas_posibles = [respuestas_p1, respuestas_p2, respuestas_p3, respuestas_p4, respuestas_p5, respuestas_p6, respuestas_p7,
                        respuestas_p8, respuestas_p9, respuestas_p10]