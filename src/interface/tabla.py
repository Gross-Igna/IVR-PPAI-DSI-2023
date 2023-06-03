import tkinter as tk
from tkinter import ttk


class Tabla(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.tabla = ttk.Treeview(self, columns=("Respuesta",))
        self.tabla.heading("#0", text="Pregunta")
        self.tabla.heading("Respuesta", text="Respuesta")
        self.tabla.pack(pady=10, padx=10, fill="both", expand=True)
