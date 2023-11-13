import tkinter as tk
from tkinter import ttk, messagebox
from src.classes.GestorConsultarEncuestas import GestorConsultarEncuestas

gestor = None
# Crear la ventana principal
window = tk.Tk()
window.title("Consultar Encuesta")


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

        button_buscar = tk.Button(window, text="Buscar", command=lambda: botonBuscar(self, gestor, entry_fecha_desde, entry_fecha_hasta))
        button_buscar.pack(pady=10)

        button_cancelar = tk.Button(window, text="Cancelar", bg="salmon", command=exit)
        button_cancelar.pack(pady=10, side="bottom")

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
        self.solicitarSeleccionLlamada(llamadas, gestor)

    def solicitarSeleccionLlamada(self, llamadas, gestor):
        label_titulo = tk.Label(window, text="Seleccionar llamada")
        label_titulo.pack()
        if len(llamadas) > 0:
            state = 'normal'
        else:
            state = 'disabled'

        fechasDeLlamadas = []
        for i in range(len(llamadas)):
            fechasDeLlamadas.append(llamadas[i].getFechaHoraInicio())

        # Crear el combobox para seleccionar la encuesta (inicialmente deshabilitado)
        combobox_encuestas = tk.ttk.Combobox(window, state=state, values=fechasDeLlamadas)
        combobox_encuestas.pack(pady=5)

        button_seleccionar = tk.Button(window, text="Seleccionar",
                                  command=lambda: botonSeleccionarLlamada(self, gestor, combobox_encuestas))
        button_seleccionar.pack(pady=10)

        linea_divisoria = ttk.Separator(window, orient="horizontal")
        linea_divisoria.pack(fill="x", padx=10)

    def tomarSeleccionLlamada(self, dropdown):
        llamada_seleccionada = dropdown.get()
        return llamada_seleccionada

    def mostrarLlamadaEncuesta(self, datos_seleccionada, datos_encuesta, gestor):

        frame_detalles = tk.Frame(window)
        frame_detalles.pack(pady=10)

        etiqueta_estado = tk.Label(frame_detalles, text="Estado: ")
        etiqueta_estado.pack()

        etiqueta_cliente = tk.Label(frame_detalles, text="Cliente: ")
        etiqueta_cliente.pack()

        etiqueta_duracion = tk.Label(frame_detalles, text="Duración: ")
        etiqueta_duracion.pack()

        marco_descripcion = tk.Frame(frame_detalles, bd=2, relief="groove")
        marco_descripcion.pack(pady=10)

        etiqueta_descripcion = tk.Label(marco_descripcion, text="Descripción:")
        etiqueta_descripcion.pack()

        texto_descripcion = tk.Text(marco_descripcion, height=4, width=40)
        texto_descripcion.pack(fill="both", expand=True)
        texto_descripcion.configure(state="disabled")

        linea_divisoria = ttk.Separator(window, orient="horizontal")
        linea_divisoria.pack(fill="x", padx=10)

        tabla = ttk.Treeview(frame_detalles, columns=("Respuesta",))
        tabla.heading("#0", text="Pregunta")
        tabla.heading("Respuesta", text="Respuesta")
        tabla.pack(pady=10, padx=10, fill="both", expand=True)

        frame_opciones = tk.Frame(window)
        frame_opciones.pack()

        linea_divisoria = ttk.Separator(window, orient="horizontal")
        linea_divisoria.pack(fill="x", padx=10)

        etiqueta_estado.config(text="Estado: {}".format(datos_seleccionada[2]))
        etiqueta_cliente.config(text="Cliente: {}".format(datos_seleccionada[0]))
        etiqueta_duracion.config(text="Duración: {}".format(datos_seleccionada[1]))

        # Mostrar descripción
        texto_descripcion.configure(state="normal")
        texto_descripcion.delete("1.0", tk.END)
        texto_descripcion.insert(tk.END, datos_encuesta[0])
        texto_descripcion.configure(state="disabled")

        preguntas = datos_encuesta[1]
        respuestas = datos_seleccionada[3]

        # Limpiar la tabla de preguntas y respuestas
        tabla.delete(*tabla.get_children())
        for i in range(len(preguntas)):
            tabla.insert("", tk.END, text=preguntas[i], values=(respuestas[i]))

        self.solicitarSeleccionPresentacion(datos_seleccionada, datos_encuesta, gestor)

    def solicitarSeleccionPresentacion(self, datos_seleccionada, datos_encuesta, gestor):
        frame_opciones = tk.Frame(window)
        frame_opciones.pack()

        linea_divisoria = ttk.Separator(window, orient="horizontal")
        linea_divisoria.pack(fill="x", padx=10)

        label_generar = tk.Label(frame_opciones, text="Generar archivo:")
        label_generar.pack(side="left")

        opcion_var = tk.StringVar()
        opcion_var.set("CSV")

        radio_csv = tk.Radiobutton(frame_opciones, text="CSV", variable=opcion_var, value="CSV")
        radio_csv.pack(side="left")

        radio_imprimir = tk.Radiobutton(frame_opciones, text="Imprimir", variable=opcion_var, value="Imprimir")
        radio_imprimir.pack(side="left")

        boton_aceptar = tk.Button(window, text="Aceptar", command=lambda :mostrar_exito(self, gestor, datos_seleccionada, datos_encuesta), state='normal')
        boton_aceptar.pack(pady=10)

    def tomarOpcionPresentacion(self, gestor, datos_seleccionada, datos_encuesta):
        gestor.tomarOpcionDePresentacion(datos_seleccionada, datos_encuesta)

    def no_hay_llamadas(self):
        messagebox.showinfo("No hay llamadas", "No se encontraron llamadas en este periodo.")
        # exit()

def botonBuscar(pantalla, gestor, entry_desde, entry_hasta):
    fechaDesde = pantalla.tomarFechaInicio(entry_desde)
    fechaHasta = pantalla.tomarFechaFin(entry_hasta)

    gestor.tomarFechaInicio(fechaDesde)
    gestor.tomarFechaFin(fechaHasta)

    gestor.obtenerLlamadasPeriodoConEncuesta(pantalla)
    # TODO tomar fechas debe llamar a los metodos

def botonSeleccionarLlamada(pantalla, gestor, dropdow):
    llamada_seleccionada = pantalla.tomarSeleccionLlamada(dropdow)
    gestor.tomarSeleccionLlamada(llamada_seleccionada)
    gestor.mostrarLlamadaSeleccionada(llamada_seleccionada, pantalla)


def mostrar_exito(pantalla, gestor, datos_seleccionada, datos_encuesta):
    messagebox.showinfo("Éxito", "Se ha generado con éxito!")
    pantalla.tomarOpcionPresentacion(gestor, datos_seleccionada, datos_encuesta)

