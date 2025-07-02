-- Eliminar base de datos si ya existe
DROP DATABASE IF EXISTS gestion_pedidos;

-- Crear base de datos
CREATE DATABASE gestion_pedidos;

-- Usar la base de datos
USE gestion_pedidos;

-- Tabla: clientes
-- Almacena información básica de los clientes
CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    direccion TEXT
);

-- Tabla: productos
-- Lista de productos disponibles para venta
CREATE TABLE productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL
);

-- Tabla: pedidos
-- Registra cada pedido hecho por un cliente
CREATE TABLE pedidos (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    estado ENUM('pendiente', 'completado', 'cancelado') DEFAULT 'pendiente',
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

-- Tabla: detalle_pedido
-- Detalla qué productos y cantidades se incluyen en cada pedido
CREATE TABLE detalle_pedido (
    id_detalle INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT,
    id_producto INT,
    cantidad INT NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);