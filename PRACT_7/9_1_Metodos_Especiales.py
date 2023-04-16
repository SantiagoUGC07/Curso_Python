#METODOS ESPECIALES

#metodo sin clase
mi_lista=[1,1,1,1,1,1,1]
print(len(mi_lista))#metodo len que tiene integrado python
#Metodos especiales
class CD:
    def __init__(self,autor,titulo,canciones):
        self.autor=autor
        self.titulo=titulo
        self.canciones=canciones
    def __str__(self):#DEFINIMOS como se imprimen los strings para evitar que se imprima solo donde esta el objeto
        return f"Album:{self.titulo} de {self.autor}"
    def __len__(self):#DEFINIMOS como devolver la cantidad de valores por el metodo len
        return self.canciones
    def __del__(self):#ELIMINAR
        return print("Se ha eliminado el CD")
mi_cd=CD('Pink Floyd','The Wall', 24)
print(mi_cd)#se imprime en forma de string
print(len(mi_cd))#se imprime la cantidad de canciones en el album

del mi_cd#se borra el objeto y la memoria... y como lo definimos en la clase se imprime que se borro

