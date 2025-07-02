from conexion import conectar
from modelos.cliente import Cliente
from modelos.producto import Producto
from modelos.pedido import Pedido, DetallePedido


def mostrar_menu():
    print("\n--- GESTIÓN DE PEDIDOS ---")
    print("1. Registrar cliente")
    print("2. Registrar producto")
    print("3. Crear pedido")
    print("4. Añadir detalle a pedido")
    print("5. Mostrar clientes")
    print("6. Mostrar productos")
    print("7. Mostrar pedidos")
    print("8. Salir")


def registrar_cliente(conexion):
    nombre = input("Nombre del cliente: ")
    email = input("Email del cliente (opcional): ")
    direccion = input("Dirección del cliente (opcional): ")
    Cliente.crear(conexion, nombre, email if email else None, direccion if direccion else None)


def registrar_producto(conexion):
    nombre = input("Nombre del producto: ")
    descripcion = input("Descripción del producto (opcional): ")
    precio = float(input("Precio del producto: "))
    Producto.crear(conexion, nombre, descripcion if descripcion else None, precio)


def crear_pedido(conexion):
    id_cliente = int(input("ID del cliente: "))
    cliente = Cliente.obtener_por_id(conexion, id_cliente)
    if cliente:
        nuevo_pedido = Pedido.crear(conexion, id_cliente)
        print(f"✅ Pedido creado con ID {nuevo_pedido.id_pedido}")


def agregar_detalle_pedido(conexion):
    id_pedido = int(input("ID del pedido: "))
    pedido = Pedido.obtener_por_id(conexion, id_pedido)
    if pedido:
        id_producto = int(input("ID del producto: "))
        cantidad = int(input("Cantidad: "))
        DetallePedido.crear(conexion, id_pedido, id_producto, cantidad)
        print("✅ Detalle añadido al pedido.")


def mostrar_clientes(conexion):
    clientes = Cliente.obtener_todos(conexion)
    print("\nClientes:")
    for cliente in clientes:
        print(cliente)


def mostrar_productos(conexion):
    productos = Producto.obtener_todos(conexion)
    print("\nProductos:")
    for producto in productos:
        print(producto)


def mostrar_pedidos(conexion):
    pedidos = Pedido.obtener_todos(conexion)
    print("\nPedidos:")
    for pedido in pedidos:
        total = pedido.calcular_total(conexion)
        print(f"{pedido} | Total: {total:.2f}€")


def insertar_datos_ficticios(conexion):
    print("\n📦 Insertando datos ficticios...")

    # Insertar 20 CLIENTES FICTICIOS
    clientes_ficticios = [
        ("Ana López", "ana@example.com", "Calle Mayor 10"),
        ("Miguel Torres", "miguel@example.com", "Avenida Libertad 45"),
        ("Sofía Martínez", "sofia@example.com", "Plaza del Sol 5"),
        ("Carlos Ruiz", "carlos@example.com", "Calle Falsa 123"),
        ("Laura Gómez", "laura@example.com", "Carrera 56"),
        ("Javier Fernández", "javier@example.com", "Calle Real 789"),
        ("Isabel Díaz", "isabel@example.com", "Paseo de la Reforma 100"),
        ("David Morales", "david@example.com", "Calle 13 No. 45-67"),
        ("Elena Castro", "elena@example.com", "Avenida Principal 200"),
        ("Mario Sánchez", "mario@example.com", "Calle Larga 300"),
        ("Natalia Ortega", "natalia@example.com", "Callejón del Sol 15"),
        ("Rafael Jiménez", "rafael@example.com", "Diagonal 456"),
        ("Patricia Rojas", "patricia@example.com", "Calle 7 # 12-34"),
        ("Fernando Vega", "fernando@example.com", "Calle 89 Bis"),
        ("Claudia Mendoza", "claudia@example.com", "Carrera 10 # 50-12"),
        ("Luis Ríos", "luis@example.com", "Avenida Sur 300"),
        ("Andrea Paredes", "andrea@example.com", "Calle Nueva 101"),
        ("Hugo León", "hugo@example.com", "Carrera 15 # 20-30"),
        ("Diana Cárdenas", "diana@example.com", "Calle 22 # 44-55"),
        ("Oscar Herrera", "oscar@example.com", "Avenida Norte 700")
    ]

    for nombre, email, direccion in clientes_ficticios:
        Cliente.crear(conexion, nombre, email, direccion)

    # Insertar productos
    Producto.crear(conexion, "Portátil Gamer", "Portátil con gráficos avanzados", 1299.99)
    Producto.crear(conexion, "Teclado Mecánico", "Teclado gaming RGB", 79.99)
    Producto.crear(conexion, "Auriculares Inalámbricos", "Con cancelación de ruido", 89.99)
    Producto.crear(conexion, "Monitor 27\" 4K", "Monitor Ultra HD", 399.99)
    Producto.crear(conexion, "Ratón Gaming", "Ratón con iluminación RGB", 49.99)

    # Crear pedidos y detalles
    pedido1 = Pedido.crear(conexion, 1)  # Cliente 1
    DetallePedido.crear(conexion, pedido1.id_pedido, 1, 2)  # 2 portátiles

    pedido2 = Pedido.crear(conexion, 2)  # Cliente 2
    DetallePedido.crear(conexion, pedido2.id_pedido, 4, 1)  # 1 monitor
    DetallePedido.crear(conexion, pedido2.id_pedido, 5, 2)  # 2 ratones

    print("✅ Datos ficticios insertados correctamente.")


def main():
    conexion = conectar()
    if not conexion:
        print("❌ No se pudo conectar a la base de datos.")
        return

    insertar_datos_ficticios(conexion)

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            registrar_cliente(conexion)

        elif opcion == "2":
            registrar_producto(conexion)

        elif opcion == "3":
            crear_pedido(conexion)

        elif opcion == "4":
            agregar_detalle_pedido(conexion)

        elif opcion == "5":
            mostrar_clientes(conexion)

        elif opcion == "6":
            mostrar_productos(conexion)

        elif opcion == "7":
            mostrar_pedidos(conexion)

        elif opcion == "8":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("❌ Opción no válida. Por favor, intenta de nuevo.")

    conexion.close()


if __name__ == "__main__":
    main()
