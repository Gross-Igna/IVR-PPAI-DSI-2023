import csv

class GeneradorCSV:
    def __init__(self):
        super().__init__()

    def generarCSVdeLlamada(self, cliente, estado, duracion, preguntas, respuestas):
        preg_resp = []
        encabezado = [f'Cliente: {cliente}', f'Estado: {estado}', f'Duracion: {duracion} segundos']
        for i in range(len(preguntas)):
            preg_resp.append({
                'Pregunta': preguntas[i],
                'Respuesta': respuestas[i]})

        with open('llamada.csv', mode='w', newline="") as file:

            encabezado_writer = csv.writer(file, delimiter=' ', quotechar='|')
            # probar con: encabezado_writer = csv.writer(file, delimiter=',')
            encabezado_writer.writerow(encabezado)

            writer = csv.DictWriter(file, delimiter=',', fieldnames=['Pregunta', 'Respuesta'])
            writer.writeheader()

            for i in preg_resp:
                writer.writerow(i)


