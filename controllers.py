from db import create_connection

def create_user(name, email):
    if not name.strip() or not email.strip():
        print("Nombre y correo no pueden estar vacíos.")
        return

    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()
        print("Usuario agregado correctamente.")
    except Exception as e:
        print("Error al agregar el usuario:", e)
    finally:
        conn.close()



def read_users():
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        print("\n Lista de usuarios:")
        for row in rows:
            print(f"ID: {row[0]} | Nombre: {row[1]} | Email: {row[2]}")
    except Exception as e:
        print("Error al leer los usuarios:", e)
    finally:
        conn.close()


def update_user(user_id, name, email):
    if not name.strip() or not email.strip():
        print("Nombre y correo no pueden estar vacíos.")
        return

    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET name=%s, email=%s WHERE id=%s", (name, email, user_id))
        conn.commit()
        print("Usuario actualizado.")
    except Exception as e:
        print("Error al actualizar el usuario:", e)
    finally:
        conn.close()



def delete_user(user_id):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
        conn.commit()
        print("Usuario eliminado.")
    except Exception as e:
        print("Error al eliminar el usuario:", e)
    finally:
        conn.close()