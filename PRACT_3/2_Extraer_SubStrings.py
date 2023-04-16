#EXTRAER CARACTERES, el numero antes del corchete no lo cuenta.
texto = "ABCDEFGHIJKLM"
fragmento = texto[2:4]#VA A EXTRAER LOS CARATERES EN LAS POSICIONES DE 2:4
print(fragmento)#IMPRIME LOS CARACTERES EXTRAIDOS

fragmento2 = texto[2:]#EXTRAE LOS CARACTERES DEL 2 HASTA EL FINAL
print(fragmento2)
print(type(fragmento2))

fragmento3 = texto[2:10:2]#EXTRAE LOS CARACTER DEL POSCISION 2 AL 10 DE DOS EN DOS POR EL NUMERO 2 AL FINAL.
print(fragmento3)

fragmento4 = texto[::3]#EXTRAE LOS CARACTER DEL INICIO AL FINAL DE TRES EN TRES
print(fragmento4)

fragmento5 = texto[::-2]#EXTRAE LOS CARACTER DEL INICIO AL FINAL DE DOS EN DOS PERO SE IMPRIME AL REVEZ
print(fragmento5)
