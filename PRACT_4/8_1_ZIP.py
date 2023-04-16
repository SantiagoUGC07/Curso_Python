#ZIP sirve para junta dos lista en un tuple
Nombre = ['Ana', 'Hugo', 'Valeria']
Edad = [65, 29, 42]
Combinados = list(zip(Nombre,Edad))
print(Combinados)

#ZIP Acoplando tres listas y mostrando sus valores con un loop
Nombre = ['Ana', 'Hugo', 'Valeria']
Edad = [65, 29, 42]
Ciudad = ['Lima', 'Madrid', 'Mexico']

Combinados = list(zip(Nombre,Edad,Ciudad))
print(Combinados)
for nom,ed,ciu in Combinados:
    print(f"{nom} tiene {ed} años y vive en {ciu}")
