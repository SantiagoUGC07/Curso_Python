#Modulos para comprimir y descomprimir archivos
'''
para comprimir y descomprimir archivos ocuparemos los sig. modulos
zipfile
shutil
'''
import zipfile
#1.-COMPRIMIR ARCHIVO CON ZIPFILE
'''
mi_zip = zipfile.ZipFile('archivo_comprimido.zip','w')#el nombre del archivo comprimido

mi_zip.write('mi_texto_A.txt')
mi_zip.write('mi_texto_B.txt')
print("Se comprimieron sus archivos")
mi_zip.close()
'''
#2.-DESCOMPRIMIR ARCHIVO CON ZIPFILE
'''
zip_abierto = zipfile.ZipFile('archivo_comprimido.zip','r')#el nombre del archivo a descomprimir
zip_abierto.extractall()#extraer todo el contenido
print("Se descomprimio su archivo")
'''
import shutil
#3.-COMPRIMIR ARCHIVOS CON SHUTIL
'''
carpeta_origen = 'C:\\Users\\Tomas Garcia\\Desktop\\Curso_Python\\PRACT_1'#la carpeta de PRACT_9 sera la que se comprimira
archivo_destino = 'Todo_Comprimido'
# se coloca el nombre del archivo nuevo comprimido, el tipo del archivo comprimido y donde se encuentra la carpeta a comprimir
shutil.make_archive(archivo_destino, "zip", carpeta_origen)
print("Se comprimio tu carpeta PRACT_1 con el nombre Todo_Comprimido")
'''
#4.-DESCOMPRIMIR ARCHIVOS CON SHUTIL
#el nombre del archivo a descomprimir, la carpeta donde se guardara y el tipo del archivo comprimido
shutil.unpack_archive("archivo_comprimido.zip", "Archivo_Descomprimido","zip")
print("Se descomprimido tu archivo")


