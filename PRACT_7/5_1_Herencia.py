#Herencia
'''
se pueden heredar atributos o metodos de una clase padre a una hija
UNA CLASE HIJA puede sobres escribir los metodos y atributos de la clase padre
e incluso crear los propios.
'''
class Animal:#clase padre
    def __init__(self,edad,color):#de esta manera se crean los atributos
        self.edad = edad
        self.color = color
    def nacer(self):
        print("Este animal ha nacido")
class Pajaro(Animal):#clase hija
    pass

#CREACION DE INSTANCIAS
piolin=Pajaro(2,"Amarillo")#piolin hereda los atributos de la clase animal
print(piolin.color)#y podemos acceder a sus atributos
print(piolin.edad)
piolin.nacer()#piolin heredo el metodo nacer de clase Animal


print(Pajaro.__bases__)#nos indica la clase pajaro hereda de la clase animal
print(Animal.__subclasses__())#nos indica la clase animal hereda a la clase pajaro, y si hubieran mas clases se mostraria el listado
