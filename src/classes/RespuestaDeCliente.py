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
rta1.setFechaEncuesta("7/6/23")
rta1.setRespuestaSeleccionada(respuestas_posibles[2])

rta2 = RespuestaDelCliente()
rta2.setFechaEncuesta("7/6/23")
rta2.setRespuestaSeleccionada(respuestas_posibles[4])

rta3 = RespuestaDelCliente()
rta3.setFechaEncuesta("7/6/23")
rta3.setRespuestaSeleccionada(respuestas_posibles[6])


rta4 = RespuestaDelCliente()
rta4.__fechaEncuesta = "2023-06-05 12:00:00"
rta4.__respuestaSeleccionada = respuestas_posibles[0]

rta5 = RespuestaDelCliente()
rta5.__fechaEncuesta = "2023-06-05 12:00:00"
rta5.__respuestaSeleccionada = respuestas_posibles[3]

rta6 = RespuestaDelCliente()
rta6.__fechaEncuesta = "2023-06-05 12:00:00"
rta6.__respuestaSeleccionada = respuestas_posibles[5]

respuestasSeleccionadas = [rta1, rta2, rta3, rta4, rta5, rta6]
