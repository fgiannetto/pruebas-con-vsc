import usuarios.usuario as modelo
import notas.acciones


class Acciones:
    
    def registro (self):
        print ("\n- - - - - - - - -")
        print ("Ok! Registrese...")
        print ("- - - - - - - - -\n")
        nombre = input ("Cual es tu nombre?   ")
        apellidos = input ("Cual es tu apellido?  ")
        email = input("Cual es tu mail?  ")
        password = input ("Genere una contraseña: ")

        usuario= modelo.Usuario(nombre, apellidos,email,password)
        registro = usuario.registrar()

        if registro[0] >=1:
            print (f"Hola {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("No te has registrado correctamente")
     
    def login(self):
        print ("\n- - - - - - - - -")
        print("Inicie sesión...")
        print ("- - - - - - - - -\n")

        try:
            email = input("Cual es tu mail?  ")
            password = input ("Genere una contraseña: ")

            usuario = modelo.Usuario('','', email, password)
            login = usuario.identificar()

            if email== login[3]:
                print(f"\nBienvenido: {login[1]}, te has registrado el día {login[5]} ")
                self.proximo(login)

        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Login incorrecto !¡")

    def proximo(self, usuario):
        print("""
        Acciones disponibles:
        - Crear nota
        - Mostrar notas
        - Eliminar nota
        - Salir
        """)

        accion = input("Que queres hacer?: ")
        hace = notas.acciones.acciones()

        if accion == "crear":
            hace.crear(usuario)
            #print ("Vamos a crear") 
            self.proximo(usuario)

        elif accion == "mostrar":
            hace.mostrar(usuario)
            #print ("Vamos a mostrar")
            self.proximo(usuario)

        elif accion == "eliminar":
            hace.borrar(usuario)
            # print ("Vamos a eliminar")
            self.proximo(usuario)

        elif accion == "salir":
            print (f"Hasta luego {usuario[1]}!")          
            exit()

        return None



