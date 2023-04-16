from random import choice
palabras=['Padre','Carro','Camion','Casa']
letras_correctas = []
letras_incorrectas= []
intentos=6
aciertos=0
juego_terminado =False

def eligir_palabra(lista_palabras):
    palabra_elegida=choice(lista_palabras)#elige una palabra aleatoria
    letras_unicas=len(set(palabra_elegida))#coloca la palabra en un set para solo tener letras unicas

    return palabra_elegida, letras_unicas#devuelve la palabra y las letras unicas


def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnopqrstvwxyz'

    while not es_valida:#para evitar que se introduzca un numero
        letra_elegida = input("Elige una letra: ").lower()#convierte las letras a minuscula
        if letra_elegida in abecedario and len(letra_elegida)==1:#evitar que se introduzca mas de una letra
            es_valida = True#si no es un numero y no es mas de una letra
        else:
            print("No has eledigo una letra correcta")#si es un numero y es mas de una letra
    return letra_elegida


def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta = []
    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)#agregar las letras correctas a la lista oculta
        else:
            lista_oculta.append('-')#si no esta agregar un guion se repite para la longitud de la palabra
    print(" ".join(lista_oculta))#cambiar lista a string


def checar_letra(letra_elegida, palabra_oculta, vidas, coincidencias):
    fin = False
    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)#para agregar solo una vez la letra a las palabras correctas
        coincidencias += 1
    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print("Ya has encontrado esa letra intenta con otra diferente")#evitar que siga ingresando la misma letra
    else:
        letras_incorrectas.append(letra_elegida)#agregar las letras incorrectas
        vidas -= 1#disminuir una vida
    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)

    return vidas,fin, coincidencias


def perder():
    print("Te has quedado sin vidas")
    print("La palabra oculta era " + palabra)

    return True


def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print("Felicitaciones, has encontrado la palabra")
    return True



palabra, letras_unicas = eligir_palabra(palabras)
while not juego_terminado:
    print("\n" + "*" * 20 + "\n")
    mostrar_nuevo_tablero(palabra)
    print("\n")
    print("letras incorrectas: " + "-".join(letras_incorrectas))
    print(f"vidas: {intentos}")
    letra = pedir_letra()
    intentos, terminado, aciertos = checar_letra(letra, palabra, intentos, aciertos)
    juego_terminado = terminado