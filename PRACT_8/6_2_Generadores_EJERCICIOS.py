#1.-EJERCICIO
'''
Crea un generador (almacenado en la variable generador) que sea capaz de devolver una secuencia infinita de números,
iniciando desde el 1, y entregando un número consecutivo superior cada vez que sea llamada mediante next
'''
print(f"\n1.-EJERCICIO")
def funcion_generadora():
    num = 0#no importa que se declare  se queda apartir del ultimo numero enviado
    while True:
        num+=1
        yield num
call_FG=funcion_generadora()
print(next(call_FG))
print(next(call_FG))
print(next(call_FG))
print(next(call_FG))

#2.-EJERCICIO
'''
Crea un generador (almacenado en la variable generador) que sea capaz de devolver de manera indefinida múltiplos de 7, 
iniciando desde el mismo 7, y que cada vez que sea llamado devuelva el siguiente múltiplo (7, 14, 21, 28...).
'''
print(f"\n2.-EJERCICIO")
def Fgenerador():
    i=1
    while True:
        num = 7 #si inicializa una variable dentro del ciclo si se restablece su valor
        num*=i
        i+=1
        yield num
generador = Fgenerador()
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))

#3.-EJERCICIO
'''
Crea un generador que reste una a una las vidas de un personaje de videojuego, 
y devuelva un mensaje cada vez que sea llamado:
    "Te quedan 3 vidas"
    
    "Te quedan 2 vidas"
    
    "Te queda 1 vida"
    
    "Game Over"
Almacena el generador en la variable perder_vida
'''
print(f"\n3.-EJERCICIO")

def Fgenerador_vidas():
    vidas=4
    while True:
        if vidas > 1:
            vidas-=1
            yield f"Te quedan {vidas} vidas"
        else:
            yield "Game Over"

generador=Fgenerador_vidas()
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
