#METODOS (upper - lower - split - join - find - replace) hay mas de 20 metodos
texto = "Este es el texto de federico"

#1 - Metodo UPPER (convertir texto a mayus)
print(texto.upper())
print(texto[2].upper())#cambia a mayus el caracter en la poscicion 2

#2 - Metodo LOWER (convertir texto a minus)
print(texto.lower())
print(texto[2].lower())#cambia a minus el caracter en la poscicion 2

#3 - Metodo SPLIT (separar los elementos, tomando como separador los espacios vacios,
# o el caracter que se coloque como separador)
print(texto.split())
print(texto.split("t"))#se toma como separador la t
print(texto[2].split())#se separar e imprime el caracter

#4  - Metodo JOIN unir textos.
a = "Aprender"
b = "Phyton"
c = "Es"
d = "Genial"
e = " ".join([a,b,c,d])#se construye una lista y se colocan espacios vacios con " " y el metodo join es para unirlos
f = "-".join([a,b,c,d])#si se coloca un "-" entre las comillas se coloca entre las palabras
print(e)
print(f)

#5 - Metodo FIND encontrar en el texto
print(texto.find("texto"))#busca la palabra en el texto y regresa la poscicion
print(texto.find("z"))#si buscas un caracter que no extiste, no manda error manda un -1

#6 - Metodo REPLACE templazar textos o caracter del texto
print(texto.replace("e","x"))#remplaza las E por X
print(texto.replace("Este", "PERRO"))#remplaza este por PERRO





