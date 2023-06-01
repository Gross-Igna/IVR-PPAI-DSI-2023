class Cliente:
    def __init__(self):
        self.__dni = ""
        self.__nombreCompleto = ""
        self.__nroCelular = ""

    def getDni(self):
        return self.__dni

    def setDni(self, dni):
        self.__dni = dni

    def getNombreCompleto(self):
        return self.__nombreCompleto

    def setNombreCompleto(self, nombre):
        self.__nombreCompleto = nombre

    def getNroCelular(self):
        return self.__nroCelular

    def setNroCelular(self, celular):
        self.__nroCelular = celular
