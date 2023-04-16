import cv2



#ruta= Path("C:\Users\uri\Desktop\Curso_Python\Pruebas\2_implementacion de modelo\cascade.xml")

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)#activar la camara web

CervezaVicClassif = cv2.CascadeClassifier('cascade.xml')#se toma el modelo preentrenado

while True:
    ret,frame = cap.read()#se le la imagen
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#se pasa a escala de grises la imagen

    Producto = CervezaVicClassif.detectMultiScale(gray,#se manda el modelo en escala de grises
                                           scaleFactor = 7,#los valores para comparar con la imagen estos se puede aumentar
                                           minNeighbors = 91,
                                           minSize=(70,78))

    for(x,y,w,h) in Producto:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame,'Cerveza victoria',(x,y+10),2,0.7,(0,255,0),2,cv2.LINE_AA)

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()