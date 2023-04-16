#1.-EJERCICIO Crea una funcion lanzar_dados que arroje dos dados al azar y devuelva sus resultados:
# la funcion debe retornar dos valores, resultado, que se encuentre 1 y 6
# dicha funcion no debe requerir argumentos para funcionar, si no que debe generar internamente
#  los valores aleatorios.
#proporciona el resultado de estos dos dados a una funcion que se llama evaluar_jugada (es decir, esta segunda funcion
# debe recibir dos argumentos) y que retorne -sin imprimirlo- un mensaje segun la suma de estos valores:
#si la suma es menor o igual a 6
# "la suma de tus dados es{suma_dados}. lamentable"
from random import shuffle
from random import randint
Naleatorios=[]
#1.-LANZAR LOS DADOS
print("1.-EJERCICIO")
def lanzar_dados():
    dados=list(range(1,7))
    n = 0
    while(n<2):
        #Revuelve la lista
        shuffle(dados)
        print(dados)
        #aqui no se ocupa la lista pero se Elije un numero aleatorio
        Naleatorios.append(randint(1,7))
        n+=1
    return Naleatorios
#1.-EVALUAR LA JUGADA
def evaluar_jugada(Naleatorios):
    suma_dados=0
    for n in Naleatorios:
        suma_dados=suma_dados+n
    print(suma_dados)
    if(suma_dados<=6):
        print(f"La suma de tus dados es {suma_dados}. Lamentable")
    elif(suma_dados>6 and suma_dados<10):
        print(f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
    elif(suma_dados>=10):
        print(f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")
    else:
        pass
#1.-PROGRAMA
Naleatorios=lanzar_dados()
print(Naleatorios)
evaluar_jugada(Naleatorios)
#
#1.-EJERCICIO OTRA SOLUCION
import random
print("\n1.-EJERCICIO otra sol.")
def lanzar_dados2():
    return random.randint(1, 6), random.randint(1, 6)
def evaluar_jugada2(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
dado1,dado2=lanzar_dados2()#se devolvieron dos valores y se guardaron en dos variables
print(evaluar_jugada2(dado1,dado2))#se envian variables y se recibe respuesta
#
#2.-EJERCICIO Crea una funcion llamada reducir_lista() que tome una lista como argumento (crea tambien la variable
# lista_numeros), y devuelva la misma lista, pero eliminando duplicados (dejando uno solo de los numeros si hay repetidos)
# y eliminando el valor mas alto. el orden de los elementos puede modificarse.
#por ejemplo, si se le proporciona la lista[1,2,15,7,2] debe devolver [1,2,7]
#crea una funcion llamada promedio() que pueda recibir como argumento la lista devuelta por la anterior funcion, y que calcule
#el promedio de los valores de la misma. debe devolver el resultado, sin impriirlo
#2.-CREACION DE LISTA
def reducir_lista():
    lista_numeros= [1,2,15,7,2]
    print(f"\n2.-EJERCICIO\nla cantidad de numeros en la lista es de {len(lista_numeros)}")# cuantos numero tiene la lista
    nset= set(lista_numeros)
    N=0
    for n in nset:
        if (n>N):
            N=n
        else:
            pass
    print(f"el numero mas alto y el que se eliminara {N}")
    nset.remove(N)
    lista_numeros=list(nset)
    print(lista_numeros)
    return lista_numeros
#2.-PROMEDIO DE LOS NUMEROS
def promedio(lista_numeros):
    promedio=0
    N=len(lista_numeros)#cantidad de numeros en la lista
    print(f"La cantidad de numeros en la nueva lista {N}")
    for n in lista_numeros:
        promedio = promedio+n
    promedio = promedio/N
    print(f"se imprime el promedio de la lista {promedio}")
lista_numeros=reducir_lista()
promedio(lista_numeros)
#
#2.-EJERCICIO otra solucion
print("\n2.-EJERCICIO otra sol.")
lista_numeros = [1, 2, 15, 7, 2, 8]
#2.-REDUCIR LISTA
def reducir_lista2(lista):
    lista = list(set(lista))
    print(f"Se imprime la lista ordenada {lista}")
    lista.sort()
    print(f"Se imprime la lista {lista}")
    lista.pop(-1)
    print(f"Se imprime la lista sin el numero mayor {lista}")
    return lista
#2.-PROMEDIO DE LA LISTA
def promedio2(lista):
    valor_medio = sum(lista) / len(lista)
    return valor_medio
lista=reducir_lista2(lista_numeros)
lista=promedio2(lista)
print(f"Se imprime el promedio de la lista {lista}")
#
#3.-EJERCICIO crea una funcion llamada lanzar moneda que devuelva el resultado de lanzar una moneda (al azar). dicha funcion debe
# poder devolver los resultados "cara" o "cruz" y no debe recibir argumentos para funcionar
# crea una segunda funcion llamada probar_suerte, que tome dos argumentos el primero, debe ser el resultado del lanzamiento de la
# moneda. el segundo argumento sera una lista de numeros cualquiera (debes crear una lista con valores y llamarla lista_numeros)
print("\n3.-EJERCICIO")
from random import *
lista_numeros=[1,2,3,2,3,2]
#3.-LANZAR LA MONEDA
def lanzar_moneda():
    lista=["Cara","Cruz"]
    lista=choice(lista)
    return lista
#3.-PROBAR SUERTE DE LA MONEDA
def probar_suerte(lista,lista_numeros):
    lista=lista.lower()
    print(f"La lista es {lista_numeros} la moneda es {lista}")
    if(lista == "cara"):
        lista_numeros=[]
        return f"La lista se autodestruira, la lista esta vacia {lista_numeros}"
    else:
        return f"La lista fue salvada {lista_numeros}"
lista=lanzar_moneda()
lista=probar_suerte(lista,lista_numeros)
print(lista)
#3.-EJERCICIO otra solucion
print("\n3.-EJERCICIO otra solucion")
lista_numeros = [1, 2, 15, 7, 2, 8]
import random
#3.-LANZAMIENTO DE MONEDA
def lanzar_moneda2():
    resultado = random.choice(["Cara", "Cruz"])
    return resultado
#3.-PROBAR SUERTE
def probar_suerte2(moneda, lista):
    if moneda == "Cara":
        print("La lista se autodestruirá")
        return []
    elif moneda == "Cruz":
        print("La lista fue salvada")
        return lista
moneda=lanzar_moneda2()
moneda=probar_suerte2(moneda,lista_numeros)
print(moneda)
