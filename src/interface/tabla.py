import tkinter as tk
from tkinter import ttk


class Tabla(tk.Frame):
    def __init__(self, master, pregs, respuestas):
        super().__init__(master)

        self.tabla = ttk.Treeview(self, columns=("Pregunta", "Respuesta"))
        self.tabla.heading("#0", text="Pregunta")
        self.tabla.heading("Respuesta", text="Respuesta")
        for i, pregunta in enumerate(pregs):
            self.tabla.insert("", "end", text=pregunta, values=(respuestas[i],))

        self.tabla.pack(pady=10, padx=10, fill="both", expand=True)