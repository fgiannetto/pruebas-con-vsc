
import mysql.connector

# Conexion
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "master_python"

)

# ¿Conexion correcta?
#print (database)

# Cursor, nos permite ejecutar las consultas
cursor = database.cursor(buffered=True)

# Crear base de datos
"""
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")

for bd in cursor:
    print (bd)
"""
# Crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
id int(10) auto_increment not null,
marca varchar(40) not null,
modelo varchar(40) not null,
precio float(10,2) not null,
CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")

cursor.execute("SHOW TABLES")

for table in cursor:
    print (table)

# Insertar datos
#cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 12000)")

# Insertar datos de forma masiva

coches= [
    ('Seat', 'Ibiza', 5000),
    ('Seat', 'Leon', 15000),
    ('fiat', 'uno', 25000),
    ('Fiat', 'duna', 55000)
]

#cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)", coches)

database.commit()

cursor.execute("SELECT * FROM vehiculos WHERE precio <= 5000 AND marca = 'Seat' ")
result = cursor.fetchall()

print("-----TODOS MIS COCHES-----")
for coche in result:
    print (coche[1], coche [3]) 

cursor.execute("DELETE FROM vehiculos WHERE marca = 'Fiat'")
database.commit()

print(cursor.rowcount, "borrados!")

cursor.execute("UPDATE vehiculos SET modelo= 'Leon' WHERE marca = 'Seat'")
database.commit()

print(cursor.rowcount, "Actualizados!")




