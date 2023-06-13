import tkinter as tk
from tkinter import ttk, messagebox
from src.classes.GestorConsultarEncuestas import GestorConsultarEncuestas

gestor = None
# Crear la ventana principal
window = tk.Tk()
window.title("Consultar Encuesta")


def botonHacerCosas(pantalla, gestor, entry_desde, entry_hasta):
    fechaDesde = pantalla.tomarFechaInicio(entry_desde)
    fechaHasta = pantalla.tomarFechaFin(entry_hasta)

    gestor.tomarFechaInicio(fechaDesde)
    gestor.tomarFechaFin(fechaHasta)

    print(f"fecha desde: {fechaDesde}, fecha hasta: {fechaHasta}")
    gestor.obtenerLlamadasPeriodoConEncuesta(pantalla)


def botonSeleccionarLlamada(pantalla, gestor, dropdow):
    llamada_seleccionada = pantalla.tomarSeleccionLlamada(dropdow)
    print(llamada_seleccionada)
    gestor.setLlamadaSeleccionada(llamada_seleccionada)
    gestor.mostrarLlamadaSeleccionada(llamada_seleccionada, pantalla)


class PantallaConsultarEncuesta:
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
        frame_inputs = tk.Frame(window)
        frame_inputs.pack()

        # Crear el input de "Fecha desde"
        label_fecha_desde = tk.Label(frame_inputs, text="Fecha desde")
        label_fecha_desde.pack(side=tk.LEFT)

        entry_fecha_desde = tk.Entry(frame_inputs)
        entry_fecha_desde.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)

        label_fecha_hasta = tk.Label(frame_inputs, text="Fecha hasta")
        label_fecha_hasta.pack(side=tk.LEFT)

        entry_fecha_hasta = tk.Entry(frame_inputs)
        entry_fecha_hasta.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)

        button_buscar = tk.Button(window, text="Buscar",command=lambda: botonHacerCosas(self, gestor, entry_fecha_desde, entry_fecha_hasta))
        button_buscar.pack(pady=10)

        linea_divisoria = ttk.Separator(window, orient="horizontal")
        linea_divisoria.pack(fill="x", padx=10)

    def tomarFechaInicio(self, entry_fecha_desde):
        fecha = entry_fecha_desde.get()
        return fecha

    def tomarFechaFin(self, entry_fecha_hasta):
        # Crear el input de "Fecha hasta"

        fecha = entry_fecha_hasta.get()

        return fecha

    def mostrarLlamadasEncuestaRespondida(self, llamadas: list, gestor):
        label_titulo = tk.Label(window, text="Seleccionar llamada")
        label_titulo.pack()
        if len(llamadas) > 0:
            state = 'normal'
        else:
            state = 'disabled'
        # Crear el combobox para seleccionar la encuesta (inicialmente deshabilitado)
        combobox_encuestas = tk.ttk.Combobox(window, state=state, values=llamadas)
        combobox_encuestas.pack(pady=5)

        button_buscar = tk.Button(window, text="Seleccionar",
                                  command=lambda: botonSeleccionarLlamada(self, gestor, combobox_encuestas))
        button_buscar.pack(pady=10)

        linea_divisoria = ttk.Separator(window, orient="horizontal")
        linea_divisoria.pack(fill="x", padx=10)

    def tomarSeleccionLlamada(self, dropdown):
        llamada_seleccionada = dropdown.get()
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



