
import psycopg2
from datetime import datetime, timedelta


# Nuevos detalles de conexión
hostname = "0crl1.h.filess.io"
database = "Test9876_shinningis"
port = "61007"
username = "Test9876_shinningis"
password = "3875d5e4415466cf9fe375095ae0f189ab81e4ca"



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

import psycopg2

# Database connection details
host1 = "0crl1.h.filess.io"
name2 = "Test9876_shinningis"
port3 = "61007"
user4 = "Test9876_shinningis"
pass5 = "3875d5e4415466cf9fe375095ae0f189ab81e4ca"
# Function t count rows in the table
def func6():
    """Counts rows in nuevo_esquema.palabras table."""
    try:
        with psycopg2.connect(
            database=name2, user=user4, password=pass5,
            host=host1, port=port3
        ) as conn7:
            with conn7.cursor() as cur8:
                sql9 = "SELECT COUNT(*) FROM nuevo_esquema.palabras;"
                cur8.execute(sql9)
                count10 = cur8.fetchone()[0]
                return count10
    except psycopg2.Error as err11:
        print(f"❌ Failed to count rows: {err11}")
        return None

# Call and print the result
res12 = func6()
if res12 is not None:
    print(f"✅ Total rows in 'nuevo_esquema.palabras': {res12}")

#######
# Insertar 10 timestamps en zona horaria UTC-3
for i in range(31):
    now_utc_minus3 = datetime.utcnow() - timedelta(hours=3)
    timestamp = now_utc_minus3.strftime("%Y-%m-%d %H:%M:%S")
    if i % 10 == 0:
        print(f"Conteo: {i}")
        insert_timestamp(f"✅ Totallabras': {res12}")
    insert_row(timestamp)

print("✅ Palabras insertadas correctamente")

