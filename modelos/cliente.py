class Cliente:
    def __init__(self, id_cliente, nombre, email=None, direccion=None):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.email = email
        self.direccion = direccion

    def __str__(self):
        return f"Cliente[ID: {self.id_cliente}, Nombre: {self.nombre}, Email: {self.email}, Dirección: {self.direccion}]"

    @staticmethod
    def crear(conexion, nombre, email=None, direccion=None):
        cursor = conexion.cursor()
        sql = "INSERT INTO clientes (nombre, email, direccion) VALUES (%s, %s, %s)"
        valores = (nombre, email, direccion)
        cursor.execute(sql, valores)
        conexion.commit()
        print(f"✅ Cliente '{nombre}' creado correctamente.")

    @staticmethod
    def obtener_todos(conexion):
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM clientes")
        resultados = cursor.fetchall()
        clientes = []
        for fila in resultados:
            cliente = Cliente(*fila)
            clientes.append(cliente)
        return clientes

    @staticmethod
    def obtener_por_id(conexion, id_cliente):
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM clientes WHERE id_cliente = %s", (id_cliente,))
        fila = cursor.fetchone()
        if fila:
            return Cliente(*fila)
        else:
            print(f"❌ Cliente con ID {id_cliente} no encontrado.")
            return None