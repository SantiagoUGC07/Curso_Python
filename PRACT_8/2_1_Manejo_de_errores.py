#MANEJO DE ERRORES
'''
El manejo de errores, nos ayuda a pre-establecer como se deberia comportar el programa al presentarse un error
con el manejo de errores, podemos hacer que el codigo siga ejecutandose, aun que se presente un error.
para esto se ocupa la sig. estructura con los sig. comandos

try      sirve para decirle a python que intente ejecutar un codigo para ver si fluye sin problema o si se sigue presentando el error

except   sirve para evitar que salgan los errores en rojo y continue con el resto del codigo

finaly   sirve cuando no importa si existe un error o no, que se ejecute el siguiente codigo
'''

#1.-EJEMPLO
'''
def suma():
    n1 = int(input("numero 1: "))
    n2 = int(input("numero 2: "))
    print(n1 + n2)
    print("Gracias por sumar")
suma()
'''

'''
#manejo de errores
#primero se usa
try:
    #codigo que queremos probar
    suma()
except:
    #codigo a ejecutar si hay un error
    print("Algo no ha salido bien")
else:#este es un adicional a la estructura de manejo de errores
    #codigo a ejecutar si no hay un error
    print("Hiciste todo bien")
finally:
    print("Eso fue todo, END")
    #codigo que se va a ejecutar de todos modos
'''

#2.-EJEMPLO
'''
def suma():
    n1 = int(input("numero 1: "))
    n2 = int(input("numero 2: "))
    print(n1 + n2)
    print("Gracias por sumar" +n1)#ESTE ERROR DE QUERER SUMAR DOS DISTINTOS

try:
    suma()
except TypeError:#PARA EVITAR EL ERROR DEL TYPE ERROR DE LA LINEA 47 concatenar tipos distintos
    print("Estas intentando concatener tipos distintos")
except ValueError:#PARA EVITAR EL ERROR DE INGRESO DE UNA LETRA PARA SUMA DE ENTEROS
    print("Ese no es un numero")
else:#SI SE HIZO TODO BIEN Y SE EVITARON LOS EXCEPT
    print("Hiciste todo bien")
finally:
    print("Eso fue todo")
'''


#3.-EJEMPLO
def pedir_numero():#funcion para evitar errores de ingreso de un numero
    while True:
        try:
            numero = int(input("Dame un numero: "))
        except:
            print("Ese no es un numero")
        else:
            print(f"Ingresaste el numero {numero}")
            break#si todo sale bien salir y no sale un error
    print("Gracias")
pedir_numero()
