from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey, Boolean, ARRAY

Base = declarative_base()

class Estado(Base):

    __tablename__ = 'estados'
    id = Column(Integer, Sequence('estados_id_seq'), primary_key=True)
    nombre = Column(String)

    def __init__(self):
        self.nombre = ""

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre


# estado1 = Estado()
# estado1.setNombre("En curso")
# estado2 = Estado()
# estado2.setNombre("Iniciada")
# estado3 = Estado()
# estado3.setNombre("Finalizada")
#
# estados = [estado1, estado2, estado3]
