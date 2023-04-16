num1 = 20
num2 = 20.5
print(type(num1))
print(type(num2))

#1 - Esta es una conversion implicita
#ya que num1 paso a ser float al sumarle num2
num1 = num1 + num2
print(type(num1))

#2 - Conversion explicita
NUM1= 5.8
print(NUM1)
print(type(NUM1))
#se indica a que tipo de valor se quiere convertir
NUM2= int(NUM1)
print(NUM2)
print(type(NUM2))

#3 CAMBIAR EDAD A INT Y SUMARLE 1
EDAD = input("Dime tu edad: ")
print(type(EDAD))
EDAD = int(EDAD)
print(type(EDAD))
nueva_EDAD= 1 + EDAD
print(nueva_EDAD)
#ESTO MARCA ERROR por que no sabe que generar.
print("tu nueva edad es" + nueva_EDAD)