#1.-EJERCICIO
'''
Crea una clase llamada Casa, y asígnale atributos: color, cantidad_pisos.
Crea una instancia de Casa, llamada casa_blanca, de color "blanco" y cantidad de pisos igual a 4.
'''
class Casa:
    def __init__(self,color,cantidad_pisos):
        self.color=color
        self.atributo_cantidad_pisos=cantidad_pisos
casa_blanca=Casa("blanco",4)#se asignan los parametros para los atributos color y atributo_cantidad_pisos
#no olvides colocar el nombre de la clase
print(f"mi casa es {casa_blanca.color} y de {casa_blanca.atributo_cantidad_pisos} pisos")

#2.-EJERCICIO
'''
Crea una clase llamada Cubo, y asígnale el atributo de clase:
caras = 6

y el atributo de instancia:
color
Crea una instancia cubo_rojo, de dicho color.
'''
class Cubo:
    caras=6
    def __init__(self,color):
        self.color=color
cubo_rojo=Cubo("rojo")
print(f"el cubo es de color {cubo_rojo.color} y tiene {cubo_rojo.caras} caras")

#3.-EJERCICIO
'''
Crea una clase llamada Personaje, y asígnale el siguiente atributo de clase:
real = False

Crea una instancia llamada harry_potter con los siguientes atributos de instancia:
especie = "Humano"
magico = True
edad = 17
'''
class Personaje:
    real=False
    def __init__(self,especie,magico,edad):
        self.especie=especie
        self.magico=magico
        self.edad=edad

harry_potter=Personaje("Humano",True,17)
print(f"harry potter es un {harry_potter.especie} es magico {harry_potter.magico} y tiene {harry_potter.edad} años el no es real {harry_potter.real}")