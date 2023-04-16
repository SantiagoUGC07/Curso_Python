#1.-EJERCICIO asignar una fecha
'''
Crea un objeto fecha llamado mi_fecha que almacene el día 3 de febrero de 1999
'''
from datetime import date
mi_fecha=date(1999,2,3)
print(mi_fecha)

#2.-EJERCICIO fecha pc
'''
Crea un objeto en la variable hoy que siempre almacene la fecha actual cuando sea invocada.
'''
hoy=date.today()
print(hoy)

#3.-EJERCICIO almacenar los minutos actuales
'''
En una variable llamada minutos, almacena únicamente los minutos de la hora actual.
Por ejemplo, si se ejecutara a las 20:43:17 de la noche, la variable minutos debe almacenar el valor 43
'''
from datetime import datetime
minutos=datetime.now().minute
print(minutos)