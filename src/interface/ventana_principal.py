import tkinter as tk
from tkinter import messagebox

from fechas_selector import FechasSelector
from titulo import Titulo
from button import Button
from combobox import Combobox
from box_texto import TextoBox
from separator import Separator
from etiquetas import Etiqueta
from marco_descripcion import MarcoDescripcion
from tabla import Tabla
from label import Label
from radio_buttons import RadioButton


# este es nuestro gestor

def obtener_llamadas_periodo_con_encuesta(fechas):
    llamadas_p_encuestas = []
    for llamada in llamadas:
        if llamada.es_de_periodo(fechas):
            llamadas_p_encuestas.append(llamada)

    return llamadas_p_encuestas


def obtener_llamada_por_fecha(fecha_llamada):
    for llamada in llamadas:
        if llamada.__fechaHoraInicio == fecha_llamada:
            return llamada


class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Consultar encuesta")

        titulo = Titulo(self, "Seleccionar Llamada")
        titulo.pack()

        separador_inicial = Separator(self)
        separador_inicial.pack()
        # Selecionar fechas

        fecha_selector = FechasSelector(self)
        fecha_selector.pack()

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


# deberiamos tener hardcodeados las llamadas
llamadas = []


if __name__ == "__main__":
    ventana = VentanaPrincipal()
    ventana.mainloop()
