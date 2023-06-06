import tkinter as tk
from tkinter import ttk


class Combobox(tk.Frame):
    def __init__(self, master, datos):
        super().__init__(master)

        self.combobox = tk.ttk.Combobox(self, values=datos)
        self.combobox.pack(pady=5)

    def get_llamada(self):
        llamada = self.combobox.get()
        # retorna la fecha de la llamada (__fechaHoraInicio)
        return llamada
