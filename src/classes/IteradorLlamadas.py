from abc import ABC, abstractmethod
from ..classes.Llamada import Llamada
from typing import List


class Iterator(ABC):
    @abstractmethod
    def siguiente(self):
        pass

    @abstractmethod
    def actual(self):
        pass

    @abstractmethod
    def ha_terminado(self):
        pass

    @abstractmethod
    def primero(self):
        pass

    @abstractmethod
    def cumple_filtros(self):
        pass


class IteratorLlamadas(Iterator):
    def __init__(self, filtros: List[str], llamadas: List[Llamada]):
        self.posicion_actual = 0
        self.filtros = filtros
        self.llamadas = llamadas
        self.llamadas_cumple_filtros = []

    def siguiente(self):
        self.posicion_actual += 1

    def ha_terminado(self):
        if self.posicion_actual > len(self.llamadas) - 1:
            return True
        else:
            return False

    def primero(self):
        self.posicion_actual = 0

    def actual(self):
        if self.cumple_filtros():
            self.llamadas_cumple_filtros.append(self.llamadas[self.posicion_actual])
            return self.llamadas[self.posicion_actual]

    def cumple_filtros(self):
        # [FechaInicio, FechaFin]
        es_de_periodo = self.llamadas[self.posicion_actual].esDePeriodo(self.filtros[0], self.filtros[1])
        if es_de_periodo:
            tiene_encuestas_resp = self.llamadas[self.posicion_actual].tieneEncuestaRespondida()
            if tiene_encuestas_resp:
                return True
            else:
                return False
