#MODULO PATH
'''
Path: nos sirver para
crear o morver archivos
enumerar archivos
crear rutas basadas en strings ( cambiar string a una ruta de carpetas)
NO SE CREAN CARPETAS.
LAS CARPETAS FUERON AGREGADAS
'''
from pathlib import Path
print("1. RUTA RELATIVA")
guia = Path("Barcelona", "Sagrada familia.txt")#para crear rutas de acceso. usando el constructor path
#una ruta relativa se puede cambiar en cualquier ruta de nuestro equipo
print(guia)#se imprime la ruta con una ruta absuluta

print("\n2. RUTA ABSOLUTA")
base= Path.home()
guia = Path(base, "Barcelona", "Sagrada familia.txt")#para crear rutas de acceso. usando el constructor path
#una ruta relativa se puede cambiar en cualquier ruta de nuestro equipo
print(base)#devuelve una instancia path con una ruta absoluta al directorio principal
print(guia)#se imprime la ruta con una ruta absuluta

print("\n3. RUTA ABSOLUTA Agregando otra ruta")
base= Path.home()
guia = Path(base, "Europa", "España", Path("Barcelona", "Sagrada familia.txt"))#para crear rutas de acceso.
#se tiene la base (ruta absoluta) luego la direccion y con un path unimos las dos rutas relativas.
print(guia)#se imprimen las rutas relativas con una ruta absuluta

print("\n4. APUNTAR A DISTINTOS ARCHIVOS")
base= Path.home()
guia = Path(base, "Europa", "España", Path("Barcelona", "Sagrada familia.txt"))#para crear rutas de acceso.
#se tiene la base (ruta absoluta) luego la direccion y con un path unimos las dos rutas relativas.
guia2 = guia.with_name(("La_pedrera.txt"))#se cambia la ruta final por el sig archivo
print(guia)#solo se imprime las rutas relativas definidas , mas la ruta absoluta
print(guia2)#se imprimen las rutas relativas (cambiando la direccion final) mas la ruta absuluta
print("\n5. APUNTAR A DISTINTOS ARCHIVOS ")
print(guia.parent.parent)#se imprime regresando dos rutas atras, para salir de una carpeta se usa partent

print("\n6. ENUMERAR SOLO LOS TXT EN UNA CARPETA")
guia = Path(Path.home(), "Europa")
for txt in Path(guia).glob("*.txt"):#se accede al metodo glob y se usa * asterisco que significa todo y acceder a los archivos txt de la carpeta
    print(txt)
print("\n7. MOSTRAR TODOS LOS TXT EN LAS CARPETAS")
for txt in Path(guia).glob("**/*.txt"):#s
    # e accede al metodo glob y se usa **/* para mostrar todos los archivos txt dentro de todas las carpetas
    print(txt)

print("\n8. MOSTRAR EL OBJETO DE UNA CARPETA ")
guia = Path("Europa", "España", "Barcelona", "Sagrada familia.txt")
en_europa = guia.relative_to(Path("Europa"))#metodo relative_to sirve para devolver un objeto relacionado con el objeto determinado (en este caso el archivo .txt
en_espania = guia.relative_to(Path("Europa","España"))
print(en_europa)#imprime el objeto relacionado con guia osea sagrada familia.txt
print(en_espania)