import tkinter as tk
from tkinter import messagebox
from src.interface.combobox import Combobox


llamadas = []
def mostrar_exito():
    messagebox.showinfo("Éxito", "Se ha generado con éxito!")


# TODO como recorrer desde aca las llamadas, pasar como parametro al boton ?
# o traer de la base de datos ? deberiamos traerlas de las base de datos

def obtener_llamadas_periodo_con_encuesta(fechas):
    llamadas_p_encuestas = []
    for llamada in llamadas:
        if llamada.es_de_periodo(fechas):
            llamadas_p_encuestas.append(llamada)

    return llamadas_p_encuestas


class Button(tk.Frame):
    def __init__(self, master, placeholder, fecha_selector=None):
        super().__init__(master)

        self.fecha_selector = fecha_selector

        if placeholder == "Aceptar":
            self.button = tk.Button(self, text="Aceptar", command=mostrar_exito, state='normal')
            self.button.pack(pady=10)
        elif placeholder == "Buscar Llamadas":
            self.button = tk.Button(self, text="Buscar Llamadas", command=self.get_fechas, state='normal')
            self.button.pack(pady=10)
            fechas_seleccionadas = self.get_fechas()
            llamadas_en_periodo = obtener_llamadas_periodo_con_encuesta(fechas_seleccionadas)
            if len(llamadas_en_periodo) > 0:
                combobox_encuestas = Combobox(self, llamadas_en_periodo)
                combobox_encuestas.pack()
                self.llamada_seleccionada = combobox_encuestas.get_llamada()
            else:
                messagebox.showinfo("Éxito", "No hay llamadas en el periodo seleccionado.")
        else:
            self.button = tk.Button(self, text=placeholder,)
            self.button.pack(pady=5)

    def get_fechas(self):
        if self.fecha_selector:
            fechas = self.fecha_selector.get_fecha_seleccionada()
            return fechas

    def get_llamada_seleccionada(self):
        if self.llamada_seleccionada:
            llamada = self.llamada_seleccionada
            return llamada
