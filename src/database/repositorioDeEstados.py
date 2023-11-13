from ..classes.GestorPersistencia import GestorPersistencia
from ..classes.Estado import Estado

class RepositorioDeEstados():

    persistencia = GestorPersistencia();

    def __init__(self):
        self.session = self.persistencia.getSession()

    def obtenerTodos(self):
        return self.session.query(Estado).all()
