import os,shutil

# Crear carpeta
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print ("La carpeta ya existe")

# Eliminar carpeta
#os.rmdir('./mi_carpeta')
"""
ruta_original = "./mi_carpeta"
ruta_nueva =  "./mi_carpeta_COPIADA"
#ruta_alternativa = str(pathlib.Path().absolute()) + "/../07-ejercicios/ficherito.txt"

shutil.copytree(ruta_original, ruta_nueva)

# Eliminar carpeta
#os.rmdir('./mi_carpeta_COPIADA')
"""
print ("Contenido de mi carpeta: ")
contenido = os.listdir ("./mi_carpeta")

for carpeta in contenido:
    print("Carpeta: " + carpeta)