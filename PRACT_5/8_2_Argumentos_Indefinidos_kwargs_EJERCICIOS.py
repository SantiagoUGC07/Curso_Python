#1.-EJERCICIO crea una funcion llamada cantidad_atributos que cuente la cantidad de parametros que se entregan y devuelva
# esa cantidad como resultado
print("1.-EJERCICIO")
def cantidad_atributos(**kwargs):
    n=0
    for clave,valor in kwargs.items():
        n+=1
    return n
print(cantidad_atributos(a=2,b=3,c=4))
#
#2.-Crea una funcion lladama lista_atributos que devuelva en forma de lista los valores de los atributos
#entregados en forma de palabras clave keywords. la funcion debe preveer recibir cualquier cantidad de argumentos
# de este tipo
print("\n2.-EJERCICIO")
def lista_atributos(**kwargs):
    lista=[]
    for clave,valor in kwargs.items():
        lista.append(valor)
    return(lista)
lista=lista_atributos(a=1,b=4,c=5,d=4,e=6,f=5)
print(lista)

#3.-EJERCICIO crea una funcion llamada describir_persona, que tome como parametros su nombre y luego una cantidad indeterminada
# de arguentos. esta funcion debera mostrar en pantalla.
# caracteristicas de {nombre}....
# {nombre_argumento} : {valor_argumento}
# {nombre_argumento} : {valor_argumento}
# describir_persona("María", color_ojos="azules", color_pelo="rubio")
# Mostrar en pantalla
# Características de María:
# color_ojos: azules
# color_pelo: rubio
print("\n3.-EJERCICIO")
def describir_persona(nombre,**kwargs):
    print(f"caracteristicas de {nombre}")
    for clave,valor in kwargs.items():
        print(f"{clave} : {valor}")
kwargs={"color_ojos":"Azules","color_pelo":"Rubio"}
describir_persona("Santiago",**kwargs)
