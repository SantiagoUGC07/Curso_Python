#Existen distitos modos de escritura y lectura de un archivo.
#modos de apertura
'''
mi_archivo = open ("archivo.txt","r") #modo solo lectura aun que no se coloque la r python lo toma asi
mi_archivo = open ("archivo.txt","w") #modo de solo escritura, si existe el archivo se resetea desde cero y si no existe se crea
mi_archivo = open ("archivo.txt","a") #modo escritura, si existe el archivo no se borra el contenido anterior y si no existe se crea
'''
#1.-EJEMPLO
'''
print("1.-EJEMPLO")
archivo = open('prueba.txt', 'r')#modo lectura "r"
archivo.write('soy el nuevo texto')#no se puede escribir por que se abri como modo lectura
archivo.close()
'''
#2.-EJEMPLO
'''
print("2.-EJEMPLO")
archivo=open('prueba.txt','w')
archivo.write("soy el nuevo texto")
archivo.close()
'''
#3.-EJEMPLO
print("3.-EJEMPLO")
archivo=open('prueba.txt','a')
archivo.write('''hola
soy
yo''')#metodo para incorporar el salto de linea
archivo.close()

#4.-EJEMPLO
print("4.-EJEMPLO")
archivo=open('prueba.txt','a')
archivo.writelines(['hola','mundo','aqui'])#escribe en el archivostring detras del otro sin espacio
archivo.close()

#5.-EJEMPLO
print("5.-EJEMPLO")
archivo=open('prueba.txt','a')
lista=['hola','mundo','aqui']
for p in lista:
    archivo.writelines(p+'\n')#integra palabras con salto de linea en el archivo
archivo.close()