from ..classes.RespuestaPosible import respuestas_posibles


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

    def getDescripcionRta(self):
        seleccionada = self.getRespuestaSeleccionada()
        descripcion = seleccionada.getDescripcionRta()
        return descripcion


rta1 = RespuestaDelCliente()
rta1.setFechaEncuesta("6/7/23")
rta1.setRespuestaSeleccionada(respuestas_posibles[2])

rta2 = RespuestaDelCliente()
rta2.setFechaEncuesta("6/7/23")
rta2.setRespuestaSeleccionada(respuestas_posibles[4])

rta3 = RespuestaDelCliente()
rta3.setFechaEncuesta("6/7/23")
rta3.setRespuestaSeleccionada(respuestas_posibles[6])


rta4 = RespuestaDelCliente()
rta4.setFechaEncuesta("8/7/23")
rta4.setRespuestaSeleccionada(respuestas_posibles[0])

rta5 = RespuestaDelCliente()
rta5.setFechaEncuesta("8/7/23")
rta5.setRespuestaSeleccionada(respuestas_posibles[3])

rta6 = RespuestaDelCliente()
rta6.setFechaEncuesta("8/7/23")
rta6.setRespuestaSeleccionada(respuestas_posibles[5])



rta7 = RespuestaDelCliente()
rta7.setFechaEncuesta("9/7/23")
rta7.setRespuestaSeleccionada(respuestas_posibles[0])

rta8 = RespuestaDelCliente()
rta8.setFechaEncuesta("9/7/23")
rta8.setRespuestaSeleccionada(respuestas_posibles[3])

rta9 = RespuestaDelCliente()
rta9.setFechaEncuesta("9/7/23")
rta9.setRespuestaSeleccionada(respuestas_posibles[5])

respuestasSeleccionadas = [rta1, rta2, rta3, rta4, rta5, rta6, rta7, rta8, rta9]
