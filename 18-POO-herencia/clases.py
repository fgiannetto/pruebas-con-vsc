# HERENCIA: Posibilidad de compartir atributos y metdodos entre clases, 
# y que diferentes clases hereden de otras

class Persona:
    """
    nombre
    apellidos
    altura
    edad
    etc.
    """
    #getters
    def getNombre (self):
        return self.nombre
    
    def getApellido (self):
        return self.apellido
    
    def getAltura(self):
        return self.altura

    def getEdad (self):
        return self.edad

    #setters
    def setNombre (self, nombre):
        self.nombre = nombre
    
    def setApellido (self, apellido):
        self.apellido = apellido 
    
    def setAltura (self, altura):
        self.altura = altura
    
    def setEdad (self, edad):
        self.edad = edad

    def hablar(self):
        return "estoy hablando"

    def caminar (self):
        return "Estoy caminando"    
    
    def dormir (self):
        return "Estoy durmiendo"
    
class Informatico (Persona):
    """
    lenguajes
    experiencia
    """

    def __init__(self):
        self.lenguajes = "HTML, PYTHON, PHP"
        self.experiencia = 5
    
    def getLenguajes (self):
        return self.lenguajes
    
    def aprender(self, lenguajes):
        self.lenguajes=lenguajes
        return self.lenguajes
    
    def programar(self):
        return "Estoy programando"

    def repararPC (self):
        return "He reparado tu PC"

class TecnicoRedes (Informatico):
    
    def __init__ (self):
        self.auditarRedes = 'experto'
        