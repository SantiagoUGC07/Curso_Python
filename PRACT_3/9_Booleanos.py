#BOOLEANOS solo pueden tener dos valores, TRUE O FALSE
#se pueden declarar de manera indirecta, con las operaciones logicas
# >,<,>=,<=,==,!=.. el resultado que proporcionan es boleano
#tambien se encuentrar los booleanos en las listas con ( 5 in lista)

#1 - DECLARACION DE BOOLEANOS
var1 = True
var2 = False
print(type(var1))
print(var1)

#2 - CREAR DE MANERA INDIRECTA
numero= 5 > 2+3
print(type(numero))
print(numero)

#3 - COMPARACIONES
numero = 5 == 2+3
print(numero)
print(type(numero))

#4 - CREAR FUNCION BOOL PARA ANALIZAR
numero = bool(5<6)
print(type(numero))
print(numero)
numero = bool()#si se queda vacia manda un valor falso
print(type(numero))

#5 - EJEMPLO, crear lista y preguntar si el numero esta dentro de la misma
lista = [1,2,3,4]
control = 5 in lista
print(lista)
print(type(control))
print(control)
