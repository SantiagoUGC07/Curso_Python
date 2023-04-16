#METODOS PARA COMPRENDER MEJOR LAS LISTAS

#1.1Generar una lista con cada elemento del string
palabra = 'phyton'
lista = []
for letra in palabra:
    lista.append(letra)
print(lista)
#1.2 UTILIZANDO COMPRENSION DE LISTAS
palabra = 'phyton'
lista = [letra for letra in palabra]#crear una lista letra por letra
print(lista)

#2.2Generar una lista con range CON COMPRENSION DE LISTAS
lista = [n for n in range(0,21,2)]#generar una lista numero por numero de dos en dos
print(lista)

#3.2Generar una lista con numero dividos usando range con COMPRENSION DE LISTAS
lista = [n/2 for n in range(0,21,2)]#se altera el valor antes de entrar a la lista, la liste se genera de 0 al 21 de dos en dos
print(lista)

#4.2 Incorporar un if en la creacion de la lista
lista = [n for n in range(0,21,2) if n * 2 > 10] # crear una lista del 0 al 21 de dos en dos mientras el numero *2 sea mayor a 10
print(lista)

#5.2 Incorporar un else en la creacion de la lista
#se agrega un no para los numeros que no cumplen la condicion
lista = [n if n * 2 > 10 else 'no' for n in range(0,21,2)]
print(lista)

#6.2 ELABORAR una lista convirtiendo los pies a metros
pies = [10,20,30,40,50]
metro = [p * 3.281 for p in pies]
print(metro)

