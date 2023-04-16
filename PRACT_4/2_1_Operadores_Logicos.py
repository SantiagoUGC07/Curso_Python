#1.- Comparacion metdo and
mi_bool = 4 < 5 and 5 > 6
print(mi_bool)

#2.- Comparacion metodo and
mi_bool = (4 < 5) and (5 == 2+3)
print(mi_bool)

#3.- Comparacion metodo and strings
mi_bool = (55 == 55) and ('perro' == 'perro')
print(mi_bool)

#4.- Comparacion metodo or
mi_bool = 1 == 10 or 3 == 30
print(mi_bool)

#5.-Ejercicio comparacion or
texto = "esta frase es breve"
mi_bool = ('frase' in texto) and ('phyton' in texto)
print(mi_bool)

#6.- Ejercicio comparacion con negacion
mi_bool = not ('a' == 'a')#se niega el igual y manda false al print
print(mi_bool)

#7.- Ejercicio comparacion con doble negacion
mi_bool = not ('a' != 'a')#se niega doblement y dara un true
print(mi_bool)

