from flask import Flask, render_template, request, redirect, url_for, flash
from db import create_connection

app = Flask(__name__)
app.secret_key = 'secret-key'

# Ruta principal
@app.route('/')
def home():
    return '<h2> App CRUD Flask + MySQL</h2><a href="/usuarios">Ver usuarios</a>'

# Ruta para mostrar la lista de usuarios
@app.route('/usuarios')
def listar_usuarios():
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        usuarios = cursor.fetchall()
        conn.close()
        return render_template("usuarios.html", usuarios=usuarios)
    except Exception as e:
        return f"Error al obtener usuarios: {e}"

# Ruta para crear un nuevo usuario
@app.route('/crear', methods=['GET', 'POST'])
def crear_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']

        if not nombre.strip() or not email.strip():
            return "Nombre y correo no pueden estar vacíos."

        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (nombre, email))
            conn.commit()
            conn.close()
            flash('Usuario creado correctamente.')
            return redirect(url_for('listar_usuarios'))
        except Exception as e:
            return f"Error al crear usuario: {e}"

    return render_template("crear.html")

@app.route('/eliminar/<int:id>')
def eliminar_usuario(id):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        flash('Usuario eliminado correctamente.')
        return redirect(url_for('listar_usuarios'))
    except Exception as e:
        return f"Error al eliminar usuario: {e}"


@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_usuario(id):
    try:
        conn = create_connection()
        cursor = conn.cursor()

        if request.method == 'POST':
            nombre = request.form['nombre']
            email = request.form['email']

            if not nombre.strip() or not email.strip():
                return "Nombre y correo no pueden estar vacíos."

            cursor.execute("UPDATE users SET name=?, email=? WHERE id=?", (nombre, email, id))
            conn.commit()
            conn.close()
            flash('Usuario actualizado correctamente.')
            return redirect(url_for('listar_usuarios'))

        # GET → mostrar datos
        cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
        usuario = cursor.fetchone()
        conn.close()

        if usuario:
            return render_template("editar.html", usuario=usuario)
        else:
            return "Usuario no encontrado."

    except Exception as e:
        return f"Error al editar usuario: {e}"

# Ejecutar la app
if __name__ == '__main__':
    app.run(debug=True)
