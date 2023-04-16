#TUPLES: son una coleccion de elementos, e inmutables..
#ocupan menos espacio de memoria que las listas, y pueden servir cuando no queremos que los datos no sean modificados
#1 - ESTRUCTURA
mi_tuple = (1,2,(10,2),3,4)
print(type(mi_tuple))

#2 - EXTRAER
print(mi_tuple[-2])#imprimir el elemento 2 de derecha a izq
print(mi_tuple)#no soportan adicion de items

#3 - CONSULTAR
print(mi_tuple[2][0])#el elemento 2 en la poscicion 0

#4 - CASTINGS
mi_tuple = list(mi_tuple)
print(type(mi_tuple))#cambiar el tipo lista
mi_tuple = tuple(mi_tuple)
print(type(mi_tuple))#regresar al tipo tuple

#5 - ASIGNAR VARIABLES CON TUPLE
t=(1,2,3)
x,y,z =t
print(x,y,z)#esto se puede hacer con listas y diccionarios tambien

#6 - CANTIDAD DE ELEMENTOS
t=(1,2,3,1)
print(len(t))#imprimir la cantidad de elementos

#7 - CONTAR LA CANTIDAD DE ELEMENTOS REPETIDOS EN UN TUPLE
print(t.count(1))#ponemos el 1 que es el numero repetido

#8 - CONSULTAR EL NUMERO DE INDICE
print(t.index(2))#numero de indice del elemento
