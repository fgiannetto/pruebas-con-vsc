"""
SET es un tipo de dato para tener una coleccion de valores
pero no tiene ni indice ni orden 
"""

personas = {
    "Victor",
    "Franco",
    "Carlos"
}

personas.add("pepito")  
personas.remove("Franco")

print(type(personas))
print(personas)
