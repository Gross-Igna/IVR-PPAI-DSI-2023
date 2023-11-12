from ..classes.GestorPersistencia import GestorPersistencia
from ..classes.Cliente import Cliente

class RepositorioDeClientes():

    persistencia = GestorPersistencia();

    def __init__(self):
        self.session = self.persistencia.getSession()

    def guardar(self, cliente):
        self.session.add(cliente)
        self.session.commit()

    def obtenerPorDni(self, dni):
        return self.session.query(Cliente).filter(Cliente.dni == dni).first()

    def obtenerTodos(self):
        return self.session.query(Cliente).all()