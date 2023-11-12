from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# # Crear una clase Base para declarar modelos
# Base = declarative_base()
#
# # Definir un modelo simple
# class Usuario(Base):
#     __tablename__ = 'usuarios'
#     id = Column(Integer, Sequence('usuario_id_seq'), primary_key=True)
#     nombre = Column(String(50))
#     edad = Column(Integer)
#
# # Crear la tabla en la base de datos
# Base.metadata.create_all(engine)
#
# # Crear una sesión
# Session = sessionmaker(bind=engine)
# session = Session()
#
# # Ejemplo: Insertar un nuevo usuario
# nuevo_usuario = Usuario(nombre='Juan', edad=25)
# session.add(nuevo_usuario)
# session.commit()
#
# # Ejemplo: Consultar todos los usuarios e imprimir sus nombres y edades
# usuarios = session.query(Usuario).all()
# for usuario in usuarios:
#     print(f"Nombre: {usuario.nombre}, Edad: {usuario.edad}")
#
# # Cerrar la sesión
# session.close()

class GestorPersistencia():
    def __init__(self):
        self.__bdUrl = 'sqlite:///C:/ivr.db'
        self.__engine = create_engine(self.__bdUrl, echo=False)
        self.__Base = declarative_base()
        self.__Session = sessionmaker(bind=self.__engine)
        self.__session = self.__Session()

    def getSession(self):
        return self.__session