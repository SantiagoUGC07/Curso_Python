#ARGUMENTOS INDEFINIDOS **kwargs
#**kwargs = se puede ocupar otra palabra en vez de kwargs como **gato mientras se tengan los asteriscos
#Los kwargs nos sirven para recibir tantos argumentos como queramos, con la funcion adicional de darles un nombre
#como a=b asi nombrando a "b" como "a"
#1.-INTRODUCCION
def suma(**kwargs):#recibe los datos los nombra y los cambia de tipo de dato
    print(type(kwargs))#es un tipo de dato dic o bien diccionario
suma(x=3, y=5, z=2)

print("Ejemplo")#recibiendo variables kwargs
def suma2(**kwargs):
    total=0
    for clave,value in kwargs.items():#el .items es debido a que son diccionarios, y asi acceder a sus valores
        print(f"{clave} = {value}")#se imprimen los valores y las claves
        total+=value
    return total
print(suma2(x=3, y=5, z=2))

print("Ejemplo 2") #PARA RECIBIR OTRAS VARIABLES
def suma3(num1,num2,*args,**kwargs):#este es el orden correcto para recibir las variables
    print(f"el primer valor es {num1}:")#se imprimen los valores int
    print(f"el segundo valor es {num2}:")
    for arg in args:
        print(f"arg es igual a {arg}")#se imprimen los args
    for clave,value in kwargs.items():
        print(f"{clave} = {value}")#se imprimen los kwargs

args=[100,200,323,233]#otra forma de enviar los args
kwargs={"x":"uno","y":"dos","z":"tres"}#otra forma de enviar los kwargs
suma3(15,50,*args,**kwargs)#la forma correcta de enviar los datos