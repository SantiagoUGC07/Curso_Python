#los string son inmutables(no se puede cambiar contenido ni modificar)
#los string pueden concatenarse usando el simbolo +
#los string pueden multiplicarse usando *
#los string pueden dar salto de linea con """ comillas antes del texto y al final """
#Los string se puede ver si en los substring se encuentran en los string
#se puede verficar la cantidad de caracteres que posee un string con la funcion LEN

#PROPIEDADES DE STRINGS
#1 - Esto nos arroja un error debido a la INMUTABILIDAD
#nombre = "Carina"
#nombre[0] = "K"

#2 - CONCATENAR
n1 = "Kari"
n2 = "na"
print(n1 + n2)

#3 - MULTIPLICACION STRING
print(n1 * 5)

#4 - SALTO DE LINEA es un mismo texto en diferentes lineas
poema = """Mil pequeños peces blancos como si hirviera el color
del agua agua
adios"""
#5 - CONSULTAR SI EXISTE UNA PALABRA con un substring
print("agua" in poema)#agua esta en poema? como si esta envia un true
print("goku" not in poema)#guku no esta en poema? como no esta envia true




