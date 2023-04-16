#LISTAS
mi_lista = ["a", "b", "c"]
resultado = (len(mi_lista[0]))#la cantidad de caracteres en la pos 0
resultado2 = (len(mi_lista))#la cantidad de caract en la cadena
resultado3 = mi_lista[0:]#imprimir todos los elementos

otra_lista = ["d", "e", "f"]
resultado4 = (mi_lista + otra_lista)#concatenar listas

#1 - impresion de resultados
print(resultado)
print(resultado2)
print(resultado3)
print(type(mi_lista))
print(resultado4)

#2 - ALTERAR LOS ELEMENTOS DE RESULTADO4
resultado4[0] = "alfa"#se cambia el caract de la pos 0 por "alfa"
print(resultado4)

#3 - AGREGAR A LA COLA LISTA
resultado4.append('g')#Se agrega al final de la lista
print(resultado4)

#4 - POP remover elementos de la LISTA
resultado4.pop()#interpreta que quieres eliminar el ultimo elemento
print(resultado4)

#5 - ELIMINAR CON POP un elemento en especifico y GUARDARLO
eliminado = resultado4.pop(0)
print(resultado4)
print(eliminado)

#6 - ORDENAR LISTA
lista_x = ["g","o","b","m","c"]
lista_x.sort()#Ordena la lista alfabetico, no es un metodo que devuela algo
print(lista_x)

#7 - INVERTIR EL ORDEN DE LA LISTA
lista_x.reverse()
print(type(lista_x))
print(lista_x)
