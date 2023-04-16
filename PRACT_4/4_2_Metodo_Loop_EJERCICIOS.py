#1.-EJERCICIO imprimir el saludo a cada nombre con for
alumnos_clase = ["Maria", "Jose", "Carlos", "Martina", "Isabel", "Tomas", "Daniela"]
for saludo in alumnos_clase:
    print("Hola " + saludo)

#2.-EJERCICIO imprimir la suma de todos los numeros de la lista
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0
for value in lista_numeros:
    suma_numeros = suma_numeros + value
print(suma_numeros)

#3.-EJERCICIO dividir los pare e impares de la lista en dos variables y sumarlos
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0
for value in lista_numeros:
    if value % 2 == 0:
        suma_pares = suma_pares + value
    else:
        suma_impares = suma_impares +value
print(suma_pares)
print(suma_impares)