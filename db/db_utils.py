from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db import Llamada, Cliente, CambioEstado, RespuestaDeCliente, RespuestaPosible, Encuesta, Estado, Pregunta

engine = create_engine('sqlite:///bdIvr.db')

# TODO: deberiamos tener estas funciones en la declaracion de cada clase ?


def get_llamadas_db():
    Session = sessionmaker(bind=engine)
    session = Session()
    llamadas = session.query(Llamada).all()
    session.close()
    return llamadas


def get_clientes_db():
    Session = sessionmaker(bind=engine)
    session = Session()
    clientes = session.query(Cliente).all()
    session.close()
    return clientes


def get_cambios_estados_db():
    Session = sessionmaker(bind=engine)
    session = Session()
    cambios_estados = session.query(CambioEstado).all()
    session.close()
    return cambios_estados


def get_respuesta_cliente_db():
    Session = sessionmaker(bind=engine)
    session = Session()
    respuestas_clientes = session.query(RespuestaDeCliente).all()
    session.close()
    return respuestas_clientes


def get_respuesta_posible_db():
    Session = sessionmaker(bind=engine)
    session = Session()
    respuestas_posible = session.query(RespuestaPosible).all()
    session.close()
    return respuestas_posible


def get_encuesta_db():
    Session = sessionmaker(bind=engine)
    session = Session()
    encuestas = session.query(Encuesta).all()
    session.close()
    return encuestas


def get_estado_db():
    Session = sessionmaker(bind=engine)
    session = Session()
    estados = session.query(Estado).all()
    session.close()
    return estados


def get_pregunta_db():
    Session = sessionmaker(bind=engine)
    session = Session()
    preguntas = session.query(Pregunta).all()
    session.close()
    return preguntas
