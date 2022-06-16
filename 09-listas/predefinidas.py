cantantes = ['pappo', 'bad bunny', 'pepe', 'topa']
numeros = [1, 2, 5, 10, 7, 3]

# Ordenar una lista
###print (numeros)
numeros.sort() #si no pongo nada dentro del parentesis, ordena de menor a mayor. Investigar 'key'
###print (numeros)

# Añadir elementos
###print (numeros)

cantantes.append ("charly")
#print (cantantes)

cantantes.insert (1, "don omar") # Insert siempe va a esperar dos datos .insert (posicion, "texto")
print (cantantes)

# Eliminar elementos de una lista

cantantes.pop(1) # .pop (posicion) 
cantantes.remove('topa') # .remove ('texto exacto')
print (cantantes)

numeros.reverse()
print (numeros)

# Buscar dentro de una lista

print ('pappo' in cantantes) #Devuelve un True

# Contar elementos
print (cantantes)
print (len(cantantes)) 


# Cuantas veces aparece un elemento en la lista
numeros.append ((7, 7, 7))
print (numeros.count(7))


# Conseguir indice
print (cantantes.index("pappo")) 

# Unir listas
cantantes.extend(numeros)
print (cantantes)