#1.-EJERCICIO imprimir los numeros del 10 al 0
numero = 10
while numero >= 0:
    print(numero)
    numero -= 1

#2.-EJERCICIO imprimir los numeros del 50 que son divisibles por 5
numero = 50
while numero >= 0:
    if numero % 5 == 0:
        print(numero)
    numero -=1

#3.-EJERCICIO imprimir hasta llegar a un negativo.
lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for value in lista_numeros:
    if value < 0:
        break
    print(value)
