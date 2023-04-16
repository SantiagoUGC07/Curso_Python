#Modulo datetime
import datetime
'''
mi_hora = datetime.datetime #se refiere a fecha y hora
mi_hora = datetime.date#solo se refiere a la fecha
mi_hora = datetime.time#solo se refiere a la hora
'''
#1.-TIME
mi_hora = datetime.time(17,35)#hr y min cada coma agrega mas.
print("LA HORA")
print(type(mi_hora))
print(mi_hora)#se muestran la hr y min
print(mi_hora.minute)#solo se muestra los minutos
mi_hora = datetime.time(17,35,12)#se agregan segundos a la hr y min
print(mi_hora)#se imprime la hora total

#2.-DATE
print("LA FECHA ESTABLECIDA")
mi_dia = datetime.date(2025,10,17)#se agrega la fecha
print(mi_dia.ctime())#se imprime la fecha que se indico
#2_1_FECHA DE LA PC
print("LA FECHA DE LA PC")
print(mi_dia.today())#se imprime la fecha de la pc

#3.-date y time
#se debe importar de la sig manera, la importe en esta linea para que no afecte al demas codigo
from datetime import datetime#para agrgar fecha y hora en una variable
print("LA FECHA Y HORA ESTABLECIDA")
mi_fecha=datetime(2025,5,25,22,10,15,2123)
print(mi_fecha)

#4.-DATE cambiar un elemento de la fecha
print("cambiando el mes")
mi_fecha=mi_fecha.replace(month=11)
print(mi_fecha)

#5.-ESTABLECER FECHAS y hacer OPERACIONES con las mismas
#se requiere importar date. de la sig manera
#5_1_CANTIDAD DE DIAS VIVO
from datetime import date
print("CANTIDAD DE DIAS VIVO")
nacimiento = date(1995,3,5)
defuncion = date(2095,6,19)
vida = defuncion - nacimiento
print(vida)#para ver los dias de vida y hora
print(vida.days)#para ver solo los dias
#5_2_CANTIDAD DE HORAS DESPIERTO
print("cantidad de horas despierto y en seg igual")
despierta = datetime(2022,10,5,7,30)#establecemos la fecha y luego la hora(7:30min)
duerme = datetime(2022,10,5,23,45)#establecemos la fecha y luego la hora(23:45min)
vigilia = duerme - despierta#restamos las horas
print(vigilia)#la cantidad de horas en despierto
print(vigilia.seconds)#la cantidad en segundos despierto



