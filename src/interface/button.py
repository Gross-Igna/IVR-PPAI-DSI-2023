import tkinter as tk
from tkinter import messagebox

# def toggle_busqueda():
#     global estado_busqueda
#     estado_busqueda = not estado_busqueda
#     if estado_busqueda:
#         combobox_encuestas['state'] = 'readonly'
#         boton_consultar['state'] = 'normal'
#     else:
#         pass


# TODO: necesitamos poder mandarle al botton una accion para poder ejecutar funciones cuando corresponda
# para salir del apuro utilice un if para controlar el boton segun el placeholder que se mande
# posiblemente haya una mejor manera de hacer esto
def mostrar_exito():
    messagebox.showinfo("Éxito", "Se ha generado con éxito!")


class Button(tk.Frame):
    def __init__(self, master, placeholder):
        super().__init__(master)

        if placeholder == "Aceptar":
            self.button = tk.Button(self, text="Aceptar", command=mostrar_exito, state='normal')
            self.button.pack(pady=10)
        else:
            self.button = tk.Button(self, text=placeholder,)
            self.button.pack(pady=5)

