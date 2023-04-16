#MODULO MATH
'''
contiene las funciones matematicas
'''
import math

print("Redondear num hacia abajo")
resultado = math.floor(89.665)#permite redondear un numero hacia abajo
print(resultado)

print("\nRedondear num hacia arriba")
resultado = math.ceil(89.665)
print(resultado)

print("\nfuncion log")
#a que numero se debe exponer 5 para que de 100
resultado = math.log(100,5)
print(resultado)
#a que numero se debe exponer 5 para que de 25
resultado = math.log(25,5)
print(resultado)

print("\ntangente, coseno")
resultado = math.tan(45)
print(resultado)
resultado = math.cos(45)
print(resultado)


