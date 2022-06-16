"""
Ej2:
Crear scrpit para mostrar por pantalla todos los numeros pares del 1 al 100
"""
contador = 1
numero = 1
par = 2 


for contador in range (1, 101):
    #resto = numero%par
    #contador += 1
#if resto == 0:
    if numero%2 == 0:
        print (numero)
        numero += 1
    else:
        numero += 1
        contador  += 1    

