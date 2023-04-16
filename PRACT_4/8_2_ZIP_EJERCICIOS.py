#1.-EJERCICIO combinar dos listas e una sola lista usando zip
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

combinar = list(zip(capitales,paises))
print(combinar)
for cap,pai in combinar:
    print(f"La capital de {pai} es {cap}")

#2.-EJERCICIO crear objeto zip apartir de dos listas
marcas = ["20","230","203"]
productos =[23,34,32]

mi_zip = zip(marcas,productos)
print(mi_zip)

#3.-EJERCICIO
uno = ('uno', 'dos', 'tres','cuatro', 'cinco')
dos = ('um', 'dois', 'três', 'quatro', 'cinco')
tres = ('one','two', 'three', 'four', 'five')
#cuatro = list(zip(cuatro / quatro / four))
#cinco = list(zip(cinco / cinco / five))
#for u,d,t in uno,dos,tres:
sum = zip(uno, dos, tres)
lista= list(sum)
print (lista)