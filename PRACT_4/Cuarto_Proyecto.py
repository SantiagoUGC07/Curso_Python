#Elaborar un juego donde se genere un numero aleatorio del 0 al 100, el cual el usuario debe adivinar
#Solo tiene 8 oportunidades, mostrar mensajes si equivoca o acierta.
from random import randint
num_sec = randint(1,100)
resp1 = input("Hey!, what's your name?:  ").upper()

print(f"HEllO, {resp1}!! do you wanna play a game?")
print("You have to choice one number from one to 100")
print("\nRemember you only have 8 opportunities")
print("Let's get it started")
int=0
print(f"The secret number is {num_sec}")
while int < 8:
    resp2 = input(f"Introduce the number: ")
    resp2 = float(resp2)
    if(resp2 == num_sec):
        print("YES! THE ANSWERD IS CORRECT")
        break
    elif(resp2<1):
        print("The number is less than secret number")
    elif(resp2>100):
        print("The number is higher than secret number")
    else:
        print("The answerd INCORRECT")
    int+=1
    continue
if int == 8:
    print("You've exceeded the limit of attempts")