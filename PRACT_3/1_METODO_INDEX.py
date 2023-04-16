#METODO INDEX
#sirve para la poscicion en la que se encuentra un caracter
mi_texto = "Hola"
resu = mi_texto.index("o")
resultado = mi_texto[3]
print(resultado)
print(resu)
#la busqueda la hace de izq a derecha, encontrando el primer resultado
mi_texto2 = "hola cara de bola"
resu2 = mi_texto2.index("o",5,15)#hara la busqueda de la poscicion 5 hasta la 12
print(resu2)#de esta manera encontramos letras cuando se repiten
#CON ESTE METODO SE BUSCA DE DERE A IZQ
mi_texto3 = "hola cara de bola"
resu3 = mi_texto3.rindex("o")
print(resu3)