class DetallePedido:
    def __init__(self, id_detalle, id_pedido, id_producto, cantidad):
        self.id_detalle = id_detalle
        self.id_pedido = id_pedido
        self.id_producto = id_producto
        self.cantidad = cantidad

    def obtener_subtotal(self, conexion):
        cursor = conexion.cursor()
        cursor.execute("SELECT precio FROM productos WHERE id_producto = %s", (self.id_producto,))
        precio = cursor.fetchone()[0]
        return self.cantidad * precio

    @staticmethod
    def crear(conexion, id_pedido, id_producto, cantidad):
        cursor = conexion.cursor()
        sql = "INSERT INTO detalle_pedido (id_pedido, id_producto, cantidad) VALUES (%s, %s, %s)"
        valores = (id_pedido, id_producto, cantidad)
        cursor.execute(sql, valores)
        conexion.commit()
        print("✅ Detalle de pedido añadido.")


class Pedido:
    def __init__(self, id_pedido, id_cliente, fecha, estado="pendiente"):
        self.id_pedido = id_pedido
        self.id_cliente = id_cliente
        self.fecha = fecha
        self.estado = estado
        self.detalles = []

    def agregar_detalle(self, conexion, id_producto, cantidad):
        DetallePedido.crear(conexion, self.id_pedido, id_producto, cantidad)

    def obtener_detalles(self, conexion):
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM detalle_pedido WHERE id_pedido = %s", (self.id_pedido,))
        filas = cursor.fetchall()
        self.detalles = [DetallePedido(*fila) for fila in filas]

    def calcular_total(self, conexion):
        total = 0
        for detalle in self.detalles:
            total += detalle.obtener_subtotal(conexion)
        return total

    @staticmethod
    def crear(conexion, id_cliente):
        cursor = conexion.cursor()
        sql = "INSERT INTO pedidos (id_cliente) VALUES (%s)"
        cursor.execute(sql, (id_cliente,))
        conexion.commit()
        id_pedido = cursor.lastrowid
        print(f"✅ Pedido creado con ID: {id_pedido}")
        return Pedido(id_pedido, id_cliente, "NOW()")

    @staticmethod
    def obtener_todos(conexion):
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM pedidos")
        resultados = cursor.fetchall()
        pedidos = []
        for fila in resultados:
            pedido = Pedido(*fila)
            pedido.obtener_detalles(conexion)
            pedidos.append(pedido)
        return pedidos

    @staticmethod
    def obtener_por_id(conexion, id_pedido):
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM pedidos WHERE id_pedido = %s", (id_pedido,))
        fila = cursor.fetchone()
        if fila:
            pedido = Pedido(*fila)
            pedido.obtener_detalles(conexion)
            return pedido
        else:
            print(f"❌ Pedido con ID {id_pedido} no encontrado.")
            return None