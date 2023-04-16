#Modulo collections
'''
para poder utilizar el modulo collections se debe importar
    from collections import [elemento]
el modulo collections, nos ayuda a completar y manipulas las estructuras de datos como:
los diccionarios, listas y tuples
'''
from collections import Counter
from collections import defaultdict
from collections import namedtuple
#1.-EJEMPLO cantidad de NUM Repetidos en una LISTA con COLLECTION
print("\n#1.-EJEMPLO cantidad de NUM Repetidos en una LISTA con COLLECTION ")
numeros = [8,6,9,4,5,2,3,4,4,5,3,5,6,7,8,8,7,5,9,9,8]
print(Counter(numeros))#se imprime el numero y la cantidad de veces que se repite

#2.-EJEMPLO LETRAS REPETIDAS string
print("\n2.-EJEMPLO LETRAS REPETIDAS string")
print(Counter("Missisippi"))#se imprime la letra y la cantidad de veces que se repite
#3.-EJEMPLOFRASE contar las palabras
print("\n3.-EJEMPLOFRASE contar las palabras")
frase = 'al pan pan al vino vino'
print(Counter(frase.split()))#haciendo uso de splir para separar por espacio en blanco las palabras,
                            #se hace el conteo de las palabras

#4.-EJEMPLO EL MAS COMUN, se imprime los elementos que se repiten mas veces y su cantidad de veces
print("\n#4.-EJEMPLO EL MAS COMUN")
serie = Counter([1,1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,5,5,5,5,5])
print(serie.most_common())#se imprimen todos loe elementos con su cantidad de aparicion
print(serie.most_common(2))#se imprimen los dos mas comunes

#5.-IMPRIMIR UNA LISTA APARTIR DE LOS ELEMENTOS COUNTER
print("\n#5.-EJEMPLO IMPRIMIR UNA LISTA APARTIR DE LOS ELEMENTOS COUNTER")
print(list(serie))#se imprimen los elementos de serie sin repetirse

#6.-EJEMPLO LAMBDA sirve para asignarle un valor a una variable de diccionario que no se encuentra
#se requiere importar libreria import defaultdict
print("\n6.-EJEMPLO LAMBDA asignar valor a una variable de dic que no se encuetra")
mi_dic ={'uno':'verde','dos':'azul','tres':'rojo' }
print("buscando en el dic una varible que si se encuentra")
print(mi_dic['dos'])
#6.-print(mi_dic{'cuatro'})#esto manda ERROR dado a que no existe
print("usando lambda para una variable que no se encuetra")
mi_dic = defaultdict(lambda:'nada')
print(mi_dic['dod'])#se imprime el valor de lambda
print(mi_dic)#igual se imprime nada, dado a que no estamos imprimiendo algun valor del dic

#7.-EJEMPLO nametuple
#se requiere importar namedtuple
print("\n7.-EJEMPLO namedtuple ASIGNAR tuple a un Objeto")
print("se imprime tuple")
mi_tupla = (500,18,65)
print(mi_tupla[1])
print("Ejemplo con namedtuple, crear objetos con tupple")
Persona= namedtuple('Persona',['nombre','altura','peso'])#se crea objeto persona y se le asignan valores de tuple
ariel = Persona('Ariel',1.76,79)
print("se imprime la info del objeto del tuple")
print(ariel.altura)#podemos acceder a los elementos del objeto persona, de la sig manera
print("se imprime de la manera habitual como se accede a tuple")
print(ariel[2])#igual se puede acceder de la manera normal. como TUPLE


