#1.-EJERCICIO crear una lista formada por los numeros elavados al cuadrado
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [n ** 2 for n in valores]
print(valores_cuadrado)

#2.-EJERCICIO crear una lista formada por num pares y
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [n for n in valores if n % 2 == 0]
print(valores_pares)

#3.-EJERCICIO
temperatura_fahrenheit = [32, 212, 275]
lista_temperaturas = [((n-32)*(5/9)) for n in temperatura_fahrenheit]
print(lista_temperaturas)