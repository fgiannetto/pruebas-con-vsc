"""
#Ejemplo 6
print ("### EJEMPLO 6 ###")

def calculadora (num1, num2, basicas = False):
    suma = num1 + num2
    resta= num1 - num2
    multi= num2*num1
    div= num1/num2

    cadena = ""

    cadena += "Suma: " + str(suma)
    cadena += "\n"
    cadena += "Resta: " + str(resta)
    cadena += "\n"
    cadena += "Multiplicacion: "  + str(multi)
    cadena += "\n"
    cadena += "Division: "  + str(div)
    cadena += "\n"

    return cadena 

print(calculadora(5, 6))

def getnombre (nombre):
    texto =f"El nombre es: {nombre}"
    return texto

def getapellido (apellido):
    texto =f"El apellido es: {apellido}"
    return texto

def nombreapellido (nombre, apellido):
    texto = getnombre(nombre) + "\n" + getapellido(apellido)
    return texto

nombre = input("Nombre? ")
apellido = input ("Apellido? ")

print(nombreapellido(nombre, apellido)) 
"""

#Ejemplo 8: Funciones lambda

decir_año = lambda año: f"El año es {año}"

print(decir_año(2020))

