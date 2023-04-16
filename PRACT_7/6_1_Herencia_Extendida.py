#HERENCIA EXTENDIDA
'''
herencia extendida.
    no necesariamente todo lo que se hereda sera igual
    *clase hija
    puede heredar
    metodos heredados= los metodos que recibe de la clase padre
    metodos modificaods=los metodos que modifica de la clase padre
    metodos nuevos = los que no existen en la clase padre

    asi como puede tener los atributos heredados o los propios

Herencia multiple
en la herencia multiple se pueden tener dos clase padre heredando a una clase hija
y esa misma clase hija puede heredar a otra clase.
'''
print("\n EJEMPLO 1")
class Animal:
    def __init__(self,edad,color):
        self.edad=edad
        self.color=color
    def nacer(self):
        print("Este animal ha nacido")
    def hablar(self):
        print("Este animal emite un sonido")
class Pajaro(Animal):
    #HAY DOS MANERAS DE AGREGAR ATRIBUTOS A UNA CLASE HIJA
    def __init__(self,edad,color,altura_vuelo):
        # 2 metodo
        super().__init__(edad,color)#al usar super ya no tenemos que colocar cada atributo con su parametro,
        #se realizan las asignaciones para los atributos heredados ya solo resta hacer las asignacion para los nuevos atributos
        # 1 metodo
        #self.edad=edad
        #self.color=color
        self.altura_vuelo=altura_vuelo
    def hablar(self):
        print("pio")
    def volar(self,metros):
        print(f"El pajaro vuela {metros} metros")
#METODO HEREDADO EN LA CLASE HIJA
#piolin=Pajaro(3,"Amarillo")
piolin=Pajaro(3,"Amarillo",2)#al usuar super ya no puede llamar solo dos atributos con antes
piolin.nacer()
#METODO HEREDADO PERO MODIFICADO POR LA CLASE HIJA
piolin.hablar()
#METODOS NUEVOS EN LA CLASE HIJA
piolin.volar(10)

#USANDO LOS ATRIBUTOS PROPIOS DE LA CLASE HIJA
mi_animal=Animal(5,"negro")


#*****************
print("\n EJEMPLO 2")
class Padre:
    def hablar(self):
        print("Hola")

class Madre:
    def reir(self):
        print("Ja Ja")
    def hablar(self):
        print("Que tal")

class Hijo(Padre,Madre):#HEREDA PRIMERO LO DE PADRE QUE LO DE MADRE, LE DA PRIORIDAD A LOS METODOS DE PADRE
    pass

class Nieto(Hijo):#NIETO HEREDA TODO LO QUE PADRE HEREDO A HIJO YA QUE HEREDO TODO LO DEJ HIJO
    pass

mi_nieto=Nieto()
mi_nieto.hablar()#NIETO HEREDO PRIMERO EL METODO "HABLAR" DE PADRE QUE DE LA CLASE MADRE, ES POR ESO QUE IMPRIME LO QUE SE TIENE EN CLASE PADRE
mi_nieto.reir()#NIETO PUEDE IMPRIMIR LO QUE MADRE HEREDO A HIJO, DADO A QUE NIETO HEREDA LO DEL HIJO

print(Nieto.mro())#el metodo mro() nos sirve para visualizar el orden en el cual nieto heredara atributos y metodos de las otras clases

