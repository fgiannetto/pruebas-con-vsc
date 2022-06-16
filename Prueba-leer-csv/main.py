import pandas as pd
import glob

path = r'C:/Users/NB50/Desktop/I + D/PROYECTOS/DASTEC/PROYECTO_Telemetría/Curso_Master-Python/Prueba-leer-csv' # use your path 
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)