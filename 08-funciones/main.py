"""
Funciones:
Una funcion es un conjunto de instrucciones agrupadas bajo un nombre 
concreto que pueden reutilizarse invocando a la funcion tantas veces 
como se desee

Ejemplo

def NombreDeMiFuncion (parametros):
    # BLOQUE / CONJUNTO DE INSTRUCCIONES

NombreDeMiFuncion (mi_parametro)
 

#Ejemplo 1
print ("### EJEMPLO 1 ###")

#Defino funcion
def muestraNombre():
    print("Franco")
    print("Pepe")
    print("Juan")
    print("Pedro")
    print("Paco")
    print("\n")

#Invocar funcion
muestraNombre()
muestraNombre()


#Ejemplo 2 ---- Funcion dinamica
print ("### EJEMPLO 2 ###")

def mostrarTuNombre(nombre):
    print(f"Tu nombre es: {nombre}")
    #if sarasa
        #print (sarasa)

nombre = input("Introduzca su nombre: ")
mostrarTuNombre(nombre)

#Ejemplo 3
print ("### EJEMPLO 3 ###")

def tabla (num):
    print(f"Tabla de multiplicar del nro: {num}")

    for contador in range(11):
        operacion = num*contador
        print(f"{num} X { contador} = {operacion}")
    
    print("\n")

for num_tabla in range (1,11):
    tabla(num_tabla)


#Ejemplo 4
print ("### EJEMPLO 4 ###")

#PARAMETROS OPCIONALES

def getEmpleado (nombre, DNI = 0):
    print("Empleado")
    print(f"Nombre: {nombre}")
    print(f"DNI: {DNI}")


getEmpleado("franco")

"""

#Ejemplo 5
print ("### EJEMPLO 5 ###")

#Parametros opcionales y return de datos
def saludame (nombre):
     saludo = f"Hola, saludos {nombre}"

     return saludo

print(saludame("Franco"))


