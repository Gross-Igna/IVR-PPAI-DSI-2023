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

        # button_habilitar = Button(self, "Buscar Llamadas")
        # button_habilitar.pack()
        # self.fecha_llamada_seleccionada = button_habilitar.get_fechas()
        # deberia tener este valor: [6/14/2023, 05/14/2023]

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

        # label_generar = Label(self, "Generar Archivo")
        # label_generar.pack()

        radio_buttons = RadioButton(self)
        radio_buttons.pack()

        separador5 = Separator(self)
        separador5.pack()

        boton_aceptar = Button(self, "Aceptar")
        boton_aceptar.pack()
    
    def opConsultarEncuesta(self):
        print("Llego al consultar encuesta EN PANTALLA")
        self.habilitarPantalla()

    def habilitarPantalla(self):
        print("LLego al habilitar pantalla")
        gestor = GestorConsultarEncuestas()
        gestor.consultarEncuesta(self)
        # self.mainloop()


    def solicitarSeleccionPeriodo(self):
        print("llega a solicitarseleccion periodo")  # llego
        fecha_selector = FechasSelector(self)
        fecha_selector.pack()
        fecha_inicio = self.tomarFechaInicio(fecha_selector)
        fecha_fin = self.tomarFechaFin(fecha_selector)
        return [fecha_inicio, fecha_fin]

    def tomarFechaInicio(self, fecha_selector):
        fecha_inicio = fecha_selector.get_fecha_seleccionada()
        return fecha_inicio[0]

    def tomarFechaFin(self, fecha_selector):
        fecha_fin = fecha_selector.get_fecha_seleccionada()
        return fecha_fin[1]

    def mostrarLlamadaEncuestaRespondida(self, llamadas: list):
        combobox = Combobox(self, llamadas)
        combobox.pack()

        llamada_seleccionada = self.tomarSeleccionLlamada(combobox)
        # tomar seleccion llamada gestor
        print(llamada_seleccionada)

    def tomarSeleccionLlamada(self, combobox):
        llamada_seleccionada = combobox.get_llamada_selec_combo()
        # TODO TRATAR DE CONSEGUIR AL GESTOR ACA
        # gestor.tomarSeleccionLlamada(llamada_seleccinada)
        return llamada_seleccionada

    def mostrarLlamadaEncuesta(self):

    def tomarSeleccionPresentacion(self):
        opcion =
        gestor.tomarOpcionPresentacion(opcion)



