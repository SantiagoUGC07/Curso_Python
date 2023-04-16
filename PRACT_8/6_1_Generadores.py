#Generadores
'''
son un tipo de funciones que envez de devolvernos un valor terminado, nos lo devuelve poco a poco
un ejemplo no produce una lista del 1 al 100 de golpe los va generando poco a poco, para no gastar mucho espacio de memoria
solo generara el numero una vez que se pida. se va acordando donde se quedo.
de esta manera se reserva memoria con las funciones generadoras
estructura de funcion generadora

def mi_funcion()
    yield algo

*yield en ingles significa producir, de esta manera le decimos que vaya produciendo
'''

#1.-EJEMPLO imprimiendo un generador con un solo numero
'''
def mi_funcion():#funcion normal
    return 4

def mi_generador():#funcion generadora
    yield 4
#DIFERENCIAS ENTRE FUNCIONES
print(mi_funcion())
print(mi_generador())#no se imprime, solo comenta que se tiene la clase
#para imprimirlo se necesita asignar a una variable la funcion generadora
g = mi_generador()
print(next(g))#con next se puede acceder a la funcion generadora
'''

#2.-EJEMPLO imprimiendo lista con generador
'''
def mi_funcion():#funcion normal
    lista = []
    for x in range (1,5):
        lista.append(x * 10)
    return lista

def mi_generador():#funcion generadora
    for x in range(1,5):
        yield x * 10

print(mi_funcion())
print(mi_generador())
g = mi_generador()

print(next(g))#llamando al generador
print(next(g))#va generando un numero a medida que se lo pidas
print(next(g))#apartir del punto en el que se queda, asi no almacena mucha info como una funcion normal
'''

#3.-EJEMPLO imprimiendo lista con generador
def mi_generador():#funcion generadora
    x = 1
    yield x#llega hasta aqui

    x += 1
    yield x

    x += 1
    yield x

g = mi_generador()
print(next(g))#la primera vez que llama a la funcion generadora solo llega al primer yield
print(next(g))
print("hola mundo")# aqui pueden aver funciones o otras cosas y cuando vuelvas a llamar a la funcion generadora
print(next(g))     # va a continuar donde se quedo.
