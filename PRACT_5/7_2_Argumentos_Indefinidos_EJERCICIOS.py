#1.-EJERCICIO Crea una funcion llamada suma_cuadrados que tome una cantidad inderteminada de argumentos numericos,
# y que retorne la suma de sus valores al cuadrado
# por ejemplo para los argumentos suma_cuadrados(1,2,3) debera retornar 14 (1+4+9).
print("1.-EJERCICIO")
def suma_cuadrados(*args):
    suma=0
    for n in args:
        n**=2
        suma = suma+n
    return suma
suma=suma_cuadrados(1,2,3)
print(suma)
#1.-EJERCICIO otra solucion
print("\n1.-EJERCICIO otra solucion")
def suma_cuadrados2(*args):
    suma = 0
    for arg in args:
        suma += arg ** 2#se multiplica el argumento y asu vez se va sumando
    return suma
print(suma_cuadrados2(1,2,3))
#2.-EJERCICIO Crea una funcion llamada suma_absolutos, que tome un conjunto de argumentos de cualquier
# extension, y retorne la suma de sus valores absolutos (es decir, que tome los valores sin signo y los sume,
# o lo que es lo mismo, los considere a todos -negativos y positivos- como positivos).
print("\n2.-EJERCICIO")
def suma_absolutos(*args):
    suma=0
    for arg in args:
        if arg>0:
            suma+= arg
        else:
            suma+=arg*(-1)
    return suma
suma=suma_absolutos(1,2,-3)
print(suma)
#
#2.-EJERCICIO otra solucion
print("\n2.-EJERCICIO otra solucion")
def suma_absolutos(*args):
    suma = 0
    for arg in args:
        suma += abs(arg)
    return suma
print(suma_absolutos(1,2,-3))
#
#3.-EJERCICIO Crea una funcion llamada numeros_persona que reciba, como primer argumento, un nombre, y a continuacion
# una cantidad indefinida de numeros
# la funcion debe devolver el siguiente mensaje
print("\n3.-EJERCICIO")
def numeros_persona(nombre,*args):#los valores de los args recibidos se pueden convertir en tupple
    suma=0
    suma_numeros=sum(args)#La funcion sum para sumar los argumentos
    return (f"{nombre}, la suma de tus numeros es {suma_numeros}")
#lista=["Santiago",1,2,3] SI se declara asi lo tomara como lista y no funcionara
lista=numeros_persona("Santiago",1,2,3)
print(lista)