#Directorios
#para interactuar con los directorios del ordenador se ocupa el modulo os.
'''
para que python detecte una barra invetida en una direccion se coloca doble barra invertida \\
Modulos
Path: es un modulto para detectar las barras invetidas
os: es un modulo para interactuar con los directorios del ordenador
'''
import os
#1.-MOSTRAR LA CARPETA ACTUAL
ruta = os.getcwd()#el modulo os con su metodo getcwd(currentworkdirectory)
print(ruta)#se muestra la ruta ta el archivo actual
#2.-ACCEDER A CARPETAS DISTITNAS
ruta= os.chdir('C:\\Users\\uri\\Desktop\\Curso_Phyton\\PRACT_6\\Alternativo')#para acceder a una ruta distinta
print(ruta)#nos manda none por que no esta seleccionando ningun archivo el os.chdir
archivo = open('pruebaAlternativo.txt')
print(archivo.read())
archivo.close()

#3.-CREAR CARPETAS
#  ruta=os.makedirs('C:\\Users\\uri\\Desktop\\Curso_Phyton\\PRACT_6\\Alternativo\\otra')#accedemos a la carpeta
#  alternativo para crear carpeta "otra"

#4.-RECIBIR LAS DOS PARTES DE LA RUTA
ruta= 'C:\\Users\\uri\\Desktop\\Curso_Phyton\\PRACT_6\\Alternativo\\pruebaAlternativo.txt'
elemento = os.path.basename(ruta)#se accede a la base la ruta.
print(elemento)#se imprime la base de la ruta que en este caso es "pruebaAlternativo.txt"
elemento2 = os.path.dirname(ruta)#se accede al nombre del directorio
print(elemento2)#se imprime el resto de la ruta "C:\"

#5.-RECIBIR LAS RUTAS DE DIRNAME Y BASENAME EN UNA TUPLA
elemento3 = os.path.split(ruta)
print(ruta)

#6.-ELIMINAR CARPETA
# os.rmdir('C:\\Users\\uri\\Desktop\\Curso_Phyton\\PRACT_6\\Alternativo\\otra')#Eliminar la carpeta otra

#7.-COMO ABRIR UN ARCHIVO
print("7.-abrir un archivo")
otro_archivo = open('C:\\Users\\uri\\Desktop\\Curso_Phyton\\PRACT_6\\Alternativo\\pruebaAlternativo.txt')
print(otro_archivo.read())

#8.-PARA ACCDER A DIFERENTES ARCHIVOS EN UNA CARPETA EN MAC O WINDOWS
#path es un objeto
from pathlib import Path
print("8.-abrir un archivo eb MAC o WINDOWS")
#para que cualquier sistema operativo pueda leer la ruta se escribe de la sig manera
carpeta = Path('C:/Users/uri/Desktop/Curso_Phyton/PRACT_6/Alternativo')#para colocarnos en una carpeta
archivo = carpeta / 'pruebaAlternativo.txt' #para accede a 'otro_archivo.txt' dentro de la carpeta 'carpeta'
mi_archivo  = open(archivo)
print(mi_archivo.read())#Se imprime lo que hay dentro de 'otro_archivo.txt'
mi_archivo.close()#recuerda cerrar el archivo.

print("8.-abrir un archivo eb MAC o WINDOWS OTRA FORMA")
#para colocarnos en una carpeta y seleccionar el archivo
carpeta = Path('C:/Users/uri/Desktop/Curso_Phyton/PRACT_6/Alternativo') / 'pruebaAlternativo.txt'
mi_archivo  = open(carpeta)
print(mi_archivo.read())
mi_archivo.close()

