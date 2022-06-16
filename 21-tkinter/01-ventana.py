# TKINTER
# Es un modulo para crear interfaces graficas de usuario

from tkinter import*
import os.path

class Programa:

    def __init__(self):
        self.tittle = "Primer ventana de Franquito piola"
        self.icon = '.\imagenes\instagram_logo_icon_149066.ico'
        self.icon_alt = './21-tkinter\imagenes\instagram_logo_icon_149066.ico'
        self.size = "750x450"
        self.resizable = False

    def cargar (self):
        # Creo ventana raiz
        ventana = Tk()
        self.ventana = ventana
        # Titulo
        ventana.title(self.tittle)

        # Comprobar si existe un archivo
        ruta_icono = os.path.abspath(self.icon)

        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon_alt)

        # Logotipo
        ventana.iconbitmap(ruta_icono)
        ##ventana.iconbitmap(".\imagenes\instagram_logo_icon_149066.ico")
        ##"./21-tkinter\imagenes\instagram_logo_icon_149066.ico"

        # Mostrar texto en el cuadro
        texto = Label(ventana, text=ruta_icono)
        texto.pack()

        # Cambiar tamaño ventana
        ventana.geometry(self.size)
        # Bloquear tamaño de ventana
        if self.resizable:
            ventana.resizable(1, 1)
        else:
            ventana.resizable(0, 0)
        
    def addTexto(self):
        texto = Label(self.ventana, text="\n\n\n\n\n\n\n\n\n\nHola perrito malvado")
        texto.pack()
    
    def mostrar(self):
       # Arrancar y mostrar la ventana hasta que se cierre
        self.ventana.mainloop() 

# Instanciar mi programa
programa = Programa()
programa.cargar()
programa.addTexto()
programa.mostrar()