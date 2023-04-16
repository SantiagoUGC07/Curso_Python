#limpiar consola
#depende de la consola o IDE
from os import system
'''
system('cls') #para windows
system('clear') #para otro sistema operativo
'''
nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")

system('cls')

print(f"Tu nombre es {nombre} y tienes {edad} años")

'''
IMPORTANTE ANTES DE EJECUTAR system('cls')
para lograr el borrado de pantalla click en la barra de tareas de pycharm
->Run
->Debug
->Edit Configurations..
-->Execution
--->Emulate terminal in output console
'''