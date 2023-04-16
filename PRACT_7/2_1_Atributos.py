#Atributos
'''
existen dos tipos de atributos
para la clase y afectan a todos los objetos de la clase
los atributos de instacia afectan a solo un objeto de la clase
'''
class Pajaro:
    alas=True #de esta manera se le asigna un atributo a todos los objetos

    def __init__(self,color,especie):#creando el metodo constructor para el atributo de la clase pajaro, se fijan los atributos que siempre se pasaran
        #se declaran los parametros color y especie
        self.color=color#self.color es el atributo y color es el parametro
    #el sistema atravez de init se fija que instancia se debe mandar, self sirve para representar la instancia que queremos pasar en este caso color
        self.atributo=especie
    # en este caso cambiamos especie por atributo, para visualizar como llamariamos al parametro

mi_pajaro=Pajaro("negro","tucan")#se asignan los atributos en orden a como fueron declarados
palabra="Hola"

mi_pajaro.color#al poner el objeto seguido de un punto se muestran todos los atributos como en el sig ejemplo de la palabra string
palabra.lower()#se muestra el string y al poner un punto se coloca los metodo de string

print(mi_pajaro.color)
print(palabra.lower())

print(f"mi pajaron es un {mi_pajaro.atributo} de color {mi_pajaro.color} ")

print(mi_pajaro.alas)#se imprime el atributo general





