import tkinter as tk


# TODO: podemos pasar los datos de las etiquetas por parametro
class Etiqueta(tk.Frame):
    def __init__(self, master, nombre, duracion, estado):
        super().__init__(master)

        self.etiqueta_cliente = tk.Label(self, text=f"Nombre del Cliente: {nombre}")
        self.etiqueta_duracion = tk.Label(self, text=f"Duracion: {duracion}")
        self.etiqueta_estado = tk.Label(self, text=f"Estado: {estado}")

        self.etiqueta_cliente.pack()
        self.etiqueta_duracion.pack()
        self.etiqueta_estado.pack()
