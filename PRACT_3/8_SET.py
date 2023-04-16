#SET son una coleccion de elementos igual que las listas,
#se pueden usar () o {} para declarar los sets
#para que los set los admita como argumentos con () se debe colocar ([])
#en los set solo se admiten elementos unicos, si se agregan elementos retidos phyton los descarta
#los elementos de los set son inmutables, y los elementos no estan ordenados en indices, ni se pueden organizar u ordenar
#no se pueden incluir listas y diccionarios dentro de los sets

#1-  EJEMPLO DE ESTRUCTURA CON ([])
mi_set = set([1,2,3,4,5,1,1,1,2,2,2])#se le ponen los corchetes por que los set solo le un argumento
print(type(mi_set))
print(mi_set)#no se imprimen ni admiten los valores repetidos
#1 - 1 - EJEMPLO DE ESTRUCTURA CON {}
otro_set = {1,2,3}
print(otro_set)

#2 - no se puede buscar por elemento ni asignar valor a un elemento
#print(mi_set[0])#no se puede
#mi_set[0] = 5#no se asigna

#3 - set admite los tuple, los admite por que son elemento inmutables ni ordenados
set2 = ([1,2,3,(2,3,1)])
print(set2[3][0])#imprimir el elemento 3 la posicicion 0

#4 - VER LA CANTIDAD DE ELEMENTOS
print(len(otro_set))

#5 - CONSULTAS DE NUMEROS O CARACTER DENTRO DEL SET
print(2 in otro_set)#esto tambien se puede hacer en listas,tuples y diccionarios.
#teniendo en cuenta que en los diccionarios se busca por la clave

#6 - INIR SETS
s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)#une los elementos y deja afuera un 3 por que se repite

#7 - AGREGAR ELEMENTOS
s1.add(2)
print(s1)#como el elemento se repite no se agrega, se queda normal

#8 - REMOVER ELEMENTOS
s1.remove(3)
print(s1)

#9 - DESCARTAR ELEMENTOS, si el elemento no existe no manda error
s1.discard(6)
print(s1)#es igual al elemento eliminar, pero no manda error

#10 - POP ELIMINA UN ELEMENTO ALEATORIO
sorteo = s1.pop()
print(sorteo)

#11 - CLEAR vacia nuestro SET
s1.clear()
print(s1)#queda totalemente vacio


