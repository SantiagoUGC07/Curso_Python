#Troscrape.com
'''
es una pagina libre para practicar WEB SCRAPING ya que todo es libre de autor
'''
#OBJETIVO DE LA PRACTICA: NAVEGAR EN DISTINTAS PAGINAS PARA OBTENER LOS DATOS
import bs4
import requests
import lxml

#1.-NAVEGAR POR LAS PAGINAS DEL SITIO
#"http://books.toscrape.com/catalogue/page-2.html" #este es el url original
'''
url_base="http://books.toscrape.com/catalogue/page-{}.html"#se cambia el numero por las {} para navegar por las paginas de este sitio
for n in range (1,11):#recorrer 10 paginas
    print(url_base.format(n))#format nos srive para cambiar el valor n por los llaves{} en el url_base
'''
#2.-EXTRAER TODOS LOS PRODUCTOS CON SU CALIFICACION DE LA PAGINA 1 DEL SITIO
'''
url_base="http://books.toscrape.com/catalogue/page-{}.html"
resultado = requests.get(url_base.format('1'))#.format para cambiar las llaves {} del url_base por el 1 que representa la pagina del sitio
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
print(sopa.select(".product_pod"))#se imprimen todas las clases .product_pod, que son todos los productos
'''

#3.-EXTRAER LA CLASE CON LA CALIFICACION DEL PRODUCTO LIBRO
'''
url_base="http://books.toscrape.com/catalogue/page-{}.html"
resultado = requests.get(url_base.format('1'))#.format para cambiar las llaves {} del url_base por el 1 que representa la pagina del sitio
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
libros = sopa.select(".product_pod")#se Importan en la variable libros todas las clases .product_pod, que son todos los productos
#ejemplo = libros[0] #si esto se manda a imprimir, se imprime toda la info de la primera clase product_pod que es el primer producto
#en este caso se obtiene la calificacion del producto que se encuentra junto a la clase "star-rating Three" la calificacion es Three

#el nombre de la clase es "star-rating Three" pero existe un espacio en blanco asi que se coloca un punto entre rating y one el punto al inicio es por que es una clase
ejemplo = libros[0].select(".star-rating.Three")# el Three de la clase "star-rating Three" representa la cantidad de estrellas que tiene de calificacion el producto
                                              #libros[0] se refiere a la primera clase .product_pod que representa el primer producto
                                              #nota:cuando la calificacion de estrellas no corresponde con la que tiene el libro se regresa un [] o cero 0
                                              #     en este caso el libro si tiene Three de calificiacion por lo que regresa los elementos dentro de la clase
print(ejemplo)#se imprime el contenido de la clase "star-rating Three" del primer producto libros[0]=.product_pod"
'''

#4.-EXTRAER E IMPRIMIR EL TITULO DEL LIBRO producto
'''
url_base="http://books.toscrape.com/catalogue/page-{}.html"
resultado = requests.get(url_base.format('1'))#.format para cambiar las llaves {} del url_base por el 1 que representa la pagina del sitio
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
libros = sopa.select(".product_pod")#se Importan en la variable libros todas las clases .product_pod, que son todos los productos
#ejemplo = libros[0] #si esto se manda a imprimir, se imprime toda la info de la primera clase product_pod que es el primer producto
#se analiza la info del producto y en este caso la informacion del TITULO DEL LIBRO se encuentra en la etiqueta <a>

ejemplo = libros[0].select("a")#se imprime la info de la etiqueta a para visualizar el TITULO
ejemplo = libros[0].select("a")[1]['title']# [1] indica la segunda etiqueta a que es donde esta el title
print(ejemplo)#se imprime la segunda etiqueta a que es donde esta el TITULO
#se imprimio el titulo
'''

#5.-EXTRAER E IMPRIMIR TITULOS DE LIBROS CON 4 O 5 ESTRELLAS
url_base="http://books.toscrape.com/catalogue/page-{}.html"
#lista de titutlos con 4 o 5 estrellas
titulos_rating_alto = []
#iterar paginas
for pagina in range(1, 15):
    #crear sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
    #seleccionar datos de los libros
    libros = sopa.select('.product_pod')
    #iterar libros
    for libro in libros:
        #revisar que tengan 4 o 5 estrellas los libros
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:#se pone distinto a cero por que cuanto no tiene elementos regresa un cero
            #guardar titulo en variable si tiene 4 o 5 estrellas
            titulo_libro = libro.select('a')[1]['title']
            #agregar libro a la lista
            titulos_rating_alto.append(titulo_libro)
#IMPRIMIR LOS TITULOS DE LOS LIBROS CON 4 O 5 ESTRELLAS EN CONSOLA
for t in titulos_rating_alto:#Se itera en la lista que se creo de los libros con 4 o 5 estrellas
    print(t)