import tkinter as tk


class MarcoDescripcion(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.marco_descripcion = tk.Frame(self, bd=2, relief="groove")
        self.marco_descripcion.pack(pady=10)

        etiqueta_descripcion = tk.Label(self.marco_descripcion, text="Descripción:")
        etiqueta_descripcion.pack()

        texto_descripcion = tk.Text(self.marco_descripcion, height=4, width=40)
        texto_descripcion.pack(fill="both", expand=True)