#WEB SCRAPING EXTRAER IMAGENES
'''

'''
import bs4
import requests
import lxml

resultado = requests.get("https://escueladirecta.com/")
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

#1.-EJEMPLO MOSTRAR ETIQUETAS IMG CON CONTENIDO
#imagenes = sopa.select('img')#img es la etiqueta de la imagen. primero se revisaron las etiquetas img en esa pagina
#print(imagenes)

#2.-EJEMPLO MOSTRAR ETIQUETAS IMG ORDENADAS
#imagenes = sopa.select('.course-box-image')#se filtran las imagenes con la clase course box image
#for i in imagenes:#se imprimen de manera ordenanda las etiquetas img
    #print(i)

#3.-EJEMPLO #OBETENER URL Y DESCARGAR IMAGEN
imagenes = sopa.select('.course-box-image')[0]['src']# [0]se filtra el primero elemento de la etiqueta img,[src] se obtiene el URL solamente de las etiquetas img
print(imagenes)#se imprime el URL DE LA IMAGEN
imagen_curso_1 = requests.get(imagenes)#para hacer la solicitud al URL. de la imagen deseada
#print(imagen_curso_1.content) # se imprime el codigo en binario de la imagen con el url de imagen curso 1
#---- CARGAR LA IMAGEN EN UN ARCHIVO----
f = open('mi_imagen.jpg', 'wb')#se coloca un nombre de archivo (mi_imagen.jpg) y se coloca 'wb' para escribir en binario
#colocar la extension del archivo .jpg o el que se desea.
f.write(imagen_curso_1.content)#para eescribir el codigo binario de la imagen en el archivo mi_imagen
f.close()#siempre cerrar el archivo

#NOTA
'''
SI SE QUIERE GUARDAR LA IMAGEN EN UNA RUTA LA RUTA SE COLOCA ANTES DEL NOMBRE DE L IMAGEN
f = open(c://   , 'mi_imagen.jpg', 'wb')
'''





