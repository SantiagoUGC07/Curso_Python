#1.-EJERCICIO
'''
Si la clase Hija ha heredado de su padre la forma de reir, y de su madre la vocación, y hoy tienen el mismo trabajo en la Fiscalía,
crea la herencia múltiple que le permita a esta clase heredar correctamente de Padre y Madre.
'''
class Padre():
    def trabajar(self):
        print("Trabajando en el Hospìtal")
    def reir(self):
        print("Ja ja ja!")

class Madre():
    def trabajar(self):
        print("Trabajando en la Fiscalía")


class Hija(Madre,Padre):
    pass
hija=Hija()
hija.trabajar()
hija.reir()

#2.-EJERCICIO
'''
"El ornitorrinco es una de las criaturas más raras del mundo: aunque es un mamífero, pone huevos; y amamanta a sus crías pero no tienen mamas." (National Geographic)
Crea una clase Ornitorrinco que herede de otras clases: Vertebrado, Pez, Reptil, Ave y Mamifero, tal que "construyas" un animal que tiene los siguientes métodos y atributos:

- poner_huevos()
- tiene_pico = True
- vertebrado = True
- venenoso = True

- nadar()
- caminar()
- amamantar()
'''
class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Ave,Reptil,Pez,Mamifero):
    def __init__(self,vertebrado,tiene_pico,venenoso):
        super().__init__(vertebrado,tiene_pico,venenoso)

#3.-EJERCICIO
'''
Un hijo ha heredado de su padre todas sus características, sin embargo, tienen diferentes hobbies. 
Logra que la clase Hijo herede de Padre todos sus métodos y atributos, sobreescribiendo el método hobby() para que se devuelva[1]: "Juego videojuegos en mi tiempo libre"
'''
class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"

    def reir(self):
        return "Jajaja"
    def hobby(self):
        return "Pinto madera en mi tiempo libre"
    def caminar(self):
        return "Caminando con pasos largos y rápidos"

class Hijo(Padre):
    def __init__(self,color_ojos,tipo_pelo,altura,voz,deporte_preferido):
        super().__init__(color_ojos,tipo_pelo,altura,voz,deporte_preferido)
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"
