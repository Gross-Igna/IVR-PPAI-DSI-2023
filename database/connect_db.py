from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///bdIvr.db')
# puedes utilizar la ruta relativa si la base de datos se encuentra en el mismo
# directorio que el script

try:
    with engine.connect() as connection:
        result = connection.execute(text('SELECT SQLITE_VERSION()'))
        print(result.scalar())
except Exception as e:
    print(f"Error de conexión: {str(e)}")
