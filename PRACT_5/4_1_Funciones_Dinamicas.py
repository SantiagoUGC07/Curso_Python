#Funciones Dinamicas
#que una funcion reciba una lista de numeros
def chequear_3_cifras(numero):
    return numero in range(100,1000)

resultado = chequear_3_cifras(658)
print(resultado)#como es un numero de tres cifras nos regresa un true

#VERIFICAR TODOS LOS ELEMENTOS DE UNA LISTA Y VERIFICAR SI ALGUNO TIENE 3 CIFRAS
def chequear_3_cifras2(lista):
    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass#que pase para que siga con la ejecucion de las demas
    return False #se coloca aqui por que una vez termine el ciclo y no encuentre nada devuelve un false
resultado = chequear_3_cifras2([55,99,6000])
print(resultado)#como nunca entra a la funcion y no puede devolver nada nos devuelve un none
#DEVUELVE EL TRUE POR QUE SI HAY UN NUMERO DE 3 CIFRAS
resultado = chequear_3_cifras2([553,99,6000])
print(resultado)#nos devuelve un true ni siquiera pasa por los demas numeros.

#SI EL NUMERO TIENE 3 CIFRAS AGREGARLO A UNA LISTA
def chequear_3_cifras3(lista):
    lista_3_cifras=[]
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras
resultado = chequear_3_cifras3([553,999,6000])
print(resultado)#imprime la lista creada de los numeros de 3 cifras


