#1.-EJERCICIO imprimir numero elevado a una potencia
def potencia(num1,num2):
    total = num1**num2
    return total
total = potencia(2,3)
print(total)

#2.-EJERCICIO Imprimir la cantidad convertida de dolar a euro enviar la cantidad de dolares a convertir a euros
#y regresarla para imprimir, tomar esto en cuenta 1 USD = 0.90 EUR.
def usd_a_eur(MonDolar):
    Euros = MonDolar*0.9
    return Euros
print(f"La cantidad en euros es: ", +usd_a_eur(MonDolar=3))

#3.-EJERCICIO
#Crea una funcion llamada invertir_Palabra que tome los caracteres de una palabra dad como argumento
#invierta el orden de sus caracteres y los devuelva de ese modo y en mayusculas
#phyton debera devolver nohyp
def invertir_palabra(palabra):
    palabra=palabra.upper()
    lista = list(palabra)
    lista.reverse()
    print(lista)
    palabra = "".join(lista)
    return palabra
palabra = "Phyton"
palabra=invertir_palabra(palabra)
print(palabra)
#3.-EJERCICIO OTRA SOLUCION
palabra = "Curso de Python"
def invertir_palabra2(palabra):
    palabra = palabra[::-1]
    print(palabra)
    palabra = palabra.upper()
    return palabra
palabra=invertir_palabra2(palabra)
print(palabra)
