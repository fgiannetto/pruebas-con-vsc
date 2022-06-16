"""
Varibles locales: Se definen dentro de la funcion y no
se puede usar fuera de ella, solo estan disponibles dentro.
A no ser que hagamos un return.

Variables globales: Son las que se declaran fuera de una 
funcion y estan disponibles dentro y fuera de ellas.
"""

#VARIABLE GLOBAL

frase = "Tu mama en tanga" #variables global

print(frase)

def holamundo():
    frase= "Hola mundo!" #variable local
    print (frase)

    año = 2021
    print (año)

    global teta
    teta= "teta global"

    return "return-> " + str(año)

print (holamundo())
print(teta)
