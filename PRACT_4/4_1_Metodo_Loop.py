#IMPRIMIR LETRAS
lista = ['a','b','c']
for letra in lista:
    print("letra: " + letra)
print("\n")
#IMPRIMIR LETRA CON FOR
lista2 = ['a','b','c','d']

for letra2 in lista2:
    numero_letra = lista2.index(letra2) + 1
    print(f"letra {numero_letra}: {letra2}")
print("\n")
#IMPRIMIR PALABRAS QUE INICIEN CON L CON EL COMANDO startswith
lista = ('pablo', 'laura', 'fede', 'luis', 'julia')
for nombre in lista:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print('Nombre que no comienza con L')
print("\n")
#SUMAR VALORES DE UNA CADENA.
numeros = [1,2,3,4,5]
mi_valor = 0
for numero in numeros:
    mi_valor = mi_valor + numero
    print(mi_valor)
print("La sumatoria de los numero en la cadena")
print(mi_valor)#este print solo se ejecuta una vez terminada la ejecucion de for
print("\n")
#IMPRIMIR PHYTON LETRA POR LETRA
palabra = 'phyton'
for letra in palabra:
    print(letra)
print("\n")
#IMPRMIR LISTAS QUE TENGAN LISTAS
for a, b in [[1, 2], [3, 4], [5, 6]]:
    #IMPRMIENDO LOS DOS ELEMENTOS A,B DE CADA LISTA
    print(a)
    print(b)
print("\n")
for a, b in [[1, 2], [3, 4], [5, 6]]:
    #IMPRIMIENDO SOLO EL ELEMTO A
    print(a)
print("\n")
#ITERANDO EN UN DICCIONARIO
dic = {'clave1':'a', 'clave2':'b', 'clave3':'c'}
for item in dic.items():
    print(item)
#IMPRIMIR SOLO LOS VALORES DEL DIC.
for item in dic.values():
    print(item)
print("\n")
#IMPRIMIT SOLO LOS DOS VALORES DEL DIC
for a,b in dic.items():
    print(a,b)
