#DICCIONARIO = es una coleccion de pares, una clave y un valor asociado.
#las claves no se pueden repetir,
#ESTRUCTURA
mi_dic = {'c1':'valor1', 'c2':'valor2', 'c3':'valor3'}
#no tienen un indice como las listas, se buscan en base a las claves
#en los diccionarios no importa el orden, ya que se busca por la clave
#las claves deben ser unicas, los valores pueden repetirse

#1 - declarar
diccionario = {'c1':'valor1', 'c2':'valor2'}
print(diccionario)

#2 - llamar un VALOR por su CLAVE
resultado = diccionario['c1']
print(resultado)

#3 - DICCIONARIO DE CLIENTE CONSULTA DE APELLIDO
cliente = {'nombre':'juan', 'apellido':'fuentes', 'peso':88, 'talla':1.76}
consulta = {cliente['apellido']}
print(consulta)

#4 - LISTAS y DICCIONARIOS dentro del DICCIONARIO
dic = {'c1':55, 'c2':[10,20,30], 'c3':{'s1':100, 's2':200}}
print(dic['c2'][1])#imprimir la clave 2 el elemento 1.. los elementos comienzan desde la poscicion 0
print(dic['c3']['s2'])#imprimir la clave 3 el valor de la clave s2

#5 - EJEMPLO de impresion con MAYUSCULA
dic = {'c1':['a','b','c'], 'c2':['d','e','f']}
print(dic['c2'][1].upper())

#6 - AGREGAR ELEMENTO A DICCIONARIO
dic2 = {1:'a', 2:'b'}
print(dic2)
dic2[3] = 'c'#AGREGAR un nuevo elemento al dicionario
print(dic2)

#7 - SOBRESCRIBIR ELEMENTOS cambias a MAYUSCULA
dic2[2] = 'B'
print(dic2)

#8 - CONOCER LAS LLAVES Y VALORES
print(dic2.keys())#para conocer las LLAVES
print(dic2.values())#para conocer los VALORES

#9 - CONOCER VALOR CON LLAVE ASOCIADA
print(dic2.items())





