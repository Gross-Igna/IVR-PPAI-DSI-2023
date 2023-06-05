import tkinter as tk
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
from src.database import db_utils as db


class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Consultar encuesta")

        titulo = Titulo(self, "Seleccionar Llamada")
        titulo.pack()

        separador_inicial = Separator(self)
        separador_inicial.pack()
        #TODO: ver trello
        fecha_selector = FechasSelector(self)
        fecha_selector.pack()

        button_habilitar = Button(self, "Buscar Llamadas")
        button_habilitar.pack()

        llamadas = db.get_llamadas_db()
        combobox_encuestas = Combobox(self, llamadas)
        combobox_encuestas.pack()

        button_consultar = Button(self, "Consultar Llamada")
        button_consultar.pack()

        texto_box = TextoBox(self)
        texto_box.pack()

        #TODO: hay que traer algo de la db aca?
        lista_llamadas = ["id = 1 , Fecha de Llamada = 00/00/0000"]

        button_mostrar_llamada = Button(self, "Mostrar Llamadas")
        button_mostrar_llamada.pack()

        separador2 = Separator(self)
        separador2.pack()

        # TODO: pasar datos de etiqueta por parametro
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


if __name__ == "__main__":
    ventana = VentanaPrincipal()
    ventana.mainloop()
