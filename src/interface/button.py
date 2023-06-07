import tkinter as tk
from tkinter import messagebox
from src.interface.combobox import Combobox


def mostrar_exito():
    messagebox.showinfo("Éxito", "Se ha generado con éxito!")


class Button(tk.Frame):
    def __init__(self, master, placeholder):
        super().__init__(master)

        if placeholder == "Aceptar":
            self.button = tk.Button(self, text=placeholder, command=mostrar_exito, state='normal')
            self.button.pack(pady=10)
        elif placeholder == "Buscar Llamadas":
            print('llego al boton')
            self.button = tk.Button(self, text=placeholder, command=self.set_cambio_de_estado, state='normal')
            self.button.pack(pady=10)
        else:
            print('salio por el else')
            self.button = tk.Button(self, text=placeholder,)
            self.button.pack(pady=5)

    def set_cambio_de_estado(self):
        print('Cambio de estado')
        self.precionado = True

        print(f'estado boton: {self.precionado}')

    def get_cambio_de_estado(self):
        print("devolviendo el cambio de estado")
        return self.precionado


#    def get_fechas(self):
#        if self.fecha_selector:
#            fechas = self.fecha_selector.get_fecha_seleccionada()
#            return fechas
#        #  retorna [6/14/2023, 05/14/2023]
#    def get_llamada_seleccionada(self):
#        if self.llamada_seleccionada:
#            llamada = self.llamada_seleccionada
#            return llamada
#