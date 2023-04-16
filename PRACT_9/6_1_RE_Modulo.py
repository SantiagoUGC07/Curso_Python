#MODULO RE
'''
RE= regular expresions
sirve para acceder a las expresiones regulares..

UN EJEMPLO si quisieras buscar un correo, se puede usar la siguiente cadena de expresiones
[string] + '@' [string] + '.com'
o para validar si el usuario ingreso una direccion correcta de email

Ejemplos
1.- se tiene la siguiente cadenade caracter para poder detectarla se declara patron de la sig manera
###-###-####
patron = r'\d\d\d-\d\d\d-\d\d\d\d   #se coloca r' para indicar a python que se va a buscar  o detectar toda cadena con esa estructura
#entonces todas las cadenas con la sig estructura las tomara como RE
546-456-4534
232-343-3424
344-244-3243

2.- hay diferentes maneras de expresar lo mismo la sig manera para indicar la cantidad de caracter en cada grupo
patron = r'\d{3}-\d{3}-\d{4}'   #esto es lo mismo que r'\d\d\d-\d\d\d-\d\d\d\d  y nos ayuda a no escribir tanto para identificar RE

CARACTERES ESPECIALES para identificar patrones.

    /d  = digito numerico puede ser cualquier numero de 1-9
    ejemplo de /d si se escribe v\d.\d\d python buscara todas las estructuras con numeros que coincidan con
    v\d.\d\d    v1.02    v1.03   v2.01   v3.02

    /w  = caracter alfanumerico puede ser letra, numero o simbolo
    ejemplo de /w si se escribe \w\w\w-\w\w python buscara todas las esctructucas con letras,numero y simbolo que coincidan con
    \w\w\w-\w\w   sol-do  abc-25  ABC-25   Nro-al

    /s  = espacio en blanco
    ejemplo si se escribe    numero\s\d\d python buscara todas las estructuras iguales que coincidan con
    numero\s\d\d      numero 25   numero 01   numero 99    numero 50

    LO SIGUIENTES patrones son lo contrario a los anteriores
    /D  = NO es un digito.... python buscara las letras que concida con la estrucutra
    \D\D\D\D      abcd

    /W  = NO alfanumerico ....python buscara los caracter especiales que coincidan con la estructura.
    \W\W\W     +=-    ???    !*?    ###

    /S  = NO espacio en blanco .... python buscara los patrones que no tengan espacio en blanco y coincidan con la estructura
    \S\S\S\S      1234   abcd    ¡si?   v.A1

CARACTERES CUANTIFICADORES para identificar patrones donde varian los caracter y no escribir mucho los caracter especiales \d\w\s
    +  =  que el patron varia 1 o mas veces
    ejemplo:    codigo_\d-\d+    codigo_5-5   codigo_5_555   codigo_1-02   codigo_9-95656

    {n}  =  un numero entre corchetes que el caracter se va a repetir n veces
    ejemplo:    \d-\d{4}     1-0000  1-2687   5-6060   8-0001

    {n,m}  =  dos numeros, indica que las repeticiones de los caracter estan entre esos dos numeros
    ejemplo:    \w{3,5}    hola    sol    mundo   yo526

    {n,}   =  un numero con coma entre corchetes indica que las repeticiones del caracter van desde n hasta n-veces
    ejemplo:    -\d{4,}-    -11111-    -5234-    -23244343432-      -233333-      -0000-

    *   =  un numero indeterminado de veces, puede que el caracter no exista dentro del patron o que exista muchas veces
    en el sig patron busca por la cantidad de espacio en blanco, en algunos patrones hay en otros no hay espacios en blanco
    ejemplo:    \w\s*\w      a2       a   b      fm      s4

    ?   =  un caracter exista una vez o ninguna,... un ejemplo cuando se busca una palabra que no se sabe si es singular o plural
    ejemplo:     casas?    casa   casas
'''
import re
texto = "Si necesitas ayuda llama al (658-598-9977 las 24 horas al servicio de ayuda online"
palabra= 'ayuda' in texto #buscar la palabra sin regular expresion
print(palabra)

#1.- RE search : para buscar palabras en un texto
print("\nRE.SEARCH buscar string/elemento")
texto = "Si necesitas ayuda llama al (658-598-9977 las 24 horas al servicio de ayuda online"
patron = 'nada'#palabra a buscar
busqueda = re.search(patron, texto)#se usa el modulo search para buscar en el texto
print(busqueda)#nos devuelve un objeto none dado a que no se encuentra
patron = 'ayuda'
busqueda = re.search(patron,texto)
#Impresion de BUSQUEDA .span()   .start()   .end()
print(busqueda)# se imprime la info del objeto
print(busqueda.span())#la info de la ubicacion inicial y final de la palabra
print(busqueda.start())#la info de la ubicacion inicial
print(busqueda.end())#la info de la ubicacion final de la palabra

#2.- RE.FINDALL econtrar todas las palabras igualas
print("\nRE.FINDALL buscar string/elementos iguales")
busqueda=re.findall(patron,texto)#findall es un tipo lista, sirve para encontrar todas las palabras iguales
print(busqueda)#se imprime una lista con las dos palabras ayuda que se enocntraron
print(len(busqueda))#es un tipo lista por eso se puede usar len PARA LA CANTIDAD DE ELEMENTOS

#3.- RE.FINDITER encontrar la ubicacion de los elementos repetidos en este caso la palabra ayuda
print("\nRE.FINDITER econtrar las ubicaciones de los elementos repetidos")
for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())

#4.- BUSCAR PATRONES CON RE
print("\nRE. BUSCAR PATRONES r'")
texto= "llama al 456-344-2324 ya mismo"
patron = r'\d\d\d-\d\d\d-\d\d\d\d'#r' indica a python que se inicia la busqueda de un patron con la sig estructura
resultado = re.search(patron,texto)
print(resultado)#se muestra toda la ubicacion del patron y su tipo
print(resultado.group())#solo se muestra el patron que coincide con la variable patron
#5.- BUSCAR PATRONES RE usando cuantificadores
print("\nRE. BUSCAR PATRONES r' con cuantificador")
texto= "llama al 456-344-2324 ya mismo"
patron = r'\d{3}-\d{3}-\d{4}'#estructura de patron con cuantificador
resultado = re.search(patron,texto)
print(resultado)#se imprime el patron, su ubicacon y su tipo
print(resultado.group())#se imprime el patron
#5_1.- BUSCAR PATRONES RE usando cuantificadores y  modulo compile para compilar las variables
print("\nRE. BUSCAR PATRONES r' con cuantificador y modulo compile")
texto= "llama al 456-344-2324 ya mismo"
patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})')#estructura de patron con cuantificador y compile
resultado = re.search(patron,texto)
print(resultado)#se imprime el patron, su ubicacon y su tipo
print(resultado.group())#se imprime el patron
print(resultado.group(2))#ahora se puede imprimir solo un valor del patron

#5_2.- BUSCAR PATRONES RE usando cuantificadores y  compilados
print("\nPATRONES r' con cuantificador verificando palabra ingresada")
print("se comento este codigo por eso no se visualizan resultados")
'''
clave = input("clave: ")
patron = r'\D{1}\w{7}'#significa 1 letra y 7alfanumericos algo como: a898adsa
revisar = re.search(patron,clave)#con este patron nos aseguramos que el usuario ingrese las palabra o estructura correctas
print(revisar)
'''

#6.- BUSCAR PATRONES RE usando operadores logicos para buscar
print("\nRE con operadores logicos para BUSCAR en el texto")
texto2 = "No atendemos los lunes por la tarde"
buscar = re.search(r'lunes|martes',texto2)#buscar la palabra lunes o martes   |: significa o
print(buscar)#se imprime la palabra encontrada

#7.- RE comodin buscar partes de la palabra y lo que la antecede o la continua
print("\nRE comodin buscar partes de la palabra")
texto2 = "No atendemos los lunes por la tarde"
buscar = re.search(r'demos',texto2)#buscar partes de la palabra
print(buscar)#se imprime la ubicacion y la parte de la palabra encontrada
buscar = re.search(r'.....demos....',texto2) #los puntos a la izq y derecha incluyen la parte del texto que se encuentra en esa ubicacion de la palabra demos
print(buscar)#se imprime la palabra demos y la misma cantidad de texto que se encuentra a la izq y derecha segun los puntos colocadas

#8.- RE acento ^ para verificar si un patron se encuentra al comienzo del string
print("\nRE ^ buscar un parametro especifico al inicio del texto")
texto3 = "No atendemos los lunes por la tarde"
buscar = re.search(r'^\D',texto3)#^ sirve para buscar el parametro \D al comienzo del texto \D es un NO digito
print(buscar)#se imprime la letra encontrada al inicio del texto

#9.- RE simbolo $ para verificar si un patron se encuentra al final del string
print("\nRE $ buscar un parametro especifico al final del texto")
texto3 = "No atendemos los lunes por la tarde"
buscar = re.search(r'\D$',texto3)#$ sirve para buscar el parametro \D al final del texto \D es un NO digito
print(buscar)

#10.- RE [ ] para excluir un parametro en especifico
print("\nRE [] excluir un parametro especifico")
texto3 = "No atendemos los lunes por la tarde"
#[] para excluir parametros en especifico, en este caso los espacios vacios \s
buscar = re.findall(r'[^\s]',texto3)#esto sigfinica que buscara todo lo que no sea un espacio vacio y lo excluira
print(buscar)
buscar = re.findall(r'[^\s]+',texto3)#con el simbolo + que es buscar una o mas veces, asi agregamos a una lista cada que encuentre un espacio vacio
print(buscar)#se imprime la lista echa con ayuda de los parametros
print(' '.join(buscar))#se crea un string apartir de la lista creada agregando los espacios vacios con el metodo de los strings



