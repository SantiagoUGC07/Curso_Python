import pandas as pd
import re
import openpyxl
from pathlib import Path
import xlrd
from openpyxl import load_workbook
import os
import xlsxwriter
from openpyxl import Workbook
import numpy
from datetime import datetime

'''
sheet_name=nombre de la pagina
header= desde donde comienza la fila
names= nombres de las columnas
index_col= cual sera la columna index
usecols= rango de las columnas
'''

datos = pd.read_excel(r'C:\Users\uri\Desktop\Curso_Python\PROYECT_ETE\REPORT_EXCEL\REPORTE INCI.xlsx',
                      sheet_name='Hoja1',header=1,names=None,index_col=None,usecols='A:U',engine='openpyxl')


#datos['FECHA APERTURA'] = datos['FECHA APERTURA'].astype('object')#cambiar el tipo de formato

#TIPO DE DATOS DEL DATAFRAME
print(datos.dtypes)

#CONVERTIR COLUMNA A LISTA  para posterior separar
CATEGORIA=list(datos["CATEGORIA"])
print(f"la lista de {CATEGORIA}")

def dividir_cat_y_subcat(can_elementos):
    NewlistCategorias=[]
    NewlistSubcategorias = []
    j=0
    while(j<can_elementos):
        #se coloca una j para que recorra por todos los elementos en la lista
        Ccaracter = CATEGORIA[j].find('.')#se busca la poscicion del punto en la lista
        #print(Ccaracter)#se imprime la posicion del punto de izq a derecha para hacerlo al contrario se ocuparia la funcion rfind()
        i=0
        cadena1=[]
        cadena2=[]
        for letras in CATEGORIA[j]:
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

Categoria,Subcategoria = dividir_cat_y_subcat(len(datos))#se envia la cantidad de filas correspondientes 
#CREANDO COLUMNA CATEGORIA
datos["CATEGORIA"] = Categoria
#CREANDO COLUMNA SUBCATEGORIA
datos["SUBCATEGORIA"] = Subcategoria  

#FILTRAR POR FECHA
#las fechas tomas del excel se imprimen como timestamp formato de datetime por lo que para filtrar se ocupa el sig metodo
#start_datetime = datetime.strptime('2022-03-04 12:00:00', '%Y-%m-%d %H:%M:%S') #IGUAL SE PUEDE FILTRAR CON HORAS Y MINUTOS
#end_datetime = datetime.strptime('2022-03-06 15:00:00', '%Y-%m-%d %H:%M:%S')   #
start_datetime = datetime.strptime('2023-02-02', '%Y-%m-%d')
end_datetime = datetime.strptime('2023-02-13', '%Y-%m-%d')
print(datos.loc[(datos['FECHA APERTURA'] >= start_datetime) & (datos['FECHA APERTURA'] <= end_datetime)])
filtro_fecha=datos.loc[(datos['FECHA APERTURA'] >= start_datetime) & (datos['FECHA APERTURA'] <= end_datetime)]
#print(datos["FECHA APERTURA"].str.findall('^[02/2023].*'))
'''
mask = (datos['FECHA APERTURA'] > '01/02/2023') & (datos['FECHA APERTURA'] <= '20/02/2023')
filtered_df=datos.loc[mask]
print(filtered_df)
'''

#----MOSTRANDO LA TABLA COMPLETA----
filas=datos.iloc[:]
#print(filas)
#----CANTIDAD DE FILAS----
nfilas=int(len(datos))
#print(nfilas)
#----LAS COLUMNAS EXISTENTES----
#print(datos.columns)

#----MOSTRANDO LAS PRIMERAS TRES FILAS DE LA TABLA----
#print(filas.iloc[0:3])


#CREAR DATA FRAME Y MOSTRAR COLUMNAS
#df=pd.DataFrame(filas)#se crea el data frame directo de lo que se lee del excel
df=pd.DataFrame(datos.loc[(datos['FECHA APERTURA'] >= start_datetime) & (datos['FECHA APERTURA'] <= end_datetime)])#se crea data frame con lo filtrado en fecha
print(df.loc[:,('TICKET','AUTOR DE SOLICITUD','CATEGORIA','SUBCATEGORIA','ASUNTO','DESCRIPCION','FECHA APERTURA','FECHA SOLUCION','ESTADO')])#se muestran solo unas columnas

#FILTRANDO CATEGORIAS
#despliegue = df[df['CATEGORIA']=='SERVICIO DE CNC.DESPLIEGUE DE PAQUETES DESARROLLO']
# #print("categorias")
#print(df[df['CATEGORIA'].isin(['SERVICIO DE CNC.DESPLIEGUE DE PAQUETES DESARROLLO'])])


#CREANDO NUEVO DATAFRAME con solo unas columnas, para el reporte con las columnas
reporte = pd.DataFrame(df.loc[:,('TICKET','AUTOR DE SOLICITUD','CATEGORIA','SUBCATEGORIA','ASUNTO','DESCRIPCION','FECHA APERTURA','FECHA SOLUCION','ESTADO')])


#ESCRIBIR EN EXCEL
escritor = pd.ExcelWriter(r'C:\Users\uri\Desktop\Curso_Python\PROYECT_ETE\REPORT_EXCEL\prueba.',engine='xlsxwriter')
#index=false quita la columna adicional que crea pandas, startcol y startrow para indicar la fila y columna donde se pegaran.
reporte.to_excel(escritor, sheet_name='copia',startcol=1,startrow=15,index=False)

#INSERTAR FORMULA
'''
formula=pd.DataFrame(pd.Series(['=EXTRAE(D5,1,ENCONTRAR(".",D5,1)-1)','hola']))
print(formula.iloc[:])
formula.to_excel(escritor, sheet_name='copia',startcol=9,startrow=4,index=False,header=False)
'''
                                                                            
#GUARDAR ARCHIVO
escritor.save()
escritor.close()
print("data entered successfully")



#SE LEE EL NUEVO ARCHIVO EXCEL   insertar formula
'''
AN_excel = load_workbook('REPORTE INCI2.xlsx')
pestaña = AN_excel['copia']
#INTRODUCIR NUEVAS FORMULAS
pestaña['J5'] = '=EXTRAE(D5,1,ENCONTRAR(".",D5,1)-1)'

AN_excel.save('REPORTE INCI2.xlsx')
'''