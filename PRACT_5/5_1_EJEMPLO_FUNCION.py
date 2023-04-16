#EJEMPLO DE FUNCION
#DESEMPACAR TUPPLES
precios_cafe=[('capuchino',1.5),('Expreso',1.2),('Moka',1.9)]
for elemento in precios_cafe:#se toman ambos elementos del tupple cafe y precio
    print(elemento)#se imprimen los dos elementos del tupple
for cafe,precio in precios_cafe:#se dividen los elementos del tupple
    print(cafe)#se imprimen los valores del tipo de cafe
    print(precio)#se imprimen los valores del tipo de precio

#CONOCER CUAL ES EL CAFE MAS CARO
def cafe_mas_caro(lista_precios):
    precio_mayor=0
    cafe_mas_caro=''
    for cafe,precio in lista_precios:#se dividen en dos elementos para comparar
        if(precio>precio_mayor):#se compara cada elemento contra el anterior
            precio_mayor=precio#se asignan el valor del precio
            cafe_mas_caro=cafe#se asignan el valor del cafe
        else:
            pass
    return (cafe_mas_caro,precio_mayor)#se va a devolver en forma de tupple
print(cafe_mas_caro(precios_cafe))
#GUARDAR EN DOS VARIABLES E IMPRIMIR
cafe,precio=cafe_mas_caro(precios_cafe)
print(f'el cafe mas caro es: {cafe} cuyo precio es: {precio}')