#LIBRERIAS
from pathlib import Path, PureWindowsPath
import os
from os import system
import pathlib

#**SALUDO**
def saludo():
    print("Hola buen dia")
    # RUTA DE ALMACENAMIENTO
    recetas = Path("Recetas")
    ruta = os.getcwd()
    print(f"las recetas se encuentran en: {Path(ruta, Path(recetas))}")
    # CANTIDAD DE RECETAS TOTALES.
    NRTotales = recetas_Totales(recetas)
    print(f"Exisen {NRTotales} en total en las diferentes carpetas")

def recetas_Totales(recetas):
    i=0
    for txt in Path(recetas).glob("**/*.txt"):
        i+=1
    return i

#**METODOS AUX**
def encontrar_Opcion(fileNames,opcion):
    i=1
    numeros='123456'
    if opcion in numeros and len(opcion) == 1:  # evitar que se introduzca mas de un numero
        es_valida = True  # si no es una letra y no es mas de un digito
    else:
        print("No has eledigo una opcion correcta")  # si es una letra y es mas de un digito
        es_valida=False
        return es_valida, "nada"
    opcion=int(opcion)#se cambia el string por inter
    for file in fileNames:
        if opcion==i:
            return es_valida,file  # se devuelve el nombre de la carpeta
        i+=1

def menu_categorias():
    i=1
    print("\nMENU DE CATEGORIAS DE RECETAS")
    categorias = 'C:/Users/uri/Desktop/Curso_Phyton/PRACT_6/Recetas/'
    #ESTE METODO IMPRIME SOLO LA SUBCARPETAS DE LA CARPETA DE RECETAS
    #os.scandir read all files and directories in rute
    with os.scandir(categorias) as ficheros:#esto sirve para abrir os.scandir(categorias) como ficheros evitar escribir mas
        #en la sig linea.
        subdirectorios = [fichero.name for fichero in ficheros if fichero.is_dir()]#se guardan los file en una lista por los []
        #fichero.name this method returns the name of the file. (any file).
        #.is_dir() This method returns True if the entry is a directory otherwise returns False. true when is a file and false when is .txt
    #print(type(subdirectorios)) es una lista
    for subdirect in subdirectorios:
        print(f"{i}.- {subdirect}")
        i+=1
    '''
        #ESTE METODO IMPRIME TODO LO QUE HAY DENTRO DE LA CARPETA RECETAS
        directorio = pathlib.Path(categorias)
        for fichero in directorio.iterdir():
            print(fichero.name)#.name imprime el nombre de la carpeta
    '''
    return subdirectorios,categorias

def menu_recetas(carpeta):
    i=1
    recetas = Path('C:/Users/uri/Desktop/Curso_Phyton/PRACT_6/Recetas/', Path(carpeta))#se agrega el nombre de la carpeta a la que se quiere acceder
    print(f"\nMENU DE RECETAS DE {carpeta.upper()}")
    #ESTE METODO IMPRIME SOLO LA SUBCARPETAS DE LA CARPETA DE RECETAS
    #os.scandir read all files and directories in rute
    with os.scandir(recetas) as txts:#esto sirve para abrir os.scandir(categorias) como ficheros evitar escribir mas
        #en la sig linea.
        files = [txt.name for txt in txts if not txt.is_dir()]#se guardan los file en una lista por los []
        #fichero.name this method returns the name of the file. (any file).
        #.is_dir() This method returns True if the entry is a directory otherwise returns False. true when is a file and false when is .txt
    #print(type(subdirectorios)) es una lista
    for file in files:
        print(f"{i}.- {file}")
        i+=1
    return files,recetas

def menu_opciones():
    i=1
    opciones= ["Leer receta","Crear receta","Crear categoría","Eliminar receta","Eliminar categoria","Finalizar programa"]
    for opci in opciones:
        print(f"{i}.- {opci}")
        i+=1
    return opciones

#def leer_Receta():
    file=open()

def leer_Receta(ruta_Recetas,file):
    ruta=Path(ruta_Recetas,file)
    archivo=open(ruta,"r")
    print(f"\nLeyendo el archivo {file}...")
    print(archivo.read())
    print("\n")

def crear_Receta(ruta_Categorias,carpeta):
    tipo='.txt'#para agregarle el tipo de archivo
    nuevo_File=input("Introduce el nombre para la nueva receta: ")
    nuevo_File=nuevo_File+tipo#sumar los strings del nombre del archivo y el tipo
    ruta = Path(ruta_Categorias, Path(carpeta)) / nuevo_File#sumar la ruta de la carpeta con el archivo
    f = open(ruta, "w")#se abre el archivo en modo escritura y este a su vez se crea
    f.write("Nueva receta")#se introduce un texto

def crear_Categoria(ruta_Categorias):
    nueva_Carpeta=input("Introduce el nombre para la nueva carpeta: ")
    ruta = Path(ruta_Categorias,Path(nueva_Carpeta))
    os.makedirs(ruta)#crear carpeta
    print(f"La carpeta {nueva_Carpeta} fue creada con exito")

def eliminar_Categoria(ruta_Categorias,carpeta):
    ruta = Path(ruta_Categorias,Path(carpeta))
    os.rmdir(ruta)#eliminar carpeta
    print(f"\n La carpeta {carpeta} fue eliminada con exito\n")

def eliminar_Receta(ruta_Recetas,file):
    ruta = Path(ruta_Recetas,Path(file))
    os.remove(ruta)#eliminar carpeta
    print(f"\nLa carpeta {file} fue eliminada con exito\n")

#**NAVEGACION**
def navegacion_Categorias():
    es_valida = True
    while es_valida == True:
        subdirectorios,ruta_Categorias=menu_categorias()
        opcion=input("Ingrese el numero de la categoria: ")#identificar si es numero
        #MOSTRAR_RECETAS
        es_valida,carpeta = encontrar_Opcion(subdirectorios,opcion)#se recibe el nombre de la carpeta
        return ruta_Categorias,carpeta

def navegacion_recetas(carpeta):
    es_valida = True
    while es_valida == True:
        fileNames,ruta_Recetas=menu_recetas(carpeta)
        opcion = input("Ingrese el numero de la receta: ")# identificar si es numero
        es_valida, file = encontrar_Opcion(fileNames, opcion)
        return ruta_Recetas,file

def navegacion_Menu_Principal():
    es_valida = True
    while es_valida == True:
        opciones_menu=menu_opciones()#imprimir menu de opciones
        opcion=input("Elige el numero de una opcion: ")
        es_valida, opcion_menu = encontrar_Opcion(opciones_menu, opcion)
        return opcion

#**MATCH**
def casos():
    es_valida=True
    while(es_valida==True):
        opcion=navegacion_Menu_Principal()
        match opcion:
            case "1":
                #LEER RECETA
                ruta_Categorias,carpeta=navegacion_Categorias()
                ruta_Recetas,file=navegacion_recetas(carpeta)
                leer_Receta(ruta_Recetas,file)
            case "2":
                #CREAR RECETA
                ruta_Categorias,carpeta=navegacion_Categorias()
                crear_Receta(ruta_Categorias,carpeta)
            case "3":
                #CREAR CATEGORIA
                ruta_Categorias,carpeta=navegacion_Categorias()
                crear_Categoria(ruta_Categorias)
            case "4":
                #ELIMINAR RECETA
                ruta_Categorias, carpeta = navegacion_Categorias()
                ruta_Recetas, file = navegacion_recetas(carpeta)
                eliminar_Receta(ruta_Recetas, file)
            case "5":
                #ELIMINAR CATEGORIA
                ruta_Categorias,carpeta=navegacion_Categorias()
                eliminar_Categoria(ruta_Categorias,carpeta)
            case "6":
                #FINALIZAR PROGRAMA
                es_valida=False
                print("\nfinalizando")
        input("")
        os.system ("cls")

#**MAIN**
#SALUDO
saludo()
#INCIO DE PROGRAMA
casos()