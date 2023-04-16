#MIN Y MAX sirven para detectar los valores mas altos y bajos en una lista
menor = min(58,96,72,64,35)
mayor = max(58,96,72,64,35)
print(menor)
print(mayor)

#Tomando el mayor y menor de una lista
lista = [58,96,72,64,35]
print(f'El menor es {min(lista)} y el mayor es {max(lista)}')

#Buscar el STRING con el caracter que EMPIEZA en el abecedario, la funcion busca primero en las mayusc
nombre = "Carlos"
print(min(nombre))

#Buscar el STRING busca la cadena QUE EMPIEZA CON LA PRIMERA LETRA DEL ABECEDARIO
nombres = ['juan','pablo','alicia','carlos']
print(min(nombres))

#Buscar en los DICCIONARIOS los mas bajos
dic = {'C1':45, 'C2':11}
print(min(dic))#imprime las etiquetas
print(min(dic.values()))#imprime el valor menor