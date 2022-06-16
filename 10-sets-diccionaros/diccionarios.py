"""
DICCIONARIO:
Es un tipo de dato que almacena un conjunto de datos
en formato clave > valor.
Similar a un array asociativo o un objeto json.
"""

persona = {
    # Clave     #Valor
    "nombre": "Franco",
    "apellido": "Giann",
    "web": "tuma.com.ar"
}
#print ( persona)
#print (type(persona))

#print (persona ["apellido"]) #Saca el valor de esa clave

# Lista con diccionarios

contactos = [
    {
        'nombre':'Franco',
        'correo':'gmail'
    },
    {
        'nombre':'Carlos',
        'correo': 'yahoo'
    },
    {
        'nombre': 'Pepe',
        'correo': 'hotmail'
    }
]
contactos [0]['correo'] = "MSN"
print(contactos [0]['correo'])
print("\n")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Correo del contacto: {contacto['correo']}")
    print("\n")
