import os
from datetime import datetime
def registrar_ingresos(persona):
    # se creo el archivo.csv y se colocaron dos columnas con nombre (Nombre,Hora) para despues leer el archivo
    f = open('prueba.csv','a+')#se lee el archivo, se tiene que haber creado antes
    '''
    lista_datos = f.readlines()#se len la cantidad de filas
    print(lista_datos)
    nombre_registro = []
    for linea in lista_datos:#se quenea un lista de datos apartir de las columnas
        ingreso = linea.split(',')#se genera un espacio
        print(ingreso)
        nombre_registro.append(ingreso[0])#se ingresa el nombre del usuario
    if persona not in nombre_registro:
        ahora = datetime.now()#se ingresa la fecha de la persona
        string_ahora = ahora.strftime('%H:%M:%S')
        f.writelines(f'\n{persona}, {string_ahora}')
    '''
    ahora = datetime.now()  # se ingresa la fecha de la persona
    string_ahora = ahora.strftime('%H:%M:%S')
    f.writelines(f'\n{persona}, {string_ahora}')

registrar_ingresos("Santiago")