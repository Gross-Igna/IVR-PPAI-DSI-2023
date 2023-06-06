import tkinter as tk
from tkinter import messagebox
from src.interface.combobox import Combobox


def mostrar_exito():
    messagebox.showinfo("Éxito", "Se ha generado con éxito!")


class Button(tk.Frame):
    def __init__(self, master, placeholder, fecha_selector=None, llamadas_en_periodo=None):
        super().__init__(master)

        self.fecha_selector = fecha_selector

        if placeholder == "Aceptar":
            self.button = tk.Button(self, text="Aceptar", command=mostrar_exito, state='normal')
            self.button.pack(pady=10)
        elif placeholder == "Buscar Llamadas":
            self.button = tk.Button(self, text="Buscar Llamadas", command=llamadas_en_periodo, state='normal')
            self.button.pack(pady=10)
            # fechas_seleccionadas = self.get_fechas()
            # if len(llamadas_en_periodo) > 0:
            #     combobox_encuestas = Combobox(self, llamadas_en_periodo)
            #     combobox_encuestas.pack()
            #     self.llamada_seleccionada = combobox_encuestas.get_llamada()
            # else:
            #     messagebox.showinfo("Éxito", "No hay llamadas en el periodo seleccionado.")
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
