"""
LISTAS (arrays)
Son colecciones o conjuntos de datos/valores, bajo un unico nombre.
Para acceder a esos valores podemos usar un indice numerico. (diccionario?¿)
"""
"""
pelicula = "Batman"

# Definir lista
peliculas = ["Batman", "spiderman", "tu madre"]
cantantes = list (('2pac', 'drake', 'pablito ruiz')) #necesario el doble parentesis. La lista espera un solo elemento, por lo que el contenido hay que transformarlo en una tupla (no se modifica)
años = list (range(2020, 2050))
variada = ['hola', "Franco", True, 85]


print (pelicula)
print (peliculas)
print (cantantes)
print (años)
print (variada)


# Indices

print (peliculas[1])
print (peliculas[-2])
print (cantantes [1:3])
print (peliculas [1:]) #imprime a partir del elementro 1

#Añadir elementos a una lista
print(cantantes)
cantantes.append("pepa pig") #con append agrega elementos al final de la lista
print(cantantes)

# Recorrer lista con un for
print ("\n****[lista de pelis]*****")

nueva_peli=""
while nueva_peli!= "parar":
    nueva_peli = input("introduzca pelicula")
    if nueva_peli != "parar":
        peliculas.append(nueva_peli)

for pelicula in peliculas:
    #print (pelicula)
    print (f"{peliculas.index(pelicula)+1}. {pelicula}")
"""

# Lista multidimensional (listas dentro de listas)
print ("\n* * * * [lista de contactos] * * * *")
contactos = [
    [
        'pepe',
        'pepa hot'
    ],
    [
        'juan',
        'juanhot'
    ],
    [
        'pedro',
        'hotttttt'
    ]
]

# para mostrar 'juanhot'
# print(contactos [1][1])

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento)==0:
            #print ("Nombre: " + elemento)
            print (f"Nombre: {elemento}")
        else:
            print ("Correo: " + elemento)
    print ("\n")   