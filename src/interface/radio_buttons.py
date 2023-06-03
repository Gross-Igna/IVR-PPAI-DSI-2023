import tkinter as tk


# TODO: revisar opciones
# deberíamos ejecutar las funciones correspondientes dependiendo la opcion que se elija

class RadioButton(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.opcion_var = tk.StringVar()
        self.opcion_var.set("CSV")

        self.radio_csv = tk.Radiobutton(self, text="CSV", variable=self.opcion_var, value="CSV")
        self.radio_csv.pack(side="left")

        self.radio_imprimir = tk.Radiobutton(self, text="Imprimir", variable=self.opcion_var, value="Imprimir")
        self.radio_imprimir.pack(side="left")

