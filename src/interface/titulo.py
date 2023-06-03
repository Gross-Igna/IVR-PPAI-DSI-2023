import tkinter as tk


class Titulo(tk.Frame):
    def __init__(self, master, titulo: str):
        super().__init__(master)

        self.titulo = tk.Frame(self)
        self.titulo.pack()
        # Crear el título
        self.titulo_label = tk.Label(self.titulo,text=titulo, font=("Arial", 16))
        self.titulo_label.pack(pady=10)
