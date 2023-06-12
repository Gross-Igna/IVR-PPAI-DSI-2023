import tkinter as tk
from tkinter import ttk, messagebox
from src.classes.GestorConsultarEncuestas import GestorConsultarEncuestas

# Crear la ventana principal
window = tk.Tk()
window.title("Consultar Encuesta")

class PantallaConsultarEncuesta():
    def __init__(self):
        super().__init__()
    
    def opConsultarEncuesta(self):
        self.habilitarPantalla()

    def habilitarPantalla(self):
        label_buscar_llamadas = tk.Label(window, text="Buscar Llamadas")
        label_buscar_llamadas.pack()

        gestor = GestorConsultarEncuestas()
        gestor.consultarEncuesta(self, window)

        window.mainloop()

    def solicitarSeleccionPeriodo(self,gestor):
        label_buscar_llamadas = tk.Label(window, text="Buscar Llamadas")
        label_buscar_llamadas.pack()

        # Crear el contenedor para los inputs
        frame_inputs = tk.Frame(window)
        frame_inputs.pack()

        fecha_desde = self.tomarFechaInicio(frame_inputs)
        fecha_hasta = self.tomarFechaFin(frame_inputs)

        print(fecha_desde, fecha_hasta)
        return fecha_desde, fecha_hasta

        # print("llega a solicitarseleccion periodo")  # llego
        # fecha_selector = FechasSelector(self)
        # fecha_selector.pack()
        # fecha_inicio = self.tomarFechaInicio(fecha_selector)
        # fecha_fin = self.tomarFechaFin(fecha_selector)
        # return fecha_inicio, fecha_fin

    def tomarFechaInicio(self, frame_inputs):
        # Crear el input de "Fecha desde"
        label_fecha_desde = tk.Label(frame_inputs, text="Fecha desde")
        label_fecha_desde.pack(side=tk.LEFT)

        entry_fecha_desde = tk.Entry(frame_inputs)
        entry_fecha_desde.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)
        fecha = entry_fecha_desde.get()
        return fecha

    def tomarFechaFin(self, frame_inputs):
        # Crear el input de "Fecha hasta"
        label_fecha_hasta = tk.Label(frame_inputs, text="Fecha hasta")
        label_fecha_hasta.pack(side=tk.LEFT)

        entry_fecha_hasta = tk.Entry(frame_inputs)
        entry_fecha_hasta.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)
        fecha= entry_fecha_hasta.get()

        return fecha

    def mostrarLlamadaEncuestaRespondida(self, llamadas: list, gestor):
        ##############
        combobox = Combobox(self, llamadas)
        combobox.pack()

        llamada_seleccionada = self.tomarSeleccionLlamada(combobox, gestor)
        # tomar seleccion llamada gestor
        print('en mostrar ll llamada seleccionaa', llamada_seleccionada)

        print(llamada_seleccionada)
        gestor.tomarSeleccionLlamada(llamada_seleccionada, self)

    def tomarSeleccionLlamada(self, combobox, gestor):
        print('llega a tomar seleccion en pantalla')
        llamada_seleccionada = combobox.get_llamada_selec_combo()
        #gestor.tomarSeleccionLlamada(llamada_seleccionada, self)
        return llamada_seleccionada

    def mostrarLlamadaEncuesta(self, datos_seleccionada, datos_encuesta):
        etiqueta = Etiqueta(self, datos_seleccionada[0], datos_seleccionada[1], datos_seleccionada[2])  # nombre
        etiqueta.pack()

        desc = MarcoDescripcion(self, datos_encuesta[0])
        desc.pack()

        tabla = Tabla(self, datos_encuesta[1], datos_seleccionada[3])  # datos_encuesta[0] encuesta, [1] preguntas, datos_selec[3] respuesta
        tabla.pack()

    #def tomarSeleccionPresentacion(self):
    #    opcion =
    #    gestor.tomarOpcionPresentacion(opcion)



