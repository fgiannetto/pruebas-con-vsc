"""
Ej3:
Imprimir en pantalla los cuadrados de los primeros 60 nrs.

"""

contador = 1
num = 1

"""
# WHILE

while (contador <= 60):
     print(f"El cuadrado de {num} es {num*num}")
     num += 1 
     contador +=1
"""

# FOR

for num in range(61):
    cuadrado= num * num
    print (f"El cuadrado de {num} es {cuadrado} ")
