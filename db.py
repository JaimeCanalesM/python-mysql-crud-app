import sqlite3

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('database.db')  # archivo SQLite
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
    return conn
