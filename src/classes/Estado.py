class Estado:
    def __init__(self):
        self.__nombre = ""

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre


estado1 = Estado()
estado1.setNombre("En curso")
estado2 = Estado()
estado2.setNombre("Iniciada")
estado3 = Estado()
estado3.setNombre("Finalizada")

estados = [estado1, estado2, estado3]
