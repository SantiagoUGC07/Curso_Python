#1.-EJERCICIO
#Crea una funcion llamada devolver_distintos() que reciba 3 integers como parametros
#si la suma de los 3 numeros es mayor a 15, va a devolver el numero mayor.
#si la suma de los 3 numeros es menor a 10, va a devolver el numero menor.
#si la suma de los 3 numeros es un valor entre 10 y 15 (incluidos) va a devolver el numero de valor intermedio
print("1.-EJERCICIO")
def devolver_distintos(*args):
    suma=0
    print(type(args))#lo recibe como tupple
    for arg in args:
        suma+=arg
    if(suma >15):
        mayor=max(args)
        return f"el numero mayor es: {mayor}"
    elif(suma<10):
        menor=min(args)
        return f"el numero menor es: {menor}"
    else:
        lista=list(set(args))
        return f"{lista[1]}"
print(devolver_distintos(6,4,3))
#
#2.-EJERCICIO
#Escribe una funcion (puedes ponerle cualquier nombre que quieras) que reciba cualquier palabra como parametro,
#y que devuelva todas sus letras unicas (sin repetir) pero en orden alfebetico.
#por ejemplo si al invocar esta funcion pasamos la palabra "entretenido", deberia devolver ['d','e','i','n','o','r','t']
print("\n2.-EJERICIO")
def palabras(*args):
    print(f"la palabra recibida es {args}")
    palabra=list(set(args))#eliminar letras repetidas, y convertir a lista
    palabra.sort()#ordenar la lista en forma alfabetica
    return f"la palabra resultante es {palabra}"
args=("entretenido")#tambien se puede enviar en forma de string
print(palabras(*args))
#mi_set = set() #generar un set vacio
print("\n2.-EJERICIO otra solucion")
def letras_unicas(palabra):
    mi_set = set()#se almacenan letra por letra
    for letra in palabra:
        mi_set.add(letra)
    mi_lista = list(mi_set)
    mi_lista.sort()
    return f"{mi_lista}"
print(letras_unicas("entretenido"))
#
#3.-EJERCICIO
#Escribe una funcion que requiera una cantidad indefinida de argumentos. lo que hara esta funcion es devolver True
#si en algun momento se ha ingresado al numero cero, repetido dos veces consecutivas.
#por ejemplo:
#(5,6,1,0,0,9,3,5)>>>TRUE
#[6,0,5,1,0,3,0,1]>>>FALSE
print("\n3.-EJERICIO")
def numeroCero(*args):#esta solucion no sirve para ver solo dos ceros seguidos.
    i = 0
    for value in args:
        if value == 0:
            i+=1
        else:
            pass
    print(i)
    if(i>=2):
            i=True
            return f"{args}>>>{i}"
    else:
            i=False
            return f"{args}>>>{i}"
numero=[1,2,3,34,5,42,3,0,450,12,3,0]
print(numeroCero(*numero))
#
print("\n3.-EJERICIO otra solucion")
def ceros_vecinos(*args):
    contador = 0
    for num in args:
        if contador + 1 == len(args):#analiza que la cadena corresponda a la contador
            return False
        elif args[contador] == 0 and args[contador + 1] == 0:#analiza que dos numeros sean igual a cero, yendo elemento por elemento
            #dentro de los args.
            return True
        else:#si no hay dos ceros juntos continuado con la secuencia
            contador += 1
    return False#si no encuentra ceros seguidos devuelve false
print(ceros_vecinos(1,2,3,34,5,42,3,450,12,3,0,0))

#
#4.-EJERCICIO
#Escribe una funcion llamada contar_primos() que requiera un solo argumento numerico
#Esta funcion va a mostrar en pantalla cuantos numeros primos hay en el rango que va desde cero hasta ese numero incluido,
#y va a devolver la cantidad de numeros primos que encontro.
#aclaracion, por convencion el 0 y el 1 no se consideran primos.
print("\n4.-EJERICIO")
def contar_primos(*args):#esta solucion sirve para una cantidad indeterminada de numeros
    nprimos = []
    for numero in args:
        ci = 0
        i = 2
        if numero==2:
            i=1
        while i<numero:
            if(numero%i==0 and ci==0 and numero!=2):
                print(f"{numero} % {i}")
                ci+=1
            elif(ci==0):
                nprimos.append(numero)
                break
            i+=1
    print(nprimos)
numeros=(1,2,3,4,5,4,6,67,57,5,4,0)
contar_primos(*numeros)
#
print("\n4.-EJERICIO otra solucion")
def contar_primos2(numero):#esta solucion solo sirve para un numero primo.
    primos = [2]
    iteracion = 3
    if numero < 2:
        return 0
    while iteracion <= numero:
        for n in range(3,iteracion,2):
            if iteracion%n==0:
                iteracion +=2
                break
            else:
                primos.apped(iteracion)
                iteracion += 2
    print(primos)#se imprimen los numeros primos
    return len(primos)
print(contar_primos2(1))
