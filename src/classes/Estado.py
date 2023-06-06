class Estado:
    def __init__(self):
        self.__nombre = ""

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

estados = [
    Estado(),
    Estado(),
    Estado()
]

estados[0].nombre = "En curso"

estado[1].mombre = "Iniciada"

estado[2].nombre = "Finalizada"
