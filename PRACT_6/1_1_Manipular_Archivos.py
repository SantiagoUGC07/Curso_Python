#Manipular documentos, abrir archivos y alojarlos en variables.
'''
abrir       open()
leer        read()
escribir    write()
cerrar      close()
'''
#1.-EJEMPLO
print("--EJEMPLO - 1")
mi_archivo = open('prueba.txt')#se abre el archivo
print(mi_archivo.read())#una vez que se lee el archivo ya se puede imprimir.
mi_archivo.close()#cerrar el archivo, y resguardar el espacio de memoria.

#2.-EJEMPLO
#volvemos abrir el archivo
print("\n--EJEMPLO - 2")
mi_archivo = open('prueba.txt')#se abre el archivo
una_linea = mi_archivo.readline()#imprime la primera linea del txt
print(una_linea)

una_linea = mi_archivo.readline()#al colocarse de nuevo se imprime la segunda linea del txt, con un salto de linea
print(una_linea.rstrip())#sirve para que queden seguidas las impresiones y quita el salto de linea

una_linea = mi_archivo.readline()#Imprime la tercera linea dado a que se ingreso despues.
print(una_linea.upper())#se pueden aplicar los metodos de strings, para hacer mayusculas en este caso
mi_archivo.close()#cerramos archivo para nuevo ejemplo

#3.-EJEMPLO
#SE PUEDE ITERAR DENTRO DE LAS LINEAS DE UN TEXTO
print("\n--EJEMPLO - 3")
mi_archivo=open('prueba.txt')#se abre el archivo
for l in mi_archivo:
    print("Aqui dice " + l)#De esta manera podriamos manipular las lineas
mi_archivo.close()#cerramos archivo para nuevo ejemplo

#4.-EJEMPLO
#SE IMPRIME ARCHIVO EN FORMA DE LISTA, SOLO SIRVE PARA ARCHIVOS PEQUEÑOS
print("\n--EJEMPLO - 4")
mi_archivo=open('prueba.txt')#se abre el archivo
todas=mi_archivo.readlines()#se adjutan en una lista
print(todas)#se imprime en forma de lista
#5.-EJEMPLO
print("\n--EJEMPLO - 5")
todas = todas.pop()#para excluir la ultima linea de la lista
print(todas)#se imprime solo la tercera linea