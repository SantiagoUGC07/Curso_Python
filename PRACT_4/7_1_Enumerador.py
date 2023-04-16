#ENUMERADOR acceder a los indices de una lista

#ACCEDIENDO AL INDICE SIN ENUMERADOR
lista = ['a', 'b', 'c']
indice = 0
for item in lista:
    print(indice,item)
    indice +=1

#ACCEDIENDO AL INDICE CON ENUMERADOR
lista = ['a', 'b', 'c']
for item in enumerate(lista):
    print(item)

#ACCEDIENDO AL INDICE CON ENUMERADOR
lista = ['a', 'b', 'c']
for indice,item in enumerate(lista):
    print(indice,item)

#ACCEDIENDO AL INDICE CON ENUMERADOR Y RANGE
for indice,item in enumerate(range(1,10)):
    print(indice,item)

#USANDO ENUMERADOR SIN LOOP, creando un tuple
lista = ['a', 'b', 'c']
mis_tuples = list(enumerate(lista))
print(mis_tuples)

#para acceder a los tuple, va la poscicion y numero de indice
print(mis_tuples[0][1])
