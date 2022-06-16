import clases

persona = clases.Persona()
persona.setNombre("Franco")
persona.setApellido("Giann")
persona.setAltura ("185cm")
persona.setEdad("23 años")

print(f"La persona es: {persona.getNombre()} {persona.getApellido()} ")
print (persona.hablar())

print("-------------------")

informatico = clases.Informatico()
informatico.setNombre("Pepe")
informatico.setApellido ("Santoro")

print(f"El informatico es: {informatico.getNombre()} {informatico.getApellido()}")
print(informatico.getLenguajes())
print(informatico.caminar())

print("-------------------")





