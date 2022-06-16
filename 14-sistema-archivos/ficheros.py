from io import open
import pathlib
import shutil

# Abrir archivo, en este caso lo genera
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo = open (ruta, "a+") # "a+"  es un permiso

# Escribir
#archivo.write(input("\n"))
archivo.write("Hola bb\n")

#Cerrar archivo
archivo.close()

# Abro el archivo para lectura
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo_lectura = open (ruta, "r") # "r" permiso de lectura

# Leer contenido
contenido = archivo_lectura.read()
print(contenido)
#for elemento in contenido

# Leer contenido y guardar en la lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

print(lista)
"""

# Copiar un archivo

ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_alternativa = str(pathlib.Path().absolute()) + "/../07-ejercicios/ficherito.txt"

shutil.copyfile(ruta_original, ruta_alternativa)


#Mover

ruta_original = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"

shutil.mmove (ruta_original, ruta_nueva)

"""

# Eliminar
"""
import os

ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
os.remove(ruta_nueva)
"""

# Comprobar si existe el archivo/ruta
import os.path

#print(os.path.abspath("../")) #Ruta absoluta
ruta_comprobar = os.path.abspath("./") + "/fichero_texto.txt"

if os.path.isfile(ruta_comprobar):
    print("El archivo existe")
else: 
    print("El archivo NO existe")