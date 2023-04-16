#1.-EJERCICIO Crea una funcion todos_positivos que reciba una lista de numeros como parametro
#y devuelva True si todos los valores de una lista son positivos, y false si al menos uno de los valores es
#negativo, crea una lista llamada lista_numeros con valores positivos y negativos
def todos_positivos(lista):
    lista_numeros=[]
    for n in lista:
        if (n>0):
            lista_numeros.append(n)
        else:
            lista_numeros.append(n)
            num=False
            continue
    print(lista_numeros)
    return(num)
resultado=todos_positivos([10,231,23,-2,-3,23])
print(resultado)

#1.-EJERCICIO otra solucion
lista_numeros = [1, -50, 502, -5000, 755, 600, 33, 61]
def todos_positivos2(lista_numeros):
    for numero in lista_numeros:
        if numero < 0:
            return False
        else:
            pass
    return True
resultado=todos_positivos2([10,231,23,-2,-3,23])
print(resultado)
#
#
#2.-EJERCICIO crea una funcion suma_menores que sume los numeros de una lista
#almacenada en la variable lista_numeros simpre y cuando sean mayores a 0 y menores a 1000
#y devuelva el resultado de dicha suma
def suma_menores(lista_numeros):
    suma = 0
    for n in lista_numeros:
        if(n>=0 and n<=1000):
            suma += n
        else:
            pass
    return suma
lista_numeros=[2,12,32,3434,54,5454,3]
resultado=suma_menores(lista_numeros)
print(resultado)

#2.-EJERCICIO OTRA SOLUCION
lista_numeros = [1, 50, 500, 5000, 750, 600]
def suma_menores(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        if numero in range(1, 1000):
            suma += numero
        else:
            pass
    return suma
resultado=suma_menores(lista_numeros)
print(resultado)
#
#
#3.-EJERCICIO crea una funcion cantidad_pares que cuente la cantidad de numeros pares
#que existen en una lista lista_numeros y devuelva el resultado de dicha cuenta
def cantidad_pares(lista_numeros):
    suma=0
    for n in lista_numeros:
        if (n%2==0):
            suma+=1
        else:
            pass
    return suma
lista_numeros=[1,2,3,4,5,6,7,8,9,10,12]
resultado=cantidad_pares(lista_numeros)
print(resultado)




