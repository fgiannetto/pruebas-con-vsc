"""
#FOR

-> elemento_iterable (lista, rango, etc.)

for variable in elemento_iterable
    BLOQUE DE INSTRUCCIONES

"""

contador = 0
resultado = 0

for contador in range (0,15):
    print ("Voy por el "+ str(contador))

    resultado = resultado + contador

print(f"el resultado es: {resultado}")


#break