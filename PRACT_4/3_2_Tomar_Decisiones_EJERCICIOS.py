#1.-EJERCICIO
num1 = input("Ingresa un numero: ")
num2 = input("Ingresa otro numero: ")
if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que num1")
else:
    print("Los numeros son iguales")
print("\n")
#2.-EJERCICIO
lic = input("tienes licencia? ")
edad = input("que edad tienes? ")
lic.lower()
if((lic == 'si') and (int(edad) >= 18)):
    print("puedes conducir")
elif((lic =='no') and (int(edad) >= 18)):
    print("No puedes conducir necesitas una licencia")
else:
    print("No puedes conducir aun, Debes tener 18 años y contar con una licencia")
print("\n")
#3.-EJERCICIO
habla_ingles = True
sabe_phyton = False
if((habla_ingles == True) and (sabe_phyton == True)):
    print("Cumples con los requisitos para postularte")
elif((habla_ingles == False) and (Sabe_Phyton == False)):
    print("Para postularte, necesitas saber programar en phyton y tener conocimientos de ingles")
elif((habla_ingles == True) and (sabe_phyton == False)):
    print("Para postularte, necesitas tener conocimientos de ingles")
else:
    print("Para postularte, necesitas saber programar en phyton")
print("\n")
