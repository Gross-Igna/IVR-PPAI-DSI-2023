from ..classes.GestorPersistencia import GestorPersistencia
from ..classes.Llamada import Llamada

class RepositorioDeLlamadas():

    persistencia = GestorPersistencia();

    def __init__(self):
        self.session = self.persistencia.getSession()

    def obtenerTodas(self):
        return self.session.query(Llamada).all()
