class Coche:

    # Atributos o propiedades (variables)
    # Caracteristicas del coche
    color = "Rojo"
    marca = "Ducati"
    modelo = "Panigale"
    velocidad = 300
    cv = 192
    plazas = 1

    def __init__(self, color, marca, modelo, velocidad, cv, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.cv = cv
        self.plazas = plazas

    soy_publico = "Hola, soy un atributo publico"
    __soy_privado = "Hola, soy macrista gato privado"

    # Metodos --> Acciones/caracteristicas que hace el objeto (coche) (funciones)

    def getPrivado(self):
        return self.__soy_privado

    def acelerar(self):
        self.velocidad += 1
    
    def frenar (self):
        self.velocidad -= 1

    def getVelocidad (self):
        return self.velocidad
    
    def setColor (self, color):
        self.color = color
    def getColor (self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo
    def getModelo (self):
        return self.modelo
    
    def setMarca (self, marca):
        self.marca = marca
    def getMarca (self):
        return self.marca

    def getInfo (self):
        info = ("------ Info del coche -------")
        info += "\n Color: " + self.getColor()
        info += "\n Marca: " + self.getMarca()
        info += "\n Modelo: " + self.getModelo()
        info += "\n Velocidad: " + str(self.getVelocidad())
        return info

# Fin definicion clase
