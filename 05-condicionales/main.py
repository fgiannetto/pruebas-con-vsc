"""
asdasd
"""

"""
#Ejmplo condicion 1
print("--------EJEMPLO 1------")
#color = "rojo"
color = input("Que color?: ")

if color == "rojo":
    print ("el color es rojo")
else:
    print ("el color no es rojo")


#Ejmplo 2
print("--------EJEMPLO 2------")

#año = 2020
año = int (input ("Enque año estamos?"))

if año >=2021:
    print ("estamos del 2021 en adelante")
else:
    print("pete")   
"""

#Ejmplo 3
print("--------EJEMPLO 3------")

nombre = input ("Nombre?")
continente = input ("Continente?")
if continente == "Europa":
    ciudad = input ("Ciudad?")

edad = int (input ("Edad?"))
mayoria_edad = 18

if edad >= mayoria_edad:
    print (f"{nombre} es mayor")

    if continente != "Europa":
        print (f"{nombre} no es europeo")
    else:
        print (f"{nombre} es europeo y proviene de {ciudad}")
else:
    print (f"{nombre} no es mayor de edad")