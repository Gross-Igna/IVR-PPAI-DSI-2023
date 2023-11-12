from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class GestorPersistencia():
    def __init__(self):
        self.__bdUrl = 'sqlite:///C:/ivr.db'
        self.__engine = create_engine(self.__bdUrl, echo=False)
        self.__Base = declarative_base()
        self.__Session = sessionmaker(bind=self.__engine)
        self.__session = self.__Session()

    def getSession(self):
        return self.__session