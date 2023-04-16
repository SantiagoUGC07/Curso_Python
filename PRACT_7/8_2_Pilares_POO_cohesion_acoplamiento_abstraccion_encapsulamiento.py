#1.-COHESION
'''
La cohesión se refiere al grado de relación entre los elementos de un módulo. Cuando diseñamos una función,
debemos identificar de un modo bien específico qué tarea va a realizar, reduciendo su finalidad a un objetivo único y bien definido.

*Cohesión débil: indica que la relación entre los elementos es baja, y por lo tanto no tienen una única funcionalidad.
*Cohesión fuerte: indica que existe una alta relación entre los elementos existentes dentro del módulo.
                    Este debe ser nuestro objetivo al diseñar programas.
'''
#Ejemplo_Cohesion
#Cohesion Fuerte; dado que se envian los valores a la funcion
def suma(num1, num2):
    resultado = num1 + num2
    return resultado
#Cohesion Debil:dado a que se solicitan los valores
def suma():
    num1 = float(input("Elige un número"))
    num2 = float(input("Elige otro número"))
    resultado = num1 + num2
    return resultado

#2.-ACOPLAMIENTO
'''
El acoplamiento es un concepto que mide la dependencia entre dos módulos distintos (como por ejemplo, clases). Podemos hablar de dos tipos:
*Acoplamiento débil: que implica que no hay dependencia entre un módulo y otros. Esta es la situación ideal.
*Acoplamiento fuerte: que es la situación contraria, e indica que el módulo tiene dependencias internas con otros.
'''
#Ejemplo Acoplamiento
#Acoplamiento fuerte
class Mascota:
    tiene_patas = True
    pass
class Perro:
    def correr(self, velocidad):
        if Mascota.tiene_patas:#se tiene dependencia de la clase mascota
            self.velocidad = velocidad

mi_mascota = Perro()
mi_mascota.correr("rápido")
print(mi_mascota.velocidad)

#3.-ABSTRACCION
'''
La abstracción es el pilar de la programación orientada a objetos que se relaciona con ocultar toda la complejidad que algo puede tener por dentro,
ofreciendo una interfaz con funciones de alto nivel, por lo general sencillas de usar, 
que pueden ser usadas para interactuar con la aplicación sin tener conocimiento de lo que hay dentro.
'''

#4.-ENCAPSULAMIENTO
'''
El encapsulamiento es el pilar de la programación orientada a objetos que se relaciona con ocultar al exterior determinados 
estados internos de un objeto, tal que sea el mismo objeto quien acceda o los modifique, 
pero que dicha acción no se pueda llevar a cabo desde el exterior, llamando a los métodos o atributos directamente.
'''
class Persona:
    atributo_publico = "Mostrar"   # Accesible desde el exterior
    __atributo_privado = "Oculto"  # No accesible
    # No accesible desde el exterior
    def __metodo_oculto(self):
        print("Este método está oculto")#para poder acceder a este metodo podemos hacerlo atravez de otro metodo
        self.__variable = 0
    # Accesible desde el exterior
    def metodo_normal(self):#accedemos al metodo oculto desde este metodo
        # El método si es accesible desde el interior
        self.__metodo_oculto()
alumno = Persona()
# alumno.__metodo_oculto()  # Este método no es accesible desde el exterior
alumno.metodo_normal()      # Este método es accesible
'''
Existe un pequeño truco (no recomendado) para acceder a los atributos y métodos ocultos. 
Dichos métodos están presentes con un nombre algo distinto:
instancia + _ + NombreClase + método/atributo oculto
'''
alumno._Persona__metodo_oculto()
print(alumno._Persona__atributo_privado)