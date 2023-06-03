import tkinter as tk


class Label(tk.Frame):
    def __init__(self, master, texto):
        super().__init__(master)

        self.label = tk.Label(self, text=texto)
        self.label.pack(side="left")
