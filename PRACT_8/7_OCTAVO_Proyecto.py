from OCTAVO_Proyecto_Modulos import *
#MENU DE OPCIONES
call_perfu = Perfumeria()
call_Farm = Farmacia()
call_Cosm = Cosmeticos()
def analizar_respuesta():
    while True:
        menu_area()
        try:
            otro_turno = input("Quieres sacar otro turno Y/N?: ").lower()
            ["y","n"].index(otro_turno)
        except TypeError:
            print("La respuesta no coincide con Y/N, favor de ingresar otra.")
        except ValueError:
            print("La letra ingresada no coincide debe ser Y/N")
        else:
            if otro_turno == "n":
                print("Gracias por su visita")
                break

def opciones_menu():
    print("1.-Perfumeria")
    print("2.-Farmacia")
    print("3.-Cosmeticos")
    opci = input("ingresa tu opcion: ")
    return opci

def menu_area():
    continuar = True
    opci = opciones_menu()
    opci_resp=analizar_numero(opci)
    opci = int(opci)
    ir_areas(opci,call_perfu,call_Farm,call_Cosm)
analizar_respuesta()




