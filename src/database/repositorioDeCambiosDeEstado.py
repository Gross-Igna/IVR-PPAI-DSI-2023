from ..classes.GestorPersistencia import GestorPersistencia
from ..classes.CambioEstado import CambioEstado

class RepositorioDeCambiosDeEstado():

    persistencia = GestorPersistencia();

    def __init__(self):
        self.session = self.persistencia.getSession()

    def obtenerTodos(self):
        return self.session.query(CambioEstado).all()