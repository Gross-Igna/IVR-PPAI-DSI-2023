class RespuestaDelCliente:
    def __init__(self):
        self.__fechaEncuesta = ""
        self.__respuestaSeleccionada = None

    def getFechaEncuesta(self):
        return self.__fechaEncuesta

    def setFechaEncuesta(self, fecha):
        self.__fechaEncuesta = fecha

    def getRespuestaSeleccionada(self):
        return self.__respuestaSeleccionada

    def setRespuestaSeleccionada(self, respuesta):
        self.__respuestaSeleccionada = respuesta
