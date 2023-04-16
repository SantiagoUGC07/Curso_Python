#ARGUMENTOS INDEFINIDOS
#COMO CONOCER UNA CANTIDAD DE ARGUMENTOS INDEFINIDOS
#*args sirve para adaptarse al numero de argumentos que el usuario quiera pasar
#*args=significa argumento igual se puede cambiar el nombre por *gato pero es mejor usar *args
#despues se vera la funcion de **kwargs = significa keyboard args
#UTILIZANDO *args
#1.-EJEMPLO
def suma(a,b):
    return a+b
print (suma(5,6)) #esto se puede crear dado a que la funcion acepta dos variables
#para hacer que la funcion pueda aceptar mas de un parametro se usa *args
def suma2(*args):
    total=0
    for arg in args:
        total +=arg
    return total
print(suma2(5,6,4))#dado a que se tiene args en la funcion se pueden enviar n cantidad de parametros
#UNA FORMA MAS SECILLA DE REALIZAR EL CODIGO
def suma3(*args):
    return sum(args)
print(suma3(5,4,6,6,7,87,8,76))#se puede realizar el proceso debido a que se usa *args

#OTRA FORMA DE USAR *args es sustituyendolo por otra paralabra con un asterisco
def suma4(*gato):#se muestra como se cambia *args por *gato pero es mejor usar args
    return sum(gato)
print(suma4(3,3,2,43,45,4,5))
