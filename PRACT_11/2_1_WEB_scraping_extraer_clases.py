#WEB SCRAPING extraer clases, id, etiquetas
'''
TABLA DE CARACTERES
  CARACTER        SINTAXIS                        RESULTADOS
     "         soup.select('div')                Todos los elementos con la etiqueta 'div'
     #         soup.select('#estilo_4')          Elementos que contengan id='estilo4'
     .         soup.select('.columna_der')       Elementos que contengan    class='columna der'
 (ESPACIO)     soup.select('div span')           Cualquier elemento llamado 'span' dentro de un elemento 'div'
     >         soup.select('div>span')           Cualquier elemento llamado 'span' directamente dentro de un elemento
                                                 'div' sin nada en el medio o bien para hallar etiquetas dentro de otras, sin nada en el medio
se muestran los caracteres y codigos que se pueden usar para obtener distintas etiquetas. o capturar datos de algun sitio web
'''
import bs4
import requests
import lxml

#1.-EXTRAER UNA CLASE COMPLETA y mostrar todo el contenido
'''
resultado = requests.get("https://escueladirecta-blog.blogspot.com/")
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')# lxml es un objeto tipo bs4, que nos permite navegar entre sus componentes,elementos o etiquetas
parrafor_especial= sopa.select(".post-title")# de esta manera se llama a la clase post-title  y las etiquetas a que contiene
print(parrafor_especial)
'''
#2.-EXTRAER E IMPRIMIR TODAS LAS ETIQUETAS a DE UNA CLASE
'''
resultado = requests.get("https://escueladirecta-blog.blogspot.com/")
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')# lxml es un objeto tipo bs4, que nos permite navegar entre sus componentes,elementos o etiquetas
parrafor_especial= sopa.select(".post-title a")# de esta manera se llama a la clase post-title  y las etiquetas a que contiene
print(parrafor_especial)
'''
#3.-EXTRAER E IMPRIMIR UNA ETIQUETA a DE UNA CLASE
'''
resultado = requests.get("https://escueladirecta-blog.blogspot.com/")
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')# lxml es un objeto tipo bs4, que nos permite navegar entre sus componentes,elementos o etiquetas
parrafor_especial= sopa.select(".post-title a")[0]# de esta manera se llama a la clase post-title  y la etiqueta a en la primera poscicion por [0] 
print(parrafor_especial)
'''
#3.-EXTRAER LA ETIQUETA DE UNA CLASE e imprimir solo el texto sin la etiqueta
resultado = requests.get("https://escueladirecta-blog.blogspot.com/")#llamamos a la pagina
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')# lxml es un objeto tipo bs4, que nos permite navegar entre sus componentes,elementos o etiquetas
parrafor_especial= sopa.select(".post-title a")# de esta manera se llama a la clase post-title  y las etiquetas a que contiene
for a in parrafor_especial:#para imprimir todas las etiquetas a e ocupa un loop
    # print(a)#para imprimir todas las etiqueta a
    print(a.getText())#para imprimir solo el texto de las etiquetas a
