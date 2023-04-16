#POLIMORFISMO
'''
polimorfismo:
poli= muchas
morfo= formas
los objetos pueden tomar distintas formas, ya que los objetos de distintas clases pueden compartir el mismo nombre del metodo,
y luego se pueden llamar esos metodos desde el mismo lugar pero aplicado en distintos objetos
'''
class Vaca:
    def __init__(self,nombre):
        self.nombre=nombre
    def hablar(self):
        print(self.nombre + "dice muu")

class Oveja:
    def __init__(self,nombre):
        self.nombre=nombre
    def hablar(self):
        print(self.nombre + "dice bee")

vaca1 = Vaca("Aurora")
oveja1= Oveja("Nube")

animales = [vaca1, oveja1]
for animal in animales:
    animal.hablar()#aqui se muestra el polimorfismo, dado a que se ejecuta el mismo metodo en distintas forma para disntito objetos

vaca1.hablar()#aqui se muestra el polimorfismo al ejecutar un metodo desde distintos objetos
oveja1.hablar()

def animal_habla(animal):#otra forma de polimorfismo es usando una funcion para ejectura un metodo con una variable para distintos objetos
    animal.hablar()
animal_habla(oveja1)#se manda objeto para ejecutar la funcion.
animal_habla(vaca1)

