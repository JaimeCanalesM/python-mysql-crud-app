# Python + MySQL CRUD App

Este proyecto es una aplicación de consola escrita en Python que permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre una base de datos MySQL.

---

## Tecnologías utilizadas

- Python 3.13
- MySQL
- mysql-connector-python
- Git y GitHub

---

## Funcionalidades

- **Crear** nuevos usuarios (nombre y correo).
- **Leer** usuarios registrados.
- **Actualizar** información de un usuario existente.
- **Eliminar** usuarios por ID.

---

## Cómo ejecutar el proyecto

### 1. Clona el repositorio:

```bash
git clone https://github.com/JaimeCanalesM/python-mysql-crud-app.git
cd python-mysql-crud-app

2. Crea el entorno virtual (opcional pero recomendado)

python -m venv venv
.\venv\Scripts\activate

3. Instala las dependencias:

pip install -r requirements.txt

4. Configura la base de datos

CREATE DATABASE crud_python;
USE crud_python;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

5. Ejecuta la app

python app.py



---

## Roadmap del Proyecto

Este proyecto comenzó como una aplicación CRUD de consola en Python y MySQL. A medida que avanzo en mi formación como desarrollador, iré incorporando nuevas funcionalidades y tecnologías.

### Etapas planificadas:

✅ CRUD funcional con conexión a MySQL  
✅ Validación básica de entradas  
✅ Manejo de errores con `try/except`  
✅ Separación del código en módulos  

Próximas mejoras:

- [ ] Crear estructura web usando Flask
- [ ] Formularios HTML para CRUD de usuarios
- [ ] Interfaz responsiva con Bootstrap
- [ ] Sistema de login para proteger las rutas
- [ ] Hash de contraseñas con bcrypt
- [ ] Creación de API REST con Flask
- [ ] Agregar tests automatizados con `pytest`
- [ ] Despliegue en Render o Railway


