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

# Crear objetos de la clase Cliente
cliente1 = Cliente("12345678", "Juan Pérez", "987654321")
cliente2 = Cliente("98765432", "María López", "123456789")
cliente3 = Cliente("45678912", "Carlos Gómez", "456789123")

# Crear un array de objetos de la clase Cliente
clientes = [cliente1, cliente2, cliente3]
