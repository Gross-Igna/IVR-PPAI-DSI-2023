from ..classes.Estado import estados


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


cambio1 = CambioEstado()  # iniciada para llamada 1
cambio1.fechaHoraInicio = "2023-06-01 10:00:00"
cambio1.fechaHoraFin = "2023-06-01 10:02:00"
cambio1.estado = estados[1]

cambio2 = CambioEstado()  # en curso para llamada 1
cambio2.fechaHoraInicio = "2023-06-01 10:02:00"
cambio2.fechaHoraFin = "2023-06-01 10:04:00"
cambio2.estado = estados[0]

cambio3 = CambioEstado()  # finalizada para llamada 1
cambio3.fechaHoraInicio = "2023-06-01 10:04:00"
cambio3.estado = estados[2]

cambio4 = CambioEstado()  # iniciada para llamada 2
cambio4.fechaHoraInicio = "2023-06-01 12:00:00"
cambio4.fechaHoraFin = "2023-06-01 12:02:00"
cambio4.estado = estados[1]

cambio5 = CambioEstado()  # finalizada para llamada 2
cambio5.fechaHoraInicio = "2023-06-01 12:02:00"
cambio5.estado = estados[2]

cambio6 = CambioEstado()  # iniciada para llamada 3
cambio6.fechaHoraInicio = "2023-06-01 14:00:00"
cambio6.fechaHoraFin = "2023-06-01 14:02:00"
cambio6.estado = estados[1]

cambio7 = CambioEstado()  # finalizada para llamada 3
cambio7.fechaHoraInicio = "2023-06-01 14:02:00"
cambio7.estado = estados[2]


cambios_estado = [cambio1, cambio2, cambio3, cambio4, cambio5, cambio6, cambio7]
