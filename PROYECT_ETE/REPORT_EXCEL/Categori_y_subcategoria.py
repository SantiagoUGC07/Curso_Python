import pandas as pd
import re
lista=["SERVICIO DE DBA.REVISIÓN DE PERFORMANCE DE LA BASE DE DATOS",
       "SERVICIO DE CNC.REVISIÓN DE PERFORMANCE DEL SISTEMA",
       "SERVICIO DE SEGURIDAD.CORREO.PROBLEMAS.ENCOLAMIENTO"]

def dividir_cat_y_subcat(can_elementos):
    NewlistCategorias=[]
    NewlistSubcategorias = []
    j=0
    while(j<can_elementos):
        #se coloca una j para que recorra por todos los elementos en la lista
        Ccaracter = lista[j].find('.')#se busca la poscicion del punto en la lista
        #print(Ccaracter)#se imprime la posicion del punto de izq a derecha para hacerlo al contrario se ocuparia la funcion rfind()
        i=0
        cadena1=[]
        cadena2=[]
        for letras in lista[j]:
            # 1.-SE TOMA LA CATEGORIA
            if i<Ccaracter:
                cadena1.append(letras)
            # 2.-SE TOMA LA SUBCATEGORIA
            elif i>Ccaracter:#se pone mayor para no agregar el punto a la lista
                cadena2.append(letras)
            i+=1
        Categoria="".join(cadena1)#se cambia a string la lista cadena1 que es la categoria
        Subcategoria="".join(cadena2)#se cambia a string la lista cadena2 que es la subcategoria
        NewlistCategorias.append(Categoria)
        NewlistSubcategorias.append(Subcategoria)
        j+=1
    return NewlistCategorias, NewlistSubcategorias

Categoria,Subcategoria = dividir_cat_y_subcat(3)
print(Categoria,Subcategoria)


#CREAR UN DATAFRAME APARTIR DE STRINGS columnas categoria subcategoria y fecha
df = pd.DataFrame()
df["Fecha"]=["01/02/2023  10:50:14 a. m.","28/02/2023  09:50:14 a. m.","12/02/2022  08:40:14 a. m."]
#df = df.append(pd.DataFrame(fila,columns=[Categoria]), ignore_index=True)#agregar datos horizontal
df ["Categoria"]= Categoria
df ["Subcategoria"]= Subcategoria

#IMPRIMIR DATAFRAME
print(df)
#FILTRAR DATAFRAME POR FECHA PERO ESTA FECHA NO ES TIMESTAMP por eso se puede
print(df["Fecha"].str.findall('^[02/2023].*'))


#REALIZAR OTRO TIPO DE FILTROS
# Get countries starting with letter P solo aplica con series de strings
S=pd.Series(['Finland','Colombia','Florida','Japan','Puerto Rico','Russia','france','28/02/2023  09:50:14 a. m.'])
S[S.str.match(r'(^P.*)')==True]#buscar una letra en especifico
[itm[0] for itm in S.str.findall('^[Ff].*') if len(itm)>0]#buscar en todo con la letra f o F
print(S.dtypes)
print([itm[0] for itm in S.str.findall('^[02/2023].*') if len(itm)>0])#para buscar la fecha por mes usando re pero solo funciona con str, no con los formatos timestamp del excel
print(S.iloc[:])
print([itm[0] for itm in S.str.findall('^[02/2023].*') if len(itm)>0])