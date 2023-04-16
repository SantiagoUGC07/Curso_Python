import cv2
import imutils
import numpy
import imutils as np
import os

Datos = 'p'
if not os.path.exists(Datos):
    print('Carpeta creada: ', Datos)
    os.makedirs(Datos)#crear carpeta

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)#para video streaming

x1, y1 = 190, 80
x2, y2 = 450, 398

count = 0

while True:
    ret, frame = cap.read()
    if ret == False: break
    imAux = frame.copy()#cpòar el frame del rectangulo del video capture
    cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),2)#generar rectangulo en medio de la ventana

    objeto = imAux[y1:y2,x1:x2]#almacenar el frame del rectangulo en un objeto
    objeto = imutils.resize(objeto, width=38)#cambia el tamaño de la captura de video


    cv2.imshow('frame', frame)#visuarlizar el video capture
    cv2.imshow('objeto', objeto)#visuealizar el rectangulo del video capture

    k= cv2.waitKey(1)
    if k == 27:
        break

    if k == ord('s'):
        cv2.imwrite(Datos+'/objeto_c_{}.jpg'.format(count),objeto)
        print('Imagen almacenada: ', '/objeto_a_{}.jpg'.format(count))
        count = count + 1


cap.release()
cv2.destroyAllWindows()
