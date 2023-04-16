#1.-EJERCICIO
print("\n1.-EJERCICIO")
'''
La función incorporada en Python len() tiene un comportamiento polimórfico, ya que calcula el largo de un objeto en función de su tipo
(strings, listas, tuples, entre otros), devolviendo la cantidad de items o caracteres que lo componen.
Crea un iterador que recorra los siguientes objetos: palabra, lista, tupla y muestre en pantalla (print())
para cada uno de ellos su longitud con la función len().
'''
from typing import List, Tuple

palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

dato: str | list[str] | tuple[int, int, int, int]
for dato in [palabra, lista, tupla]:#se encierran en corchetes para que dato itere entre ellos y tome su valor
    print(dato)#aqui dato toma los valores de palabra,lista y tupla
    print(len(dato))#de esta manera imprimimos la longitud de todos los tipos de datos.

#2.-EJERCICIO
print("\n2.-EJERCICIO")
'''
Cuentas con tres clases de personajes en un juego, los cuales cuentan con sus métodos de ataque específicos.
Crea un iterador que logre un ataque conjugado en el siguiente orden: Arquero, Mago, Samurai, 
llamando al método atacar() de cada uno de los personajes. Deberás crear instancias de cada una de las clases anteriores para construir un iterable (una lista llamada personajes) que pueda recorrese en dicho orden.
'''
class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")
mago=Mago()
arquero=Arquero()
samurai=Samurai()
for personaje in [mago,arquero,samurai]:#personaje toma el nombre de cada uno de los objetos y asi podemos llamar a sus metodos
    personaje.atacar()#ya no se necesita encerrar en un print para mostrar en pantalla.

#3.-EJERCICIO
print("\n3.-EJERCICIO")
'''
Tienes tres clases de personajes en un juego, los cuales cuentan con sus métodos de defensa específicos.
Crea una función llamada personaje_defender(), que pueda recibir un objeto (una instancia de las clases de tus personajes), 
y ejecutar su método defender() independientemente de qué tipo de personaje se trate.
'''
class Mago():
    def defender(self):
        print("Escudo mágico")
class Arquero():
    def defender(self):
        print("Esconderse")
class Samurai():
    def defender(self):
        print("Bloqueo")
mago=Mago()
arquero=Arquero()
samurai=Samurai()
def personaje_defender(personaje):
    personaje.defender()

personaje_defender(mago)
