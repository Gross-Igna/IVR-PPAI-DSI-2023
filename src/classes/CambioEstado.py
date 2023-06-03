class CambioEstado:
    def __init__(self):
        self.__fechaHoraInicio = None
        self.__fechaHoraFin = None
        self.__estado = None

    def getFechaHoraInicio(self):
        return self.__fechaHoraInicio

    def setFechaHoraInicio(self, fechaHoraInicio):
        self.__fechaHoraInicio = fechaHoraInicio

    def getFechaHoraFin(self):
        return self.__fechaHoraFin

    def setFechaHoraFin(self, fechaHoraFin):
        self.__fechaHoraFin = fechaHoraFin

    def getEstado(self):
        return self.__estado

    def setEstado(self, estado):
        self.__estado = estado
