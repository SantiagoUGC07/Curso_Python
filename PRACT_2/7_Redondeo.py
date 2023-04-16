#REDONDEO round(redondeo,cuantos decimales)
#1 - redondear la sig
print(round(90/7))

#2 - redondeo de variable con decimales,
valor = round(95.666666,3)
print(valor)

#3 - se convierte en entero cuando se hace el redondeo dentor de la variable
valor = round(95.66666)
print(type(valor))

#4 - no se convierte a int si es fuera de la variable
valor= 95.666
round(valor)
print(type(valor))