#RANDOM es la libreria donde se encuentra el metodo randint
#el nombre del documento debe ser diferente al de la libreria para evitar problemas
from random import randint #esta libreria es para randint

#Solicitar un num aleatorio
from random import * #esta libreria es para uniform
aleatorio = randint(1,50)#siirve para escojer un numero aleatorio
print(aleatorio)

#Solicitar un num decimal aleatorio con la libreria *
aleatorio = uniform(1,5)#nos manda un valor aleatorio en decimal
print(aleatorio)

#Solicitar un num decimal aleatorio con un decimal con la libreria *
aleatorio = round(uniform(1,5),1)#nos manda un valor con solo un decimal
print(aleatorio)

#Imprimir un color aleatorio con la libreria * usando choice
colores = ['azul','rojo','verde','amarillo']
aleatorio = choice(colores)
print(aleatorio)

#Mezcla aleatoria de numeros con la libreria *
numeros = list(range(5,50,5))#el rango de numero del 5 al 50 de 5 en 5
shuffle(numeros)#mezcla los numeros de la lista

print(numeros)




