#1.-EJERCICIO encontrar los indices de cada nombre
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el indice {indice}')

#2.-EJERCICIO crear un tuple con la palabra python, usando enumerate y loop
palabra="python"
lista_indices = list(enumerate(palabra))
print(lista_indices)

#3.-EJERCICIO imprimir unicamente los elementos de la lista que empiecen con la letra M
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,item in list(enumerate(lista_nombres)):
    nombre = list(enumerate(item.lower()))#se separa por letras y se convierte en minuscula
    if(nombre[0][1] == 'm'):#se compara la primera leta de cada elemento de la lista
        print(indice,item)#para imprimir el indice y el nombre
        print(indice)#para imprimir el solo el indice