class Cliente:
    def __init__(self):
        self.__dni = ""
        self.__nombre = ""
        self.__nroCelular = ""

    def getDni(self):
        return self.__dni

    def setDni(self, dni):
        self.__dni = dni

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getNroCelular(self):
        return self.__nroCelular

    def setNroCelular(self, celular):
        self.__nroCelular = celular


# Crear objetos de la clase Cliente
cliente1 = Cliente()
cliente1.setDni("12345678")
cliente1.setNombre("Juan Perez")
cliente1.setNroCelular("987654321")

cliente2 = Cliente()
cliente2.setDni("10312345678")
cliente2.setNombre("Juana Pereza")
cliente2.setNroCelular("107654321")

cliente3 = Cliente()
cliente3.setDni("9912345678")
cliente3.setNombre("Juancito Perez miguel")
cliente3.setNroCelular("557654321")

# Crear un array de objetos de la clase Cliente
clientes = [cliente1, cliente2, cliente3]
