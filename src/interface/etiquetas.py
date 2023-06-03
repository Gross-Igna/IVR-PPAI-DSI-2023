import tkinter as tk


# TODO: podemos pasar los datos de las etiquetas por parametro
class Etiqueta(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.etiqueta_estado = tk.Label(self, text="Estado: ")
        self.etiqueta_cliente = tk.Label(self, text="Cliente: ")
        self.etiqueta_descripcion = tk.Label(self, text="Descripcion: ")

        self.etiqueta_estado.pack()
        self.etiqueta_cliente.pack()
        self.etiqueta_descripcion.pack()
