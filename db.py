import mysql.connector

def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Admin0109",
        database="crud_python"
    )
    return connection

# Esto es para probar la conexión
if __name__ == "__main__":
    conn = create_connection()
    if conn.is_connected():
        print("Conexión exitosa a MySQL")
    conn.close()
