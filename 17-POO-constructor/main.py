from coche import Coche # Importo la calse del objeto de mi otro programa

carro = Coche("Rojo", "Ford", "Taunus", 160, 110, 4)
carro1 = Coche("Verde", "Reno", "clio", 130, 120, 4)
carro2 = Coche("negro", "Fiatt", "duna", 189, 12, 4)
carro3 = Coche("Azul", "Ferrari", "Velocipede", 169, 160, 4)



print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

# Detectar tipado (tipo de dato)
carro3 = "Aleatorio"
if type(carro3) == Coche:
    print ("True")
else:
    print ("False")

# Visibilidad publica/privada
print(carro.soy_publico)
print (carro.getPrivado())