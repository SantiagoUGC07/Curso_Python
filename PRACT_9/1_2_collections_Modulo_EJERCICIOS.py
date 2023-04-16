from collections import Counter
from collections import defaultdict
from collections import deque
#1.-EJERCICIO
'''
Aplica un Counter (contador) sobre la lista de números entregada a continuación, y almacénalo en una variable llamada contador
'''
print("\n1.-EJERCICIO")
lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]
contador = Counter(lista)
print(contador)

#2.-EJERCICIO
print("\n2.-EJERCICIO")
'''
Crea un diccionario llamado mi_diccionario, para el cual, cuando no se halle una palabra clave buscada, 
se cargue con el string "Valor no hallado".

    Carga el diccionario, al menos, con el siguiente par de datos:
    
    palabra clave = edad
    
    valor = 44

Utiliza el método defaultdict del módulo Collections.
'''
mi_diccionario={"edad":"44"}
mi_diccionario=defaultdict(lambda:'Valor no hallado')
print(mi_diccionario['nombre'])

#3.-EJERCICIO
print("\n3.-EJERCICIO")
'''
Una cola doblemente terminada o deque (del inglés double ended queue) es una estructura de datos lineal que 
permite insertar y eliminar elementos por ambos extremos.

Investiga más al respecto en cualquier sitio de documentación, y a continuación implementa una deque a partir 
del módulo collections. Los elementos iniciales de la lista se brindan a continuación.

    ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]

La lista debe tener la capacidad de incorporar elementos por la izquierda, y recibir el nombre lista_ciudades.
'''
#una deque sirve para agregar elementos a una lista por ambos extremos, asi como modificar la misma, se requiere importar deque
lista_ciudades=deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])
#appendleft agrega la palabra por el extremo izquierdo de la lista
lista_ciudades.appendleft("caca")
print(lista_ciudades)
print(type(lista_ciudades))#es un tipo collections deque