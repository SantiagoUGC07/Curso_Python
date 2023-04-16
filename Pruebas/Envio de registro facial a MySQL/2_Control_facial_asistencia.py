#generar una base de datos con rostros para identificar si es la persona
import dlib
from cv2 import cv2
import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime
from MySQL import envioDatos

#-----CREAR BASE DE DATOS------
ruta = 'Empleados'#el nombre de la carpeta
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)
#print(lista_empleados) # Ver la lista de las imagenes de los empleados agregados
for nombre in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}\{nombre}')#Generar una nueva lista sin .JPG
    mis_imagenes.append(imagen_actual)#Agregarlos a una nueva lista
    nombres_empleados.append(os.path.splitext(nombre)[0])#se cargan los nombres de los empleados en una lista
print(nombres_empleados)#para ver la lista de los empleados sin el jpg

#-----CODIFICAR IMAGENES------
def codificar(imagenes):
    #crear una lista nueva
    lista_codificada = []
    #pasar todas las imagenes a rgb
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB)
        #Codificar (encontrar la cara)
        codificado = fr.face_encodings(imagen)[0]
        #agregar a la lista
        lista_codificada.append(codificado)
    #Devolver lista codificada
    return lista_codificada
#Lista con todas las imagenes codificadas
lista_empleados_codificada = codificar(mis_imagenes)
print(len(lista_empleados_codificada))#ver la cantidad de los elementos de la lista

#REGISTRAR LOS INGRESOS
def registrar_ingresos(persona):
    # se creo el archivo.csv y se colocaron dos columnas con nombre (Nombre,Hora) para despues leer el archivo
    f = open('registro.csv','r+')#se lee el archivo
    lista_datos = f.readlines()#se len la cantidad de columndas
    nombre_registro = []
    for linea in lista_datos:#se quenea un lista de datos apartir de las columnas
        ingreso = linea.split(',')#se genera un espacio
        nombre_registro.append(ingreso[0])#se ingresa el nombre del usuario
    if persona not in nombre_registro:
        ahora = datetime.now()#se ingresa la fecha de la persona
        string_ahora = ahora.strftime('%H:%M:%S')
        envioDatos(persona, string_ahora)
        f.writelines(f'\n{persona}, {string_ahora}')


#TOMAR UNA IMAGEN DE CAMARA WEB
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#LEER IMAGENE DE LA CAMARA WEB
exito, imagen  = captura.read()
if not exito:
    print("No se ha podido tomar la captura")
else:
    #Reconocer cara en captura
    cara_captura = fr.face_locations(imagen)#localiza la imagen
    #Codificar cara capturada
    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)
    #Buscar concidencias
    for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):
        coincidencias = fr.compare_faces(lista_empleados_codificada,caracodif )#compara las caras de la lista contra la tomada por la web
        distancias = fr.face_distance(lista_empleados_codificada, caracodif)#para la distancia de diferencia entre la concidencia
        print(distancias)

        indice_concidencia = numpy.argmin(distancias)
        #Mostrar coincidencias si las hay
        if distancias[indice_concidencia] > 0.6:
            print("el valor no concide con ninguno de nuestros empleados")
        else:
            #buscar el nombre del empleado encontrado
            nombre = nombres_empleados[indice_concidencia]
            #crear rectangulo de imagen
            y1, x2, y2, x1 = caraubic#caraubic contiene los valores de los parametros para el rectangulo
            #colocar margen al rectangulo
            cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(imagen, (x1, y2 - 35), (x2,y2), (0, 255, 0), cv2.FILLED)#Filled rellena el rectangulo de color verde
            cv2.putText(imagen, nombre, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255))#poner un texto en la imagen
            #REGISTRAR INGRESOS
            registrar_ingresos(nombre)
            print("Bienvenido al trabajo")
            #mostrar la imagen obtenida
            cv2.imshow('Imagen web', imagen)#mostrar la imagen de la camara web
            #mantener la ventana abierta
            cv2.waitKey(0)



