nombre = "Franco"

# funciones generales
print (nombre)
print (type(nombre))

# detectar tipadp

comprobar = isinstance (nombre, str)

if comprobar:#= True
    print("Eso es un string perro")
else:
    print("No es un str papaiiii")

if not isinstance (nombre, float):
    print ("La variable no es un numero con decimales")

# Limpiar espacios 
frase= "            hola               "
print(frase)
print (frase.strip())


# Eliminar variables
año = 2020

print(año)
del año
#print (año)



# Comprobar variable vacia
texto = "  ff  "

if len(texto)<=0:
    print ("variable vacia")
else:
    print ("Variable con contenido:  ", len(texto))



# Encontrar caracteres
frase="Tu madre"
print (frase.find("madre"))


#Reemplazar palabras en un string
nueva_frase = frase.replace("madre", "papa")
print (nueva_frase)


# Mayusculas y minusculas
print (nombre)
print (nombre.lower())
print (nombre.upper())
