#1.-EJERCICIO
'''
Crea un método estático respirar() para la clase Mascota. Cuando se llame, debe imprimir en pantalla "Inhalar... Exhalar"
'''
class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")
Mascota.respirar()#no se necesita crear una instancio u objeto

#2.-EJERCICIO
'''
Crea un método de clase revivir() que actúa sobre el atributo de clase vivo de la clase Jugador, estableciéndolo en 
True cada vez que es invocado. El valor predeterminado del atributo vivo, debe ser False.
'''
class Jugador:
    vivo=False
    @classmethod
    def revivir(cls):
        cls.vivo=True
Jugador.revivir()

#3.-EJERCICIO
'''
Crea un método de instancia lanzar_flecha() que reste en -1 la cantidad de flechas que tiene una instancia de Personaje, 
que cuenta con un atributo de instancia de tipo número, llamado cantidad_flechas.
'''
class Personaje:
    def __init__(self,cantidad_flechas):#se generan los parametros
        self.cantidad_flechas=cantidad_flechas #se inicializan los atributos y parametros

    def lanzar_flecha(self):#si no se coloca self, no se puede acceder a los atributos de la clase
        self.cantidad_flechas=self.cantidad_flechas - 1 #se restan flechas al atributo

    def imprimir_flechas(self):
        print(self.cantidad_flechas)

personaje=Personaje(10) #se inicializa al personaje con su cantidad de flechas
personaje.lanzar_flecha() #se manda a llamar al metodo de instancia para disminuir una flecha
personaje.imprimir_flechas() # se manda a imprimir la cantidad de flechas que tiene el personaje actualmente
personaje.lanzar_flecha()#se vuelve a restar otra flecha.
personaje.imprimir_flechas()#se nota que va disminuyendo consecutivamente
