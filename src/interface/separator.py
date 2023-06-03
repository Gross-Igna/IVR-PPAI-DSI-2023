import tkinter as tk
from tkinter import ttk


# TODO: revisar separador
# parece que crea la linea pero muy chica y no llega a verse
class Separator(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.linea_divisoria = ttk.Separator(self, orient="horizontal")
        self.linea_divisoria.pack(fill="x", padx=10)
