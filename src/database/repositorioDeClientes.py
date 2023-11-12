from ..classes.GestorPersistencia import GestorPersistencia
from ..classes.Cliente import Cliente

class RepositorioDeClientes():

    persistencia = GestorPersistencia();

    def __init__(self):
        self.session = self.persistencia.getSession()

    def guardar(self, cliente):
        self.session.add(cliente)
        self.session.commit()

    def buscarPorDni(self, dni):
        try:
            cliente = self.session.query(Cliente).filter(Cliente.dni == dni).first()
            return cliente
        except Exception as e:
            print(f"Error al obtener el cliente por DNI: {e}")
            return None

    def obtenerTodos(self):
        return self.session.query(Cliente).all()