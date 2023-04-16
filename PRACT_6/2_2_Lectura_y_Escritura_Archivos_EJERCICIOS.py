#1.-EJERCICIO
#Abre el archivo llamado "mi_archivo.txt", y cambia su contenido por el texto "Nuevo texto".
#Imprime el contenido  de "mi_archivo.txt" al finalizar.

print("1.-EJERCICIO")
miArchivo = open('prueba_ejercicios.txt','w')#se abre en modo escritura
miArchivo.write('Nuevo texto')#se escribe en el archivo
miArchivo.close()
miArchivo = open('prueba_ejercicios.txt','r')#se cambia a modo lectura
print(miArchivo.read())#se lee el archivo
miArchivo.close()

#2.-EJERCICIO
#Abre el archivo llamado "mi_archivo.txt", y añade una línea al final del mismo que diga: "Nuevo inicio de sesión".
#Imprime el contenido completo de "mi_archivo.txt" al finalizar.
print("2.-EJERCICIO")
miArchivo = open('prueba_ejercicios.txt','a')#se abre en modo escritura consecutiva
miArchivo.write('Nuevo inicio de sesiòn')#se escribe en el archivo
miArchivo.close()
miArchivo = open('prueba_ejercicios.txt','r')#se cambia a modo lectura
print(miArchivo.read())#se lee el archivo
miArchivo.close()

#3.-EJERCICIO
#Utiliza el método writelines para escribir los valores de la siguiente lista al final del archivo "registro.txt" . Inserta un tabulador entre cada elemento de la lista para separarlos.
#registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
#Imprime el contenido completo de "registro.txt" al finalizar.
print("3.-EJERCICIO")
miArchivo=open('prueba_ejercicios.txt','a')
miLista=["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
for palabra in miLista:
    miArchivo.writelines(palabra + '\n')
miArchivo.close()
miArchivo=open('prueba_ejercicios.txt','r')
print(miArchivo.read())
miArchivo.close()


