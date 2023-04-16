#Modulo PATH
'''
pathlib: es un modulo para manipular archivos
'''
from pathlib import Path, PureWindowsPath #se importa pure windows path para importa de manera pura las rutas de windows

carpeta = Path('C:/Users/uri/Desktop/Curso_Phyton/PRACT_6/Alternativo/pruebaAlternativo.txt')
print(carpeta.read_text())#se imprime el texto dentro del archivo usando el metodo read_text por que ahora path contiene otro metodos
print(carpeta.name)#Imprime el nombre del archivo
print(carpeta.suffix)#Imprime que tipo de archivo es
print(carpeta.stem)#eñ nombre del archivo sin el tipo

#ver si el archivo existe
if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Genial, existe")

#RUTA WINDOWS
rutaWindows = PureWindowsPath(carpeta)
print(rutaWindows)#se imprime la ruta de windows