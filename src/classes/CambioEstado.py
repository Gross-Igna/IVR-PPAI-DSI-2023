##from ..classes.Estado import estados
from ..database.repositorioDeEstados import RepositorioDeEstados
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

Base = declarative_base()
class CambioEstado(Base):

    __tablename__ = 'cambios_estado'
    id = Column(Integer, primary_key=True)
    fechaHoraInicio = Column(String)
    fechaHoraFin = Column(String)
    estado_id = Column(Integer)
    llamada_id = Column(Integer)

    def __init__(self):
        self.fechaHoraInicio = None
        self.fechaHoraFin = None
        self.estado_id = None
        self.llamada_id = None

    def getFechaHoraInicio(self):
        return self.fechaHoraInicio

    def setFechaHoraInicio(self, fechaHoraInicio):
        self.fechaHoraInicio = fechaHoraInicio

    def getFechaHoraFin(self):
        try:
            return self.__fechaHoraFin
        except AttributeError:
            return None

    def setFechaHoraFin(self, fechaHoraFin):
        self.fechaHoraFin = fechaHoraFin

    def getEstado_id(self):
        return self.estado_id

    def setEstado_id(self, estado_id):
        self.estado_id = estado_id

    def getLlamada_id(self):
        return self.llamada_id

    def setLlamada_id(self, llamada_id):
        self.llamada_id = llamada_id

    def esUltimoCambioEstado(self):
        fechaFin = self.getFechaHoraFin()
        if fechaFin is None:
            return True


repositorioDeEstados = RepositorioDeEstados()
estados = repositorioDeEstados.obtenerTodos()
print(estados)

# cambio1 = CambioEstado()  # iniciada para llamada 1
# cambio1.fechaHoraInicio = "2023-06-01 10:00:00"
# cambio1.fechaHoraFin = "2023-06-01 10:02:00"
# cambio1.setEstado(estados[1])
#
# cambio2 = CambioEstado()  # en curso para llamada 1
# cambio2.fechaHoraInicio = "2023-06-01 10:02:00"
# cambio2.fechaHoraFin = "2023-06-01 10:04:00"
# cambio2.setEstado(estados[0])
#
# cambio3 = CambioEstado()  # finalizada para llamada 1
# cambio3.fechaHoraInicio = "2023-06-01 10:04:00"
# cambio3.setEstado(estados[2])
#
# cambio4 = CambioEstado()  # iniciada para llamada 2
# cambio4.fechaHoraInicio = "2023-06-01 12:00:00"
# cambio4.fechaHoraFin = "2023-06-01 12:02:00"
# cambio4.setEstado(estados[1])
#
# cambio5 = CambioEstado()  # finalizada para llamada 2
# cambio5.fechaHoraInicio = "2023-06-01 12:02:00"
# cambio5.setEstado(estados[2])
#
# cambio6 = CambioEstado()  # iniciada para llamada 3
# cambio6.fechaHoraInicio = "2023-06-01 14:00:00"
# cambio6.fechaHoraFin = "2023-06-01 14:02:00"
# cambio6.setEstado(estados[1])
#
# cambio7 = CambioEstado()  # finalizada para llamada 3
# cambio7.fechaHoraInicio = "2023-06-01 14:02:00"
# cambio7.llamada_id = 1
# cambio7.setEstado(estados[2])
#
#
# cambios_estado = [cambio1, cambio2, cambio3, cambio4, cambio5, cambio6, cambio7]
