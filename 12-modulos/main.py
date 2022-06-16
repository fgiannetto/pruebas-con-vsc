"""
MODULOS:
Son funcionalidades ya hechas para reutilizar. (Librerias, por ejemplo)
-----
Indice de todas las incluidas: https://docs.python.org/3/py-modindex.html
-----
Podemos conseguir modulos extra en internet y ademas podemos crearlos.
"""

# Importar modulo propio de mimodulo.py
import mimodulo
print(mimodulo.HolaMundo("Franco"))

print("- - - - - - - - - - -")

from mimodulo import HolaMundo
print(HolaMundo("Franco"))
#from mimodulo import*

print("- - - - - - - - - - - - - - - - -")

# Modulo fechas
import datetime
print(datetime.date.today())

fecha_completa = datetime.datetime.now()
print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.second)

fecha_personalizada = fecha_completa.strftime("%d / %B / %b ")
print(fecha_personalizada)

print(datetime.datetime.now().timestamp())

print("- - - - - - - - - - - - - - - - -")

# Modulo matematica
import math

print ("Raiz cuadrada de 10: ", math.sqrt(10))
print ("Numero pi:  ", math.pi)
print ("Redondear pa arriba: ", math.ceil(5.49))
print ("Redondear pa abajo: ", math.floor(5.49))


# Modulo random
import random

print ("Nro. aleatorio entre 1 y 129: ", random.randint(1, 129))


