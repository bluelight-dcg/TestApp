
import psycopg2
from datetime import datetime, timedelta


# Detalles de conexión
hostname = "noo81.h.filess.io"
database = "Test321_partforty"
port = "61007"
username = "Test321_partforty"
password = "738242b8baa61ac0313372286db18b5a4dd0c4c0"

# Obtener todos los 

# Función para insertar una fila
def insert_row(word):
    """Inserta una palabra en la tabla nuevo_esquema.palabras."""
    try:
        with psycopg2.connect(
            database=database, user=username, password=password,
            host=hostname, port=port
        ) as conn:
            with conn.cursor() as cursor:
                insert_query = "INSERT INTO nuevo_esquema.palabras (word) VALUES (%s);"
                cursor.execute(insert_query, (word,))
                conn.commit()
    except psycopg2.Error as e:
        print(f"❌ Error al insertar la palabra: {e}")


#######

import psycopg2
from datetime import datetime, timedelta

# Database connection details
db_host = "1jstx.h.filess.io"
db_name = "Fdatabase_bearaskdo"
db_port = "61007"
db_user = "Fdatabase_bearaskdo"
db_password = "31f702ea3b6dcc967db964f87d2d5326092e987d"

# Function to insert a timestamp into the table
def insert_timestamp(value):
    """Inserts a timestamp into nuevo_esquema.palabras table."""
    try:
        with psycopg2.connect(
            database=db_name, user=db_user, password=db_password,
            host=db_host, port=db_port
        ) as connection:
            with connection.cursor() as cursor:
                query = "INSERT INTO nuevo_esquema.palabras (word) VALUES (%s);"
                cursor.execute(query, (value,))
                connection.commit()
    except psycopg2.Error as error:
        print(f"❌ Failed to insert timestamp: {error}")

#############
# Insertar 10 timestamps en zona horaria UTC-3
for i in range(20000):
    now_utc_minus3 = datetime.utcnow() - timedelta(hours=3)
    timestamp = now_utc_minus3.strftime("%Y-%m-%d %H:%M:%S")
    if i % 500 == 0:
        print(f"Conteo: {i}")
        insert_timestamp(f"Conteo: {i}")
    insert_row(timestamp)

print("✅ Palabras insertadas correctamente")

