#PROGRAMAR UN ANALIZADOR DE TEXTO
#texto = input("ingresa tu texto: ")
#print(texto)
texto= input("Ingresa tu texto: ")
textoL = texto.lower()
letras = input("ingresa tres letras: ")

l1 = letras[0].lower()
l2 = letras[1].lower()
l3 = letras[2].lower()
lista ="".join([l1,l2,l3])
print(lista)
print("Imprimir cantidad de letras en el texto")
print(f"las veces que aparece \"{l1} \" en el texto son: {textoL.count(l1)}")
print(f"las veces que aparece \"{l2} \" en el texto son: {textoL.count(l2)}")
print(f"las veces que aparece \"{l3} \" en el texto son: {textoL.count(l3)}")
print(f"texto")

print("\n")
print("Imprimir cantidad de palabras")
palabras = textoL.split()
print(f"hemos encontrado: {len(palabras)}")

print("\n")
print("Imprimir letra inicia y letra final")
letra_inicio = textoL[0]
letra_final = textoL[-1]
print(f"la letra inicia es \"{letra_inicio}\" la letra final es \"{letra_final}\"")

print("\n")
print("Imprimir texto al revez")
palabras.reverse()
print(palabras)
textoR = " ".join(palabras)
print(f"el texto al revez dice : '{textoR}' ")

print("\n")
print("imprimir al revez mas chido")
textoR = textoL[::-1]
print(f"Imprimir texto al revez {textoR}")

print("\n")
Buscar_phyton = 'phyton' in texto
dic = {True: "si", False: "no"}
print(f"la palabra 'phyton' {dic[Buscar_phyton]} se encuentra. ")








