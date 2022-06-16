# Capturar excepciones y manejar errores en codigo
# susceptible a fallos / errores.
"""
try:
    nombre = input("¿Cual es tu nombre?: ")

    if len(nombre) > 1:
        nombre_usuario = "El nombre es " + nombre

    print (nombre_usuario)

except:
    print ("Nombre invalido")

else:
    print("Todo joya")

finally: #Siempre se va a ejecutar
    print("Fin de la iteracion") 


# Multiples excepciones
try:
    numero = int(input("Numero al cuadrado: "))
    print ("El cuadrado es: " + str (numero*numero))
except TypeError:
    print("Debes poner un numero, corki")
#except ValueError:
 #   print("Pone un numero capo")

except Exception as e:
    print("Hubo error: ",type(e).__name__) #name muestra SOLO el tipo de dato, sin el "<class>"
"""

# Excepciones personalizadas o lanzar excepcion
try:
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("La edad no es real, careta")
    elif len (nombre) <= 1:
        raise ValueError ("Nombre erroneo")
    else:
        print(f"Bienvenido {nombre}, de {edad} años")

except ValueError:
    print("Escribi bien")

except Exception as e:
    print ("Existe un error: ", e) 




