-- Crear base de datos
CREATE DATABASE IF NOT EXISTS crud_python;
USE crud_python;

-- Crear tabla de usuarios
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);