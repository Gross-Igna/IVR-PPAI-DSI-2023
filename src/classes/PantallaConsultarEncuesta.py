import tkinter as tk
from src.interface.titulo import Titulo
from src.interface.button import Button
from src.interface.combobox import Combobox
from src.interface.box_texto import TextoBox
from src.interface.separator import Separator
from src.interface.etiquetas import Etiqueta
from src.interface.marco_descripcion import MarcoDescripcion
from src.interface.tabla import Tabla
from src.interface.label import Label
from src.interface.radio_buttons import RadioButton
from src.interface.fechas_selector import FechasSelector
from src.classes.GestorConsultarEncuestas import GestorConsultarEncuestas


class PantallaConsultarEncuesta(tk.Tk):
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

        button_habilitar = Button(self, "Buscar Llamadas", self.fecha_selector, 'las llamadas' )
        button_habilitar.pack()
        self.fecha_llamada_seleccionada = button_habilitar.get_fechas()

        button_consultar = Button(self, "Consultar Llamada")
        button_consultar.pack()

        texto_box = TextoBox(self)
        texto_box.pack()

        #llamada_seleccionada = obtener_llamada_por_fecha(fecha_llamada_seleccionada)

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

    def solicitarSeleccionPeriodo(self):
        fecha_inicio = self.tomarFechaInicio()
        fecha_fin = self.tomarFechaFin()
        return [fecha_inicio, fecha_fin]

    def tomarFechaInicio(self):
        fecha_inicio = self.fecha_llamada_seleccionada[0]
        return fecha_inicio

    def tomarFechaFin(self):
        fecha_fin = self.fecha_llamada_seleccionada[1]
        return fecha_fin

    def mostrarLlamadaEncuestaRespondida(self, llamadas: list):
        combobox = Combobox(self, llamadas)
