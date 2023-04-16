
class Persona:
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido
    pass
class Cliente(Persona):
    def __init__(self,nombre,apellido,numero_cuenta,balance):
        super().__init__(nombre,apellido)
        self.numero_cuenta=numero_cuenta
        self.balance=balance
    def retirar(self,retiro):
        if retiro <=self.balance:
            self.balance -= retiro
            return f"su retiro fue de {retiro}"
        elif retiro>=self.balance:
            return f"CAPITAL INSUFICIENTE"
    def depositar(self,deposito):
        self.balance+=deposito
        return f"su deposito fue de {deposito}"
    def __str__(self):
        return f"hola {self.nombre} {self.apellido} Su capital es de: {self.balance}"

def crear_cliente():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    cliente=Cliente(nombre,apellido,0,0)
    inicio(cliente)
def inicio(cliente):
    opci='y'
    while(opci!='n'):
        opci = (input("\nQUE DESEA CONSULTAR? \n\"1.-cuenta\" \n\"2.-retirar\" \n\"3.-depositar\" \n\"4.-salir\"\nelige el numero de la opcion?: ")).lower()
        if(opci == '1'):
            print(cliente)#se va al metodo str
        elif(opci == '2'):
            retiro = int(input("cuanto desea retirar: "))
            print(cliente.retirar(retiro))
        elif (opci=='3'):
            deposito = int(input("cuanto desea depositar: "))
            print(cliente.depositar(deposito))
        elif(opci=='4'):
            opci='n'
#***MAIN***
crear_cliente()


