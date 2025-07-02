class Producto:
    def __init__(self, id_producto, nombre, descripcion=None, precio=0.0):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

    def __str__(self):
        return f"Producto[ID: {self.id_producto}, Nombre: {self.nombre}, Precio: {self.precio}€]"

    @staticmethod
    def crear(conexion, nombre, descripcion, precio):
        cursor = conexion.cursor()
        sql = "INSERT INTO productos (nombre, descripcion, precio) VALUES (%s, %s, %s)"
        valores = (nombre, descripcion, precio)
        cursor.execute(sql, valores)
        conexion.commit()
        print(f"✅ Producto '{nombre}' creado correctamente.")

    @staticmethod
    def obtener_todos(conexion):
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        resultados = cursor.fetchall()
        productos = []
        for fila in resultados:
            producto = Producto(*fila)
            productos.append(producto)
        return productos

    @staticmethod
    def obtener_por_id(conexion, id_producto):
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos WHERE id_producto = %s", (id_producto,))
        fila = cursor.fetchone()
        if fila:
            return Producto(*fila)
        else:
            print(f"❌ Producto con ID {id_producto} no encontrado.")
            return None