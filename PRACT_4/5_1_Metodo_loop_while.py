#Metodo while
monedas = 5
while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:print("no tengo mas dinero")

#para colocar una pregunta
respuesta = 's'
while respuesta == 's':
    respuesta = input("quieres seguir? (s/n)")
else:
    print("Gracias")

#break
nombre = input("tu nombre; ")
for letra in nombre:
    if letra == 'r':
        break  # interrupe la iteracion
    print(letra)


#continue
nombre = input("tu nombre; ")
for letra in nombre:
    if letra == 'r':
        continue#interrupe la iteracion actual y continua
    print(letra)



