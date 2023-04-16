#1.-EJERCICIO
#Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro, y devuelva su contenido (read).
def abrir_leer():
    archivo = open("prueba.txt","r")
    return f"{archivo.read()}"
print(abrir_leer())


#2.-EJERCICIO
#Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro, y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"
'''
def sobrescribir(archivo):
    archivo_sobrescribir = open(archivo, "w")
    archivo_sobrescribir.write("contenido eliminado")
'''
#3.-EJERCICIO
#Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro,
#y lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución". Finalmente, debe cerrar el archivo abierto.
'''
def registro_error(archivo):
    archivo_registro = open(archivo,"a")
    archivo_registro.write("se ha registrado un error de ejecución")
    archivo_registro.close()
'''
