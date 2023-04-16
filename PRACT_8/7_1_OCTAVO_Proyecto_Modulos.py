'''
def decorador_funcion(funcion):
    def decorador_value(valor):
        print("Hola su turno es.")
        funcion(valor)
        print("Favor espere su turno")
    return decorador_value
'''

#@decorador_funcion
def Perfumeria():
    i=0
    while True:
        i += 1
        yield f"tu turno es el P-{i}"

def ir_areas(opci):
    match opci:
        case 1:
            print(Perfumeria())

def analizar_numero(opci):
    try:
        opci=int(opci)
    except ValueError:
        print("Los datos ingresados deben ser numeros")
    else:
        ir_areas(opci)


def menu_area():
    print("1.-Perfumeria")
    print("2.-Farmacia")
    print("3.-Cosmeticos")
    opci= input("ingresa tu opcion: ")
    analizar_numero(opci)

menu_area()



