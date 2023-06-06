import tkinter as tk
from tkinter import ttk


class Combobox(tk.Frame):
    def __init__(self, master, datos):
        super().__init__(master)

        self.combobox = tk.ttk.Combobox(self, values=datos)
        self.combobox.pack(pady=5)

