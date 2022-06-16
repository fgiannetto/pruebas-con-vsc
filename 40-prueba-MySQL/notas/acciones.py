import notas.nota as modelo
 

class acciones:

    def crear(self, usuario):
        print(f"Ok {usuario[1]}! Creemos tu nota... ")

        titulo = input("Introduce el titulo de tu nota: ")
        descripcion = input ("Tipea el contenido de tu nota: ")

        nota = modelo.nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nHas guardado la nota: {nota.titulo}")

        else:
            print(f"\nPerdon {usuario}, no se pudo guardar la nota")
    
    def mostrar (self, usuario):
        print(f"Vale {usuario[1]}! Aqui teneis vuestras notas: ")
        nota = modelo.nota(usuario[0], "", "") 
        notas=nota.listar()

        for nota in notas:
            print("\n************")
            print(nota[2])
            print(nota[3])
            print("************\n")

    def borrar (self, usuario):
        print(f"A borrar mi amor, vamos a borrar mi amor")

        titulo = input("Introduce el titulo de la nota a borrar: ")

        nota = modelo.nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"Se borro la nota {nota.titulo}")
        else:
            print("No se pudo borrar la nota")