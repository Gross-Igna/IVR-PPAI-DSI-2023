from ..classes.GestorPersistencia import GestorPersistencia
from ..classes.Llamada import Llamada

class RepositorioDeLlamadas():

    persistencia = GestorPersistencia();

    def __init__(self):
        self.session = self.persistencia.getSession()

    def guardar(self, llamada):
        self.session.add(llamada)
        self.session.commit()

    def obtener(self, id):
        return self.session.query(Llamada).filter(Llamada.id == id).first()

    def obtenerTodas(self):
        return self.session.query(Llamada).all()
