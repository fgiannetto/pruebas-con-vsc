"""
Proyecto python MySQL:
- Abrir asistente
- Login o registro
- Registro --> Crea usuario
- Login --> Identifica usuario e inicia sesion
- Crear, mostrar, borrar notas
"""
from usuarios import acciones #import usuarios.acciones

print("""
Acciones disponibles:
    (1) Regisrarse
    (2) Login
""")

hace_el = acciones.Acciones()

accion = int (input ("Que desea hacer?  "))

if accion == 1: 
    hace_el.registro()

elif accion == 2:
    hace_el.login()

 

