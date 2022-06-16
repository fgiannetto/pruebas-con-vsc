# Sistema de base de datos incluido en Python
# Importo el modulo
import sqlite3

# Conexion a SQLite3
conexion = sqlite3.connect('pruebas.db')

# Crear cursor
cursor = conexion.cursor()

# Crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos(" + 
"id INTEGER PRIMARY KEY AUTOINCR EMENT,"+
"titulo varchar (255),"+
"descripcion text,"+
"precio int(255)"+
")" )

# Guardar cambios
conexion.commit()

# Insertar datos en la tabla
cursor.execute("INSERT INTO productos VALUES (null, 'producto 1', 'descripcion del producto', 750)")
conexion.commit()

# Borrar registros
cursor.execute("DELETE FROM productos")


# Listar datos
cursor.execute("SELECT * FROM productos;")
productos = cursor.fetchall()

for producto in productos:
    print(producto) 

#cursor.execute("SELECT titulo FROM productos;")
#producto= cursor.fetchone()
#print(producto)


# Cerrar conexion
conexion.close()
