#1- Llamando funciones de un modulo a otro
from ModuloOcupado import Saludar#aqui estamos llamando a la funcion saludar que esta dentro de modulo ocupado
#para importar un modulo no debe tener caracter especial en el nombre o numeros
#si se requiere llamar a todos los modulos en vez de escribir import saludar se coloca import *
Saludar()#se manda a llamar a la funcion de modulo ocupado

#2.- para abrir desde el CMD un modulo.py
'''
dirigete a la carpeta donde se encuentra ModuloVacio usando el comando cd 
una vez en la ubicacion escribe lo siguiente
python ModuloVacio.py
enter y se mostrara el texto de ModuloOcupado.
'''