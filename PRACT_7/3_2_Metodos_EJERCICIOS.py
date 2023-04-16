#1.-EJERCICIO
'''
Crea una clase Perro. Dicho perro debe poder ladrar.
Crea el método ladrar() y ejecútalo en una instancia de Perro. Cada vez que ladre, debe mostrarse en pantalla "Guau!".
'''
class Perro:
    def ladrar(self):
        print("Guau!")
#se genera instancia u objeto perro
perro=Perro()
#se llama al metodo ladrar
perro.ladrar()

#2.-EJERCICIO
'''
Crea una clase llamada Mago, y crea un método llamado lanzar_hechizo() (deberá imprimir "¡Abracadabra!").
Crea una instancia de Mago en el objeto merlin, y haz que lance un hechizo.
'''
class Mago:
    def lanzar_hechizo(self):
        print("¡Abracadabra!")
#se crear instancia o objeto merlin de la clase Mago
merlin=Mago()
merlin.lanzar_hechizo()#el objeto merlin llama al metodo lanzar_hechizo

#3.-EJERCICIO
'''
Crea una instancia de la clase Alarma, que tenga un método llamado postergar(cantidad_minutos). El método debe imprimir en pantalla el mensaje
"La alarma ha sido pospuesta {cantidad_minutos} minutos"
'''
class Alarma:
    def postergar(self,cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")
#creando instancia
alarma=Alarma()
#llamando al meotdo
alarma.postergar(10)#como llamar a un metodo sin usar __init__

