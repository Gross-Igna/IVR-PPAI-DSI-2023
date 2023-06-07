import csv


# TODO: revisar implementacion en radio buttons
class GeneradorCSV:
    def __init__(self, fecha):
        self.fechaCreacion = fecha

    def generarCSVdeLlamada(self, cliente, estado, duracion, preguntas, respuestas):
        preg_resp = []
        encabezado = [f'Cliente: {cliente}', f'Estado: {estado}', f'Duracion: {duracion} segundos']
        for i in range(len(preguntas)):
            preg_resp.append({
                'Pregunta': preguntas[i],
                'Respuesta': respuestas[i]})
    # probar con: preg_resp = [{'Pregunta': pregunta, 'Respuesta': respuesta} for pregunta, respuesta in zip(preguntas, respuestas)]

        with open('llamadas.csv', mode='w', newline="") as file:

            encabezado_writer = csv.writer(file, delimiter=' ', quotechar='|')
            # probar con: encabezado_writer = csv.writer(file, delimiter=',')
            encabezado_writer.writerow(encabezado)

            writer = csv.DictWriter(file, delimiter=',', fieldnames=['Pregunta', 'Respuesta'])
            writer.writeheader()

            for i in preg_resp:
                writer.writerow(i)


preguntas = ['¿Que tan satisfecho esta con el servicio brindado?', '¿Que tan probable es que recomiende nuestros '
                                                                   'servicios?']
respuestas = ['Muy satisfecho', 'Algo probable']
cliente = 'Juan Perez'
estado = 'Finalizada'
duracion = 255
x = []



