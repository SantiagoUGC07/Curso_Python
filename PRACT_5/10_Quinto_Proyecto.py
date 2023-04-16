#5.- PROYECTO- JUEGO DE AHORCADO
#el programa debe elegir una palabra aleatoria, el usuario solo puede visualizar guiones, el usuario debe elegir una letra
#si se encuentra la letra esta se debe poder visualizar en pantalla, cada vez que elija una letra que no este en la palabra
#perdera una vida.
from random import *
print("EL PROGRAMA PARECE QUE DA DOS OPORTUNIDADES, PERO ES POR QUE IMPRIME EL EJEMPLO DE LAS FUNCIONES")
from random import shuffle
#lista inicial
palabras=['Padre','Carro','Camion','Casa']
vidas=6
letra=''
LCIngresadas=0#contador de letras.
#mezclar palabras
def mezclarPalabras(lista):
    lista=choice(palabras)#choice sirve para mezclar los caracteres
    return lista#devuelve la palabra


#reemplazar letras
def mostrarGuiones(palabra):
    print("INICIA - mostrar")
    palabra=palabra.lower()
    i=0
    guiones=[]
    print(f"la palabra es : {palabra}")
    print(f"la palabra tiene:  {len(palabra)} digitos")
    while i<len(palabra):
        guiones.append('-')
        i+=1
    return guiones,palabra#crea una lista con guiones igual a la cantidad de digitos de la palabra devuelve la palabra
                        #devuelve la palabra en minuscula


#pedirle intento
def ingresarLetra(palabra):
    print("INICIO -  ingresar letra")
    #print(type(palabra))
    intento=''#declarando string
    while intento not in [palabra]:
        intento = input("Introduce una letra: ")
        qEncontro=palabra.find(intento)#si la letra no se encuentra devuelve un -1
        if(qEncontro==-1):
            return qEncontro,intento
        else:
            letra=buscarLetra(qEncontro,palabra)#llama buscar la letra
            print(f"la letra que volvio es {letra}")
            return qEncontro,letra

#Buscar letra
def buscarLetra(qEncontro,palabra):
    i=0
    print(palabra)
    for letra in palabra:
        if qEncontro!=i:
            i += 1
        else:
            return letra#Busca la letra y la separa de la palabra para cambiarla posteriormente.

#vidas
def vidasRestantes(qEncontro,vidas):
    print(type(vidas))
    if(qEncontro==-1 and vidas >=1):
        vidas-=1
    return vidas

#comprobar intento
def revisarIntento(palabra,qEncontro,letra,vidas):
    i=0
    print(f"la letra que se usara para comparar es {letra}")
    print(f"el tipo de la letra es: {type(letra)}")
    print(f"{palabra[qEncontro]}")
    #print(type(palabra[qEncontro]))
    if palabra[qEncontro]==letra:
        print(f"se ENCONTRO la letra {palabra[qEncontro]} muy bien continua")
    else:
        print(f"Has PERDIDO una vida te restan {vidas}")

#agregar letras a guiones
def agregarLetrasGuiones(palabra,qEncontro,letra,guiones,LCIngresadas):
    i=0
    #contador de letras ingresadas
    while i < len(palabra):
        if palabra[i] == letra:
            #print("sus palabra")
            #print(letra)
            #print(palabra[i])
            guiones[i]=letra
            LCIngresadas+=1#Cuenta las letras correctamente ingresadas
        else:
            pass
        i+=1
    print(guiones)
    return LCIngresadas

def palabraCompleta(LCIngresadas,palabra):
    if LCIngresadas == len(palabra):
        print("haz completado la palabra")
        vidas = 0
        return vidas
    else:
        pass

#programa
print("INICIO - PROGRAMA")
print(f"las palabras que se tienen {palabras}")#la palabras
palabra=mezclarPalabras(palabras)
guiones,palabra=mostrarGuiones(palabra)
print(guiones)
while vidas != 0:
    qEncontro,letra = ingresarLetra(palabra)#TE PIDE ELEGIR UN NUMERO AL AZAR
    vidas=vidasRestantes(qEncontro,vidas)
    LCIngresadas=agregarLetrasGuiones(palabra, qEncontro, letra, guiones,LCIngresadas)
    revisarIntento(palabra,qEncontro,letra,vidas)#VERIFICA SI TU NUMERO CONCIDE CON LA POSCICION DEL PALITO MAS PEQUEÑO
    vidas=palabraCompleta(LCIngresadas,palabra)


