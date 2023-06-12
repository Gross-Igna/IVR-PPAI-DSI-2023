import tkinter as tk
from ..classes.Llamada import llamadas
from src.interface.button import Button
from ..classes.Encuesta import encuestas
from tkinter import ttk, messagebox


class GestorConsultarEncuestas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.__fechaFinPeriodo = None
        self.__fechaInicioPeriodo = None
        self.__llamadas = None
        self.__llamadaSeleccionada = None
        self.__opcionPresentacion = None

    def getFechaFinPeriodo(self):
        return self.__fechaFinPeriodo

    def tomarFechaFin(self, fecha_fin):
        self.__fechaFinPeriodo = fecha_fin

    def getFechaInicioPeriodo(self):
        return self.__fechaInicioPeriodo

    def tomarFechaInicio(self, fecha_in):
        self.__fechaInicioPeriodo = fecha_in

    def getLlamadas(self):
        return self.__llamadas

    def setLlamadas(self, llamadas):
        self.__llamadas = llamadas

    def getLlamadaSeleccionada(self):
        return self.__llamadaSeleccionada

    def setLlamadaSeleccionada(self, llamada):
        self.__llamadaSeleccionada = llamada

    def getOpcionPresentacion(self):
        return self.__opcionPresentacion

    def setOpcionPresentacion(self, opcion):
        self.__opcionPresentacion = opcion

    def consultarEncuesta(self, pantalla,window):
        fecha_inicio, fecha_fin = pantalla.solicitarSeleccionPeriodo(self)




        button_buscar = tk.Button(window, text="Buscar", command=self.obtenerLlamadasPeriodoConEncuesta())
        button_buscar.pack(pady=10)

        linea_divisoria = ttk.Separator(window, orient="horizontal")
        linea_divisoria.pack(fill="x", padx=10)

        self.tomarFechaInicio(fecha_inicio)
        self.tomarFechaFin(fecha_fin)
        print(f'fehca inicio:', fecha_inicio)

        self.obtenerLlamadasPeriodoConEncuesta()
        # fecha_inicio, fecha_fin = pantalla.solicitarSeleccionPeriodo()
        # boton = Button(pantalla, "Buscar Llamadas")
        # boton.pack()
        # self.tomarFechaInicio(fecha_inicio)
        # self.tomarFechaFin(fecha_fin)
        # llamadas_PyE = self.obtenerLlamadasPeriodoConEncuesta()
        # print(llamadas_PyE)
        # pantalla.mostrarLlamadaEncuestaRespondida(llamadas_PyE, self)

    def obtenerLlamadasPeriodoConEncuesta(self):
        llamadas_p_encuestas = []
        fecha1 = self.getFechaInicioPeriodo()
        if fecha1 != '':
            for llamada in llamadas:
                print('entro al for de obetener llamadas perdiod con encuetas')
                if llamada.esDePeriodo(self.__fechaInicioPeriodo, self.__fechaFinPeriodo):
                    print('lo agrega al arreglo ')
                    llamadas_p_encuestas.append(llamada.getFechaHoraInicio())

        return llamadas_p_encuestas

    def tomarSeleccionLlamada(self, llamada_seleccionada, pantalla):
        self.setLlamadaSeleccionada(llamada_seleccionada)
        print("tomarSelec", llamada_seleccionada)
        self.mostrarLlamadaSeleccionada(llamada_seleccionada, pantalla)

    def mostrarLlamadaSeleccionada(self, llamada_fecha, pantalla):
        # buscar la llamad
        print("fecha seleccionada", llamada_fecha)
        for i in range(len(llamadas)):
            fecha_iteradora = llamadas[i].getFechaHoraInicio()
            if fecha_iteradora == llamada_fecha:
                indice = i
        # BORRAR SI O SI
        indice = 0
        LA_llamada = llamadas[indice]
        datos_seleccionada = LA_llamada.mostrarLlamada()
        #  return [nombre_cli, duracion, nombre_est, descripciones[]]
        datos_encuesta = []
        fecha_encuesta = LA_llamada.buscarFechaEncuesta()
        for encuesta in encuestas:
            es_vigente = encuesta.vigenteParaLaFecha(fecha_encuesta)
            if es_vigente:
                datos_encuesta = encuesta.getDescripcionEncuesta()
                # datos_encuesta = ["encuesta 1", ["¿como calificaria..."]]
        if len(datos_encuesta):
            pantalla.mostrarLlamadaEncuesta(datos_seleccionada, datos_encuesta)
        else:
            print('sorry bro')


    #def tomarSeleccionDePresentacion(self,opcion):
    #    self.setOpcionPresentacion(opcion)
    #    generador = GeneradorCSV()
    #    generador.generar_csv_de_llamada()
