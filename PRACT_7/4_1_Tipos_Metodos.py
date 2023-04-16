#DECORADORES
'''
metodos de instancia:
    def mi_method(self):
        print("algo")
    mi_method()

    #acceden y modifican atributos del objeto
    #accder a otros metodos
    #modificar el estado de la clase

metodos de clase  @classmethod
    @classmethod(cls):
    def mi_method(cls):
        print("algo")

    #no estan asociados a las instancias de la clase, si a la clase
    #pueden ser llamados desde la clase y desde una instancia tambien
    #no pueden acceder a los atributos de la instacina, pero si pueden modificar los atributos de la clase

metodos estaticos @staticmethod
    @staticmethod
    def mi_method():
        print("algo")

    #no pueden modificar el estado de la instancia y clase
    #pueden aceptar parametros de entrada
    #pueden servir para indicar que un metodo no puede modificar el estado de la instacia o clase
    #se pueden ver como funciones normales pero con la funcion de acceder a una clase
'''

class Pajaro:
    alas=True
    #METODOS DE INSTANCIA
    def __init__(self,color,especie):
        self.color=color
        self.especie=especie
    def piar(self):
        print("pio")
    def volar(self,metros):
        print(f"el pajaro vuela {metros} metros")
        self.piar()#se pueden llamar otros metodos de instancia
    #metodo de instancia tambien por que accden al self y modifican a cada una de las instancias del objeto Pajaro
    def pintar_negro(self):
        self.color="negro"
        print(f"Ahora el pajaro es {self.color}")

    #METODOS DE CLASE
    #esta relacionado a la clase
    @classmethod
    def poner_huevos(cls,cantidad):
        print(f"puso {cantidad} huevos")
        # no podemos llamar metodos de instancia, ni se puede acceder a los atributos de instancia que en este caso es color o especie
        #print(f"Es de color {self.color}") no se puede acceder a los atributos de instancia
        #SE PUEDE ACCDER A LOS METODOS DE CLASE para modificar los atributos de clase
        cls.alas=False
        print(Pajaro.alas)

    #METODOS ESTATICOS
    @staticmethod
    def mirar():
        #estos metodos no pueden modificar las intancias o atributos de la clase
        #SIRVEN PARA EVITAR QUE OTROS METODOS MODIFIQUEN A TUS METODOS O INSTANCIAS
        print("El pajaro mira")


#CREANDO INSTANCIA
piolin =Pajaro("Amarillo","canario")
#llamando metodo de instancia pintar_negro
piolin.pintar_negro()#se imprime el nuevo color de la instancia del objeto
piolin.volar(50)#se llama al metodo el cual llama a otro metodo
piolin.alas=False #se accede a la propiedad alas que pertenece a la clase
print(piolin.alas)

#COMO LLAMAR METODO DE CLASE
#se puede mandar a llamar aun si no se tiene una instancia creada
Pajaro.poner_huevos(3)

#COMO LLAMAR METODO ESTATICO
Pajaro.mirar()



