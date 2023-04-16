#DECORADORES
'''
podemos crear nuestros propios decoradores
los decoradores son funciones que modifican el comportamiento de otras funciones como @staticmethod @classmethod
Y ayudan a acortar el codigo
'''

#CONCEPTOS PARA ENTENDER DECORADORES
#Llamar a una funcion atravez de una variable
'''
def mayuscula(texto):
    print(texto.upper())

def minuscula(texto):
    print(texto.lower())
mi_funcion = mayuscula
mi_funcion('python')
'''
#Una funcion como argumento en otra funcion para Ejecutarla.
'''
def mayuscula(texto):
    print(texto.upper())
def minuscula(texto):
    print(texto.lower())
def una_funcion(funcion):
    return funcion
una_funcion(mayuscula('probando'))
'''

#definidir funciones dentro de otras funciones (buscador de mayusculas y minusculas)
'''
def cambiar_letas(tipo):
    def mayuscula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())

    if tipo=="may":
        return mayuscula
    elif tipo == "min":
        return minuscula
operacion = cambiar_letas('may')#llama a cambiar letras verifica la funcion a usar, como es igual a Mayuscula
#operacion = Mayuscula y al tomar el nombre de mayuscula ahora llama a la funcion mayuscula.
operacion('palabra')#el proceso al estar dentro de la funcion cambiar letras por eso puede llamar a mayuscula
'''



#DECORAR (envolver una funcion dentro de otra gracias a este decorador)
def decorar_saludo(funcion):#funcion toma el valor de mayuscula
    def otra_funcion(palabra):#palabra toma el valor que tiene mayuscula en los ("") que es texto
        print('hola')
        funcion(palabra)
        print('adios')
    return otra_funcion
#1.-METODO LLAMAR DECORADOR no olvides el return
'''
@decorar_saludo
def mayuscula(texto):#gracias al decorador podemos envolver la funcion e imprimir
    print(texto.upper())#se imprime entre los textos hola y adios ya que la funcion se envuelve y queda enmedio
@decorar_saludo
def minuscula(texto):
    print(texto.lower())
mayuscula("Python")
'''
#2.-METODO LLAMAR DECORADOR si conlocar los decoradores @ pero igual se ocupa el return
def mayuscula(texto):
    print(texto.upper())

def minuscula(texto):
    print(texto.lower())
mayuscula_decorada = decorar_saludo(mayuscula)#se llama funcion decorar_saludo para envolver a la funcion mayuscula
mayuscula_decorada('feDe')


#*************************************
#3.-EJEMPLO DE DECORADOR CON RETURN
def my_decorator_name(name):
    def my_custome_decorator(function):
        def wrapper(*args, **kwargs):
            print('Name:', name)
            return function(*args, **kwargs)

        return wrapper

    return my_custome_decorator

@my_decorator_name('CodigoFácilito')
def suma(a, b):
    return a + b
print(suma(1,2))


