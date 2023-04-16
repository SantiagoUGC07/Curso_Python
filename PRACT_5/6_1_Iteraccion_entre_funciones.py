#ITERACCION ENTRE FUNCIONES
#programas el juego de los palitos mas largo y corto
#EL PROGRAMA PARECE QUE DA DOS OPORTUNIDADES, PERO ES POR QUE IMPRIME EL EJEMPLO DE LAS FUNCIONES
print("EL PROGRAMA PARECE QUE DA DOS OPORTUNIDADES, PERO ES POR QUE IMPRIME EL EJEMPLO DE LAS FUNCIONES")
from random import shuffle
#lista inicial
palitos=['-','--','---','----']

#mezclar palitos
def mezclar(lista):
    shuffle(palitos)#shuffle sirve para mezclar los caracteres
    return lista#
print(mezclar(palitos))#se imprime la lista los palitos mezclados

#pedirle intento
def probar_suerte():
    intento=''
    while intento not in ['1','2','3','4']:
        intento = input("Elije un numero del 1 al 4: ")
    return int(intento)#ELIGES UN NUMERO EL CUAL PUEDE SER EL PALITO MAS PEQUEÑO
intento1 =probar_suerte()
print(intento1)

#comprobar intento
def chequear_intento(lista,intento):
    if lista[intento - 1] == '-':#BUSCA EN QUE POSCICION SE ENCUENTRA EL - O MAS BIEN EL PALITO MAS PEQUEÑO
        print("A lavar los platos")#SI EL NUMERO QUE ELEGISTE CONCIDE CON LA POSCICON DEL PALITO MAS PEQUEÑO PIERDES
    else:
        print("Esta vez te has salvado")#SI EL NUMERO QUE ELEGISTE NO CONCIDE TE SALVAS
    print(f"Te ha tocado {lista[intento-1]}")

#programa
print("inicio del programa en realidad")
palitos_mezclados= mezclar(palitos)#MEZCLA LOS PALITOS
print(palitos_mezclados)
seleccion = probar_suerte()#TE PIDE ELEGIR UN NUMERO AL AZAR
chequear_intento(palitos_mezclados,seleccion)#VERIFICA SI TU NUMERO CONCIDE CON LA POSCICION DEL PALITO MAS PEQUEÑO

