class RespuestaPosible:
    def __init__(self):
        self.__descripcion = ""
        self.__valor = ""

    def getDescripcion(self):
        return self.__descripcion

    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion

    def getValor(self):
        return self.__valor

    def setValor(self, valor):
        self.__valor = valor
