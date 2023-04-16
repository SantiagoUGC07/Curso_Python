#Metodos
'''
ya hemos creado metodos como __init__ este es un metodo especial

las funciones tienen la siguiente structura
def piar(self)
    print("pio")

los metodos se crean con la siguiente structura
def nombre_metodo(self,nombre_info)
    print(f"llamando metodo {objeto.nombre_info}"
*self hace referencia a cada instancia de la clase
'''

class Pajaro:
    alas=True
    def __init__(self,color,especie):
        self.color=color
        self.especie=especie

    def piar(self):
        print("pio, mi color es {}".format(self.color))#de esta manera llamamos el atributo de la instancia

    def volar(self,metros):
        print(f"el pajaro ha volado {metros} metros")

#crear instancia
piolin = Pajaro('amarillo', 'canario')
piolin.piar()#llamando metodo piar
piolin.volar(59)#llamando metodo volar
