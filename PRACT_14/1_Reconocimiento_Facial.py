#Reconocimiento facial
'''
Detecta y ubica las imagenes de un rostro,
analisis facial, el software toma en cuenta los punto de referencia claves de un rostro a otro
convertir imagen en datos cambia los rostros a datos para crear una huella facial
buscar coincidencias analiza el rostro y lo compara con una base de datos para encotrar el rostro
'''
import dlib
from cv2 import cv2
import cv2
import face_recognition as fr

#----CARGAR IMAGENES----
foto_control = fr.load_image_file("foto1_reducida.jpg")
foto_prueba = fr.load_image_file("foto2_reducida.jpg")
#Pasar imagenes a RGB
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

#LOCALIZAR CARA FOTO CONTROL
lugar_cara_A = fr.face_locations(foto_control)[0]#se envia el primer elemento de esta imagen el 0
cara_codificada_A = fr.face_encodings(foto_control)[0]#se codifica la cara para poder encontrarla y guardarla en la variable
print(lugar_cara_A) # se imprimen los parametros para colocar en los indices de lugar cara A  (167, 270, 322, 115)
#(167, 270, 322, 115) = 167 linea horizontal superior, 270 linea vertical derecha, 322 linea horizontal inferior, 115 linea vertical izquierda
#Mostrar rectangulo
cv2.rectangle(foto_control, #se colocan los pixel donde se encontran las imagenes
              (lugar_cara_A[3], lugar_cara_A[0]),#vertice superior x,y izquierdo
              (lugar_cara_A[1], lugar_cara_A[2]),#vertice inferior x,y derecho
              (0, 255, 0),#color del rectangulo
              2)#numero del borde
#LOCALIZAR CARA FOTO PRUEBA
lugar_cara_B = fr.face_locations(foto_prueba)[0]#se envia el primer elemento de esta imagen el 0
cara_codificada_B = fr.face_encodings(foto_prueba)[0]#se codifica la cara
#Mostrar rectangulo
cv2.rectangle(foto_prueba,
              (lugar_cara_B[3], lugar_cara_B[0]),
              (lugar_cara_B[1], lugar_cara_B[2]),
              (0, 255, 0),
              2)

#COMPARAR CARAS
#resultado = fr.compare_faces([cara_codificada_A],cara_codificada_B,0.9)#la distancia en diferencia actual es de 0.8 por lo que se pone un 0.9 para que el resultado en comparacion sea true
resultado = fr.compare_faces([cara_codificada_A],cara_codificada_B)#se comparan las caras
print(resultado)#se imprime el resultado de la comparacion
#MEDIR DISTANCIA DE DIFERENCIA en la comparacion.... para medir la distancia del reconocimiento, entre mayor distancia menos parecido
distancia = fr.face_distance(([cara_codificada_A]), cara_codificada_B)
print(distancia)

#MOSTRAR RESULTADO
cv2.putText(foto_prueba,
            f'{resultado}{distancia.round((2))}',#se redondea con round y se pone 2 para dos decimales
            (50,50),#una distancia para el lugar donde aparezcan los valores
            cv2.FONT_HERSHEY_COMPLEX,#el tipo de la letra
            1,#la escala de la letra
            (0, 255, 0),#color del valor (se puede cambiar el color si es verdadero o no)
            2)

#MOSTRAR IMAGENES
cv2.imshow('Foto control',foto_control)
cv2.imshow('Foto prueba', foto_prueba)
#MANTENER PROGRAMA ABIERTO
cv2.waitKey(0)#cerrar programa cuando apriete 0


