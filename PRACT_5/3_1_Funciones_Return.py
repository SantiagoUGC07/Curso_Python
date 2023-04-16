#Return
def multiplicar(numero1,numero2):
    return numero1 * numero2#Devuelve la informacion
print(multiplicar(5,10))#recibir la variable con print

#IMPRIMIR el valor devuelto de return con print
def multiplicar2(numero1,numero2):
    return numero1 * numero2#Devuelve la informacion
resultado = multiplicar(5,200)#recibir la variable en otra para despues imprimir
print(resultado)

#RECIBIR la variable de la funcion con otra
def multiplicar3(numero1,numero2):
    return numero1 * numero2#Devuelve la informacion
resultado = multiplicar(5,200)#recibir la variable en otra para despues imprimir
print(resultado)

#RECIBIR la varible en otra, tener cuidado con el tipo de variable.
def multiplicar3(numero1,numero2):
    total = numero1 * numero2
    return total#Devuelve la informacion
resultado = multiplicar(5,200)#recibir la variable en otra para despues imprimir
print(resultado)