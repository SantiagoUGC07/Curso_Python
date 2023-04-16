#1.-EJERCICIO crear una lista de 2500 al 2586 con range
mi_lista = list(range(2500,2586))
print(mi_lista)

#2.-EJERCICIO crear una lista y sumar con potencia
suma_cuadrados = 0
lista_numeros= list(range(1,16))
for value in lista_numeros:
    suma_cuadrados = suma_cuadrados + (value**2)
print(suma_cuadrados)
