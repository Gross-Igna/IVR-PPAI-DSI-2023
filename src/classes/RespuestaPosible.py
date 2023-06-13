class RespuestaPosible:
    def __init__(self):
        self.__descripcion = ""
        self.__valor = None

    def getDescripcionRta(self):
        return self.__descripcion

    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion

    def getValor(self):
        return self.__valor

    def setValor(self, valor):
        self.__valor = valor


respuestas_p1 = RespuestaPosible()
respuestas_p1.setDescripcion("Satisfecho")
respuestas_p1.setValor(0)

respuestas_p2 = RespuestaPosible()
respuestas_p2.setDescripcion("Neutral")
respuestas_p2.setValor(1)

respuestas_p3 = RespuestaPosible()
respuestas_p3.setDescripcion("Insatisfecho")
respuestas_p3.setValor(2)

respuestas_p4 = RespuestaPosible()
respuestas_p4.setDescripcion("Si")
respuestas_p4.setValor(0)

respuestas_p5 = RespuestaPosible()
respuestas_p5.setDescripcion("No")
respuestas_p5.setValor(1)

respuestas_p6 = RespuestaPosible()
respuestas_p6.setDescripcion("Aceptable")
respuestas_p6.setValor(0)

respuestas_p7 = RespuestaPosible()
respuestas_p7.setDescripcion("Largo")
respuestas_p7.setValor(1)

respuestas_p8 = RespuestaPosible()
respuestas_p8.setDescripcion("Completamente resulta")
respuestas_p8.setValor(0)

respuestas_p9 = RespuestaPosible()
respuestas_p9.setDescripcion("Parcialmente resuelta")
respuestas_p9.setValor(1)

respuestas_p10 = RespuestaPosible()
respuestas_p10.setDescripcion("No resulta")
respuestas_p10.setValor(2)

respuestas_posibles = [respuestas_p1, respuestas_p2, respuestas_p3, respuestas_p4, respuestas_p5, respuestas_p6, respuestas_p7,
                        respuestas_p8, respuestas_p9, respuestas_p10]