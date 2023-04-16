#BUSCAR INSTRUCCIONES E IMPRIMIRLAS
import shutil
import os
import re
from datetime import datetime
import time
from pathlib import Path
import math

inicio=time.time()

ruta = os.getcwd()#la ruta donde nos encontramos actualmente

#BUSCAR RUTA DEL ARCHIVO COMPRIMIDO un comando adicional que no se ocupo.
def Buscar_ruta_archivo_comprimido():
    target = "Proyecto+Dia+9.zip"#se necesita colocar la extension del archivo
    #initial_dir = 'C:\\'
    initial_dir = 'C:\\Users\\uri\\Desktop\\Curso_Python'#se necesita colocar el doble diagonal
    path = ''
    for root, _, files in os.walk(initial_dir):
        if target in files:
           path = os.path.join(root, target)
           print(path)
           break

#DESCOMPRIMIR ARCHIVO
'''
import shutil
shutil.unpack_archive("Proyecto+Dia+9.zip","Instrucciones_9no_Proyecto","zip")
print("Tu archivo fue descomprimido")
'''

#ENCONTRAR CARPETA
def encontrar_Carpeta():
    for carpeta,subcarpeta,archivo in os.walk(ruta):
        for subcarp in subcarpeta:
            if subcarp.startswith("Instrucciones"):
                subcarp_ruta = os.path.join(carpeta, subcarp)
                print(f"\n{subcarp_ruta}")#imprimir la ruta del archivo donde se encuentran los DIRECTORIOS
                return subcarp_ruta

#BUSCAR EL ARCHIVO DE TEXTO E IMPRIMIR SU RUTA
def Buscar_archivo(subcarp_ruta):
    N=0
    for carpeta,subcarpeta,archivo in os.walk(subcarp_ruta):#muestra todas las subcarpetas, archivos de la carpeta curso_python
        for arch in archivo:
            #if arch.startswith("archivo30"):#busca archivos que empiecen por las letras modul sin necesidad de poner la extension del archivo

            arch_ruta = os.path.join(carpeta,arch)#LOCALIZAR EL archivo
            #print(f"\t{arch}")  # imprimir el nombre del archivo
            #print(f"\n{arch_ruta}")#imprimir la ruta del archivo
            #name_archivo=Path(arch_ruta)   #la ruta del archivo

            mi_archivo = open(arch_ruta)#abrir archivo
            texto=mi_archivo.read()#LEE el archivo
            #print(texto)

            patron = r'[N]\w{3}-\d{5}'
            verificar = re.search(patron, texto)
            if verificar:
                print(f"\t{arch}.....\t{verificar.group()}")#se imprime el archivo y la info relacionada con el parametro
                #print(arch_ruta)#se imprime la ruta del archivo
                N = N + 1
            #else:
            #    print("no se encontro concidencia")
            mi_archivo.close()
    return N

#FUNCION PARA OBTENER LA FECHA DEL DIA DE HOY
def dia():
    fecha_hora=datetime.now()
    return fecha_hora


#LLAMANDO A LAS FUNCIONES
Buscar_ruta_archivo_comprimido()

fecha_hora=dia()
print(f"La fecha del dia de hoy es: {fecha_hora}")
print(f"\tArchivo.....\t\tNRO. SERIE")
subcarp_ruta=encontrar_Carpeta()
N=Buscar_archivo(subcarp_ruta)
print(f"Números encontrados: {N}")

fin=time.time()
duracion= fin-inicio
print(f"La duracion del programa es de: {duracion} seg.")
print(f"La duracion del programa es de: {math.ceil(duracion)} seg. redondeado hacia arriba")




