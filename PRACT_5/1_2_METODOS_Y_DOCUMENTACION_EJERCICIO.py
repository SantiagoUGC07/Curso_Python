#Elimina los caracteres a la izquierda de nuestro texto principal
#",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"

texto = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(",:%_#")
texto= texto.rstrip(',:#')
print(texto)
print((',:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#').lstrip(",:%_#"))

#Añade el elemento "naranja" como el cuarto elemento de la sig lista "frutas"
#utilizando el metodo insert()int
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3, 'naranja')
print(frutas)

#Verifica si los sets a continuacion forman conjuntos aisalados (es decir, que no tienen
#elementos en comun utilizando el metodo isdisjoint(). Almacena dicho resultado en la variable
#conjuntos_aislados
marcas_smartphones ={"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
conjuntos_aislados = marcas_tv.isdisjoint(marcas_smartphones)
print(conjuntos_aislados)
