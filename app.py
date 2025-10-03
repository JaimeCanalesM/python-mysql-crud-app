from controllers import create_user, read_users, update_user, delete_user

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
