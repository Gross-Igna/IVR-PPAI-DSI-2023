from ..classes.GestorPersistencia import GestorPersistencia
from ..classes.Estado import Estado

class RepositorioDeEstados():

    persistencia = GestorPersistencia();

    def __init__(self):
        self.session = self.persistencia.getSession()

    def obtenerTodos(self):
        return self.session.query(Estado).all()

    def obtenerPorId(self, id):
        try:
            estado = self.session.query(Estado).filter(Estado.id == id).first()
            return estado
        except Exception as e:
            print(f"Error al obtener el estado por ID: {e}")
            return None