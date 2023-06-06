# class PantallaConsultarEncuesta:
#     def __init__(self):
#         self.__fechaFinPeriodo = None
#         self.__fechaInicioPeriodo = None
#         self.__llamadas = None
#         self.__llamadaSeleccionada = None
#         self.__opcionPresentacion = None

#     def getFechaFinPeriodo(self):
#         return self.fechaFinPeriodo

#     def tomarFechaInicio(self, fecha):
#         self.__fechaFinPeriodo = fecha

#     def getFechaInicioPeriodo(self):
#         return self.__fechaInicioPeriodo

#     def tomarFechaFin(self, fecha):
#         self.__fechaInicioPeriodo = fecha

#     def mostrarLlamadasEncuestaRespondida(self):
#         return self.__llamadas

#     def setLlamadas(self, llamadas):
#         self.__llamadas = llamadas

#     def getLlamadaSeleccionada(self):
#         return self.__llamadaSeleccionada

#     def tomarSeleccionLlamada(self, llamada):
#         self.__llamadaSeleccionada = llamada

#     def getOpcionPresentacion(self):
#         return self.__opcionPresentacion

#     def tomarOpcionPresentacion(self, opcion):
#         self.__opcionPresentacion = opcion

#     def opConsultarEncuesta():

#     def habilitarPantalla():

#     def solicitarSeleccionPeriodo():

#     def solicitarSeleccionLlamada():

#     def mostrarLlamadaEncuesta():

#     def solicitarSeleccionPresentacion():

import tkinter as tk
from tkinter import messagebox

from interface.fechas_selector import FechasSelector
from interface.titulo import Titulo
from interface.button import Button
from interface.combobox import Combobox
from interface.box_texto import TextoBox
from interface.separator import Separator
from interface.etiquetas import Etiqueta
from interface.marco_descripcion import MarcoDescripcion
from interface.tabla import Tabla
from interface.label import Label
from interface.radio_buttons import RadioButton

import GestorConsultarEncuestas

class PantallaConsultarEncuesta(tk.Frame):
    def __init__(self):
        super().__init__()

        self.title("Consultar encuesta")

        titulo = Titulo(self, "Seleccionar Llamada")
        titulo.pack()

        separador_inicial = Separator(self)
        separador_inicial.pack()
        # Selecionar fechas

        self.fecha_selector = FechasSelector(self)
        self.fecha_selector.pack()

        button_habilitar = Button(self, "Buscar Llamadas", fecha_selector)
        button_habilitar.pack()
        fecha_llamada_seleccionada = button_habilitar.get_llamada_seleccionada()

        button_consultar = Button(self, "Consultar Llamada")
        button_consultar.pack()

        texto_box = TextoBox(self)
        texto_box.pack()

        llamada_seleccionada = obtener_llamada_por_fecha(fecha_llamada_seleccionada)

        lista_llamadas = ["id = 1 , Fecha de Llamada = 00/00/0000"]
        # TODO mostrar la llamada seleccionada
        button_mostrar_llamada = Button(self, "Mostrar Llamadas")
        button_mostrar_llamada.pack()

        separador2 = Separator(self)
        separador2.pack()

        etiquetas = Etiqueta(self)
        etiquetas.pack()

        marco_desc = MarcoDescripcion(self)
        marco_desc.pack()

        separador3 = Separator(self)
        separador3.pack()
        # TODO: pasar los datos a la tabla por parametro
        tabla = Tabla(self)
        tabla.pack()

        separador4 = Separator(self)
        separador4.pack()

        label_generar = Label(self, "Generar Archivo")
        label_generar.pack()

        radio_buttons = RadioButton(self)
        radio_buttons.pack()

        separador5 = Separator(self)
        separador5.pack()

        boton_aceptar = Button(self, "Aceptar")
        boton_aceptar.pack()
    
    def opConsultarEncuesta(self):
        self.habilitarPantalla()

    def habilitarPantalla(self):
        self.mainloop()
        gestor = GestorConsultarEncuestas()
        gestor.consultarEncuesta(self)

    def solicitarSeleccionPeriodo():
        fechaInicio = self.tomarFechaInicio()
        fechaFin = self.tomarFechaFin()
        return [fechaInicio , fechaFin]

    def tomarFechaInicio():
        fechaInicio = self.fecha_llamada_seleccionada[0]
        return fechaInicio

    def tomarFechaFin():
        fechaFin = self.fecha_llamada_seleccionada[1]
        return fechaFin

    



    


    