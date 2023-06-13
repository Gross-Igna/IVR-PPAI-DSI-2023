from src.database.db_utils import get_llamadas_db
# Contenido opcional en caso de que sea necesario inicializar algo en el paquete database

llamadas = get_llamadas_db()
print(len(llamadas))