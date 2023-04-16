#1.-EJERCICIO
'''
Dada la clase Libro, implementa el método especial __str__ para que cada vez que se imprima el objeto,
devuelva '"{titulo}", de {autor}' (atención: el título debe estar encerrado entre comillas dobles).
'''
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
    def __str__(self):
        return f'\"{self.titulo}\", de {self.autor}'
libro=Libro("El coronel no tiene quien le escriba","Gabriel Garcia Marquez",10)
print(libro)

#2.-EJERCICIO
'''
Dada la clase Libro, implementa el método especial __str__ para que cada vez que se imprima el objeto, 
devuelva '"{titulo}", de {autor}' (atención: el título debe estar encerrado entre comillas dobles).
'''
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
    def __len__(self,):
        return self.cantidad_paginas
libro=Libro("El coronel no tiene quien le escriba","Gabriel Garcia Marquez",10)
print(len(libro))#len lee la cantidad_paginas que tiene el objeto por medio del metodo que definimos en la clase

#3.-EJERCICIO
'''
Dada la clase Libro, implementa el método especial __del__ para que el usuario sea informado con 
el mensaje "Libro eliminado", mostrándolo en pantalla cada vez que el libro se elimine.
'''
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
    def __del__(self):
        return print("El libro fue eliminado")
libro=Libro("El coronel no tiene quien le escriba","Gabriel Garcia Marquez",10)
del libro