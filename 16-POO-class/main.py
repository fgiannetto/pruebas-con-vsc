# Programacion orientada a objetos (POO)

#Definir una clase --> Molde para crear mas objetos de ese tipo
# (Coche) con caracteristicas similres

class Coche:

    # Atributos o propiedades (variables)
    # Caracteristicas del coche
    color = "Rojo"
    marca = "Ducati"
    modelo = "Panigale"
    velocidad = 300
    cv = 192
    plazas = 1

    # Metodos --> Acciones/caracteristicas que hace el objeto (coche) (funciones)

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
# Fin definicion clase

# Crear objetos / Instanciar la clase
print("COCHE 1: ")
coche = Coche()

coche.setColor("amarillo")
coche.setModelo("R6")  

print (coche.marca, coche.getModelo(), coche.color)
print("Velocidad actual: ", coche.velocidad)
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
print("Nueva velocidad actual: ", coche.getVelocidad())

coche.frenar()
print("Nueva velocidad: ", coche.velocidad)

print("-------------------------")
print("COCHE 2: ")

# Crear mas objetos
coche2 = Coche()

# Modifico un segundo objeto de la misma clase e imprimo en pantalla 
coche2.setColor("Azul electrico")
coche2.setModelo("R1")

print(coche2.marca, coche2.getModelo(), coche2.getColor())

  

