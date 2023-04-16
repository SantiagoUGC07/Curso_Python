#MEDIR EL TIEMPO DE EJECUCION DE UN CODIGO
'''
time:
nos permite establecer marcas de tiempo, para medir el tiempo que paso de una a otra
time no funciona cuando las funciones son muy pequeñas ya que el tiempo puede ser cero 0
timeit:
tiene la funcion de medir el tiempo de ejecucion del bloque que se le mande
'''
import time

#Haremos la prueba de los dos modulos time y timeit para medir el tiempo de ejecucion de dos codigos
def prueba_for(numero):#crea una lista dependiendo el numero que diga el usuario
    lista = []
    for num in range(1,numero + 1):
        lista.append(num)
    return lista

def prueba_while(numero):#crea una lista dependiendo el numero que diga el usuario
    lista=[]
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista

#1.-EJECUTANDO CODIGO
print(prueba_for(15))
print(prueba_while(15))

#2.-MIDIENDO EL TIEMPO CON time
print("\nMidiendo el tiempo con time")
inicio=time.time()
prueba_for(1500000)
fin=time.time()
print("tiempo de ejecucion 1er codigo")
print(fin-inicio)

inicio=time.time()
prueba_while(1500000)
fin=time.time()
print("tiempo de ejecucion 2nd codigo")
print(fin-inicio)

#2.-MIDIENDO EL TIEMPO CON timeit
import timeit
print("\nMidiendo el tiempo con timeit 1er codigo")
#se llama a la funcion de la sig manera
declaracion = '''
prueba_for(10)
'''
#se agrega la funcion a la variable de la sig manera
mi_setup = '''
def prueba_for(numero):
    lista = []
    for num in range(1,numero + 1):
        lista.append(num)
    return lista
'''
print("tiempo de ejecucion 1er codigo")
duracion=timeit.timeit(declaracion, mi_setup, number = 100000)#number es la cantidad de veces que se ejecutara la funcion para medir su eficiencia
print(duracion)

print("\nMidiendo el tiempo con timeit 2nd codigo")
declaracion2 = '''
prueba_while(10)
'''
mi_setup2 = '''
def prueba_while(numero):
    lista=[]
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
'''
print("tiempo de ejecucion 2nd codigo")
duracion2=timeit.timeit(declaracion2, mi_setup2, number = 100000)#number es la cantidad de veces que se ejecutara la funcion para medir su eficiencia
print(duracion2)