#1.-EJERCICIO
#Almacena en la variable ruta_base, un objeto Path que señale el directorio base del usuario.
from pathlib import Path
print("1.-EJERCICIO")
ruta_base = Path.home()
print(ruta_base)

#2.-EJERCICIO
#Implementa y crea una ruta relativa que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:
print("\n2.-EJERCICIO")
ruta = Path("Curso Python", "Día 6", "practicas_path.py")
print(ruta)

#3.-EJERCICIO
#Implementa y crea una ruta absoluta que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:
print("\n3.-EJERCICIO")
ruta = Path(ruta_base,Path("Curso Python", "Día 6", "practicas_path.py"))
print(ruta)