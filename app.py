from db import create_connection

def create_user(name, email):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    conn.close()
    print("Usuario agregado correctamente.")

def read_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    print("\n Lista de usuarios:")
    for row in rows:
        print(f"ID: {row[0]} | Nombre: {row[1]} | Email: {row[2]}")

def update_user(user_id, name, email):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name=%s, email=%s WHERE id=%s", (name, email, user_id))
    conn.commit()
    conn.close()
    print("Usuario actualizado.")

def delete_user(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
    conn.commit()
    conn.close()
    print("Usuario eliminado.")

def menu():
    while True:
        print("\n--- Menú CRUD ---")
        print("1. Crear usuario")
        print("2. Ver usuarios")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")

        choice = input("Selecciona una opción: ")

        if choice == "1":
            name = input("Nombre: ")
            email = input("Email: ")
            create_user(name, email)
        elif choice == "2":
            read_users()
        elif choice == "3":
            user_id = input("ID del usuario a actualizar: ")
            name = input("Nuevo nombre: ")
            email = input("Nuevo email: ")
            update_user(user_id, name, email)
        elif choice == "4":
            user_id = input("ID del usuario a eliminar: ")
            delete_user(user_id)
        elif choice == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
