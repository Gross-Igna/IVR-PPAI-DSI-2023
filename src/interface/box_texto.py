import tkinter as tk


class TextoBox(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.texto = tk.Text(self, height=5, width=30)
        self.texto.pack(padx=10, pady=10)