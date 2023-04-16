#WEB SCRAPING
'''
el web scraping en españól significa raspando el internet
esto sirve para obtener info, imagenes, sonido de un sitio web.
para esta practica se requiere instalar
    pip install lxml
    pip install bs4
    pip install requests
NOTA: para la libreria lxml, importarla en el doc y luego click secundario sobre la misma, e installar libreria
'''
#Para realizar web scraping usaremos las sig librerias.
import bs4 #beautifulsoup nos sirve para navegar en el texto
import requests #nos permite hacer solicitudes a paginas web
import lxml

#1.-solicitar info a URL en ESPECIFICO_____Requests
resultado = requests.get("https://escueladirecta.com/p/analisis-de-datos-con-pandas-y-python")
#print(type(resultado))#es el tipo response. pero este no permite navegar entre los elementos
#print(resultado.text)#es el texto que hay en el codigo fuente de la pagina

#2.-USANDO BS4 PARA NAVEGAR
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')#es un objeto tipo sopa, que nos permite navegar entre sus componentes,elementos o etiquetas
#print(sopa) #se muestra todo el codigo fuente de la pagina
print("SE IMPRIMEN EJEMPLOS CON TITLE")
print(sopa.select('title'))#SE IMPRIME TODO EL ELEMENTO CON LA ETIQUETA TITLE
print(sopa.select('title')[0])#SE IMPRIME el elemento sin las corcheas
print(sopa.select('title')[0].getText())#SE IMPRIME solo el texto de la etiqueta TITLE

#3.-VISUALIZAR ELEMENTOS DE LA PAGINA
print("\nCANTIDAD DE ELEMENTOS EN ETIQUETA P y los elementos")
#print(sopa.select('p'))#SE IMPRIMEN TODOS LOS ELEMENTOS DE LA ETIQUETA P
print(len(sopa.select('p')))#SE IMPRIME la cantidad de los elementos con etiqueta P
print("\nSE IMPRIMEN LOS ELEMENTOS EN ETIQUETA H1")
print(sopa.select('h1'))#SE IMPRIMEN TODOS los elementos con la etiqueta h1

#4.-IMPRIMIR SOLO UN ELEMENTO DE LA ETIQUETA
print("\nSE IMPRIMEN EL ELEMENTO 3 DE LA ETIQUETA P")
parrafor_especial= sopa.select('p')[3].getText()
print(parrafor_especial)




