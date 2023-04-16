#DECORADOR
def decorador_funcion(funcion):
    def decorador_value(valor,letra):
        print("Hola!.")
        funcion(valor,letra)
        print("Favor espere su turno")
    return decorador_value
#FUNCIONES GENERADORAS
def Perfumeria():
    i = 0
    while True:
        i += 1
        yield i
def Farmacia():
    i = 0
    while True:
        i += 1
        yield i
def Cosmeticos():
    i = 0
    while True:
        i += 1
        yield i
#FUNCION DECORADA
@decorador_funcion
def turnos(call_tienda,letra):
    tipo=letra
    print(f"Su turno es {tipo}-{next(call_tienda)}")
#MATCH DE TIENDAS
def ir_areas(opci,call_perfu,call_Farm,call_Cosm):
    match opci:
        case 1:
            letra="P"
            turnos(call_perfu,letra)
        case 2:
            letra="F"
            turnos(call_Farm,letra)
        case 3:
            letra="C"
            turnos(call_Cosm,letra)
#ANALICIS DE DATOS
def analizar_numero(opci):
    try:
        ["1","2","3"].index(opci)
    except ValueError:
        print("tu respuesta no coincide con las opciones")
    else:
        print("se esta procesando su solicitud")



