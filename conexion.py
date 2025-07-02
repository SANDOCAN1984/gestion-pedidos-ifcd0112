import mysql.connector

def conectar():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',             # ← Cambia si tu usuario es diferente
            password='sandocan1984',# ← Sustituye por tu contraseña real
            database='gestion_pedidos'
        )
        print("✅ Conexión exitosa a MySQL")
        return conexion
    except mysql.connector.Error as err:
        print(f"❌ Error al conectar: {err}")
        return None

# Prueba directa
if __name__ == '__main__':
    conn = conectar()
    if conn:
        conn.close()

