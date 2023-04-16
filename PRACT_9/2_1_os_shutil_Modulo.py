#Modulo os
import os
import shutil
#import send2trash

#1.-EJEMPLO Ver en que directorio me encuentro trabajando

# print(os.getcwd()) #se imprime la ruta donde nos encontramos actualmente
'''
archivo = open("curso.txt", "w")
archivo.write("Hola este es un nuevo archivo")#creamos un archivo
archivo.close()
print(os.listdir())#nos muestra los archivos que tenemos
'''
#2.-EJEMPLO Mover archivos, movemos el archivo que acabamos de crear
#se importa la libreria shutil y se ocupa el modulo move
'''
shutil.move("curso.txt","C:\\Users\\Tomas Garcia\\Desktop\\Curso_Python\\PRACT_9\\carpeta_prueba")
'''

#3.-EJEMPLO metodos de eliminar archivos y carpetas
'''
os.unlink()#elimina un archivo en la ruta que le coloquemos
os.rmdir()#elimina una carpeta vacia, colocar su ruta
shutil.rmtree()#elimina la carpeta con archivos,colocar su ruta cuidado por que no se va a papelera de reciclaje
'''
#4.-EJEMPLO eliminar carpeta a la papelera
'''
existe un modulo que elimina una carpeta y la manda a la papelera, send2trash, installar por cmd
    pip install send2trash
#ejemplo
send2trash.send2trash("curso.txt")
'''

#5.-EJEMPLO walk recorrer por los archivos
#walk muestra el contenido de una carpeta
ruta="C:\\Users\\Tomas Garcia\\Desktop\\Curso_Python"
print(os.walk(ruta))#sirve para recorrer por las carpetas, paara poder ver los nombres se necesita un iterador
#ocupamos en este caso for para ver todas las subcarpetas y archivos dentro de la carpeta python, y continuamente
#va abriendo carpeta, mostrando sus subcarpetas y archivos
#5_1 EJEMPLO
'''
for carpeta,subcarpeta,archivo in os.walk(ruta):#muestra todas las subcarpetas, archivos de la carpeta curso_python
    print(f"en la carpeta: {carpeta}")
    print(f"las subcarpetas son: ")
    for sub in subcarpeta:#muestra la subcarpeta
        print(f"\t{sub}")
        print("los archivos son: ")#muestra el archivo de la subcarpeta
    for arch in archivo:
        print(f"\t{arch}")
    print("\n")
'''
#5_2 EJEMPLO
#Se pueden buscar archivos dentro de las diferentes ramas de la carpeta. usando condicionales
#en este carso buscamos los archivos que comiencen por las letras modul
for carpeta,subcarpeta,archivo in os.walk(ruta):#muestra todas las subcarpetas, archivos de la carpeta curso_python
    print(f"en la carpeta: {carpeta}")
    print(f"las subcarpetas son: ")
    for sub in subcarpeta:#muestra la subcarpeta
        print(f"\t{sub}")
        print("los archivos son: ")#muestra el archivo de la subcarpeta
    for arch in archivo:
        if arch.startswith("modul"):#busca archivos que empiecen por las letras modul
            print(f"\t{arch}")
    print("\n")