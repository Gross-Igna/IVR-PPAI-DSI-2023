import tkinter as tk
from tkcalendar import DateEntry
from src.interface.label import Label


class FechasSelector(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.frame_fechas = tk.Frame(self)
        self.frame_fechas.pack()

        self.label_inicio = Label(self.frame_fechas, "Fecha de Inicio")
        self.label_inicio.pack(side="left")

        self.cal_inicio = DateEntry(self.frame_fechas, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.cal_inicio.pack(side="left", padx=5)

        self.label_fin = Label(self.frame_fechas, "Fecha de fin")
        self.label_fin.pack(side="left")

        self.cal_fin = DateEntry(self.frame_fechas, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.cal_fin.pack(side="left", padx=5)

    def get_fecha_seleccionada(self):
        return self.cal_inicio.get(), self.cal_fin.get()

        # retorna 6/14/2023, 05/14/2023

