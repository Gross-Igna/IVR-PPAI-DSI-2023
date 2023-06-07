import tkinter as tk
from tkcalendar import DateEntry
from tkinter import messagebox, ttk


estado_consulta = False
estado_busqueda = False


# Manejo de estado del boton busqueda
def toggle_busqueda():
    global estado_busqueda
    estado_busqueda = not estado_busqueda
    if estado_busqueda:
        combobox_encuestas['state'] = 'readonly'
        boton_consultar['state'] = 'normal'
    else:
        pass


# Manejo de estado del boton consulta
def toggle_estado():
    global estado_consulta
    estado_consulta = not estado_consulta

    if estado_consulta:
        texto.delete("1.0", tk.END)  # Borra el contenido existente en el widget de texto
        for item in lista_llamadas:
            texto.insert(tk.END, item + "\n")  # Agrega cada string de la lista en una nueva línea
            boton_mostrar_llamada['state'] = 'normal'
    else:
        texto.delete("1.0", tk.END)  # Borra el contenido existente en el widget de texto

        boton_mostrar_llamada['state'] = 'normal'


# manejo de datos de la llamada
def mostrar_llamada():
    estado = "Estado de la llamada"  # Obtén el nombre del estado de la llamada
    cliente = "Nombre del cliente"  # Obtén el nombre del cliente de la llamada
    duracion = "Duración de la llamada"  # Obtén la duración de la llamada
    descripcion = "Descripción de la llamada"  # Obtén la descripción de la llamada
    respuestas = {
        "Pregunta 1": "Respuesta 1",
        "Pregunta 2": "Respuesta 2",
        "Pregunta 3": "Respuesta 3"
    }  # Obtén las respuestas seleccionadas

    # Mostrar estado, cliente y duración
    etiqueta_estado.config(text="Estado: {}".format(estado))
    etiqueta_cliente.config(text="Cliente: {}".format(cliente))
    etiqueta_duracion.config(text="Duración: {}".format(duracion))

    # Mostrar descripción
    texto_descripcion.configure(state="normal")
    texto_descripcion.delete("1.0", tk.END)
    texto_descripcion.insert(tk.END, descripcion)
    texto_descripcion.configure(state="disabled")

    # Limpiar la tabla de preguntas y respuestas
    tabla.delete(*tabla.get_children())

    # Mostrar las respuestas en la tabla
    for pregunta, respuesta in respuestas.items():
        tabla.insert("", tk.END, text=pregunta, values=(respuesta,))

# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
def mostrar_exito():
    messagebox.showinfo("Éxito", "Se ha generado con éxito!")


# ----------------------------------------------------------------------------------
def consultar_encuesta():
    periodo_inicio = cal_inicio.get_date()
    periodo_fin = cal_fin.get_date()
    encuesta_seleccionada = combobox_encuestas.get()

    # Aquí puedes realizar las acciones necesarias con el periodo de fechas y la encuesta seleccionada

    # Ejemplo de impresión de los datos seleccionados
    print("Periodo seleccionado:")
    print("Fecha de inicio:", periodo_inicio)
    print("Fecha de fin:", periodo_fin)
    print("Encuesta seleccionada:", encuesta_seleccionada)

    boton_mostrar_llamada['state'] = 'normal'  # Habilitar el botón "Mostrar Llamada"

# ----------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Consultar encuesta")

# Crear el título
titulo = tk.Label(ventana, text="Seleccionar Llamada", font=("Arial", 16))
titulo.pack(pady=10)

linea_divisoria = ttk.Separator(ventana, orient="horizontal")
linea_divisoria.pack(fill="x", padx=10)

# Crear los DateEntry para seleccionar el periodo de fechas
frame_fechas = tk.Frame(ventana)
frame_fechas.pack()

label_inicio = tk.Label(frame_fechas, text="Fecha de inicio")
label_inicio.pack(side="left")

cal_inicio = DateEntry(frame_fechas, width=12, background='darkblue', foreground='white', borderwidth=2)
cal_inicio.pack(side="left", padx=5)

label_fin = tk.Label(frame_fechas, text="Fecha de fin")
label_fin.pack(side="left")

cal_fin = DateEntry(frame_fechas, width=12, background='darkblue', foreground='white', borderwidth=2)
cal_fin.pack(side="left", padx=5)

# Crear el botón para habilitar el combobox de encuestas
boton_habilitar = tk.Button(ventana, text="Buscar Llamadas", command=toggle_busqueda)
boton_habilitar.pack(pady=5)

# Crear el título
label_titulo = tk.Label(ventana, text="Seleccionar llamada")
label_titulo.pack()

# Crear el combobox para seleccionar la encuesta (inicialmente deshabilitado)
Llamada = ["LLamada 1", "Llamada 2", "Llamada 3"]  # Ejemplo de encuestas disponibles, puedes modificarlo según tus necesidades
combobox_encuestas = tk.ttk.Combobox(ventana, values=Llamada, state='disabled')
combobox_encuestas.pack(pady=5)

# Crear el botón de consultar
boton_consultar = tk.Button(ventana, text="Consultar", command=toggle_estado, state='disabled')
boton_consultar.pack(pady=10)

texto = tk.Text(ventana, height=5, width=30)
texto.pack(padx=10, pady=10)

lista_llamadas = ["id = 1 , Fecha de Llamada = 00/00/0000"]

# Crear el botón para mostrar los detalles de la llamada (inicialmente deshabilitado)
boton_mostrar_llamada = tk.Button(ventana, text="Mostrar Llamada", command=mostrar_llamada, state='disabled')
boton_mostrar_llamada.pack(pady=10)

linea_divisoria = ttk.Separator(ventana, orient="horizontal")
linea_divisoria.pack(fill="x", padx=10)


# Crear los elementos para mostrar los detalles de la llamada
frame_detalles = tk.Frame(ventana)
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

linea_divisoria = ttk.Separator(ventana, orient="horizontal")
linea_divisoria.pack(fill="x", padx=10)

tabla = ttk.Treeview(frame_detalles, columns=("pregunta", "Respuesta"))
tabla.heading("#0", text="Pregunta probdano")
tabla.heading("Respuesta", text="Respuesta probando ")
tabla.pack(pady=10, padx=10, fill="both", expand=True)
frame_opciones = tk.Frame(ventana)
frame_opciones.pack()

linea_divisoria = ttk.Separator(ventana, orient="horizontal")
linea_divisoria.pack(fill="x", padx=10)

label_generar = tk.Label(frame_opciones, text="Generar archivo:")
label_generar.pack(side="left")

opcion_var = tk.StringVar()
opcion_var.set("CSV")

radio_csv = tk.Radiobutton(frame_opciones, text="CSV", variable=opcion_var, value="CSV")
radio_csv.pack(side="left")

radio_imprimir = tk.Radiobutton(frame_opciones, text="Imprimir", variable=opcion_var, value="Imprimir")
radio_imprimir.pack(side="left")

boton_aceptar = tk.Button(ventana, text="Aceptar", command=mostrar_exito, state='normal')
boton_aceptar.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
