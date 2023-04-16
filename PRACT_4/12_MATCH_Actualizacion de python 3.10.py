#COINCIDENCIAS DE PATRONES como switch, pero MATCH es mucho mejor ya que permite hacer algo distinto
#deacuerdo a un patron

#ejemplo elegir una opcion entre distintas
serie = "N-02"
if serie == "N-01":
    print("Samsung")
elif serie == "N-02":
    print("Nokia")
elif serie == "N-03":
    print("Motorola")
else:
    print("No existe ese producto")

#version con MATCH
match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No existe ese producto")

#QUE HACE ESPECIAL A MATCH
cliente = {'nombre':'Federico', 'edad':45, 'ocupacion':'instructor'} #LOS PATRONES establecidos
pelicula={'titulo':'Matrix', 'ficha_tecnica': {'protagonista':'keanu reeves', 'director': 'lana y lilly wachowski'}}
elementos = [cliente, pelicula, 'libro']#BUSCARA EN LOS CASE DE MATCH los patrones similares a los establecidos
for e in elementos:
    match e:
        case {'nombre': nombre, 'edad': edad, 'ocupacion':ocupacion}:
            print('Es un cliente')
            print(nombre,edad,ocupacion)
        case {'titulo':titulo, 'ficha_tecnica':{'protagonista':protagonista, 'director':director}}:
            print("Es una pelicula")
            print(titulo,protagonista,director)
        case _:
            print("No se que es esto")
