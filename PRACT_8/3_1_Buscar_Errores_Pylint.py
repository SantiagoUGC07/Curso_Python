#Se tiene dos BIBLIOTECAS
#Pylint
#unittest
'''
pylint: analiza el codigo e informa sobre posibles problemas, problemas de estilo o algun codigo no valido

unittest: te permite probar los programas y verificar si se obtienen los resultados deseados

nota: python tiene un conjunto de reglas de convencion de estilo que se tiene por la sig nomenclatura
estilo = PEP-8
'''
#se debe instalar pylint por cmd con pip install pylint
'''
ya que desde ahi se revisan los problemas con pylint
y ingresar en cmd el sig comando. que nos lleva a donde esta el actual archivo
    cd C:\Users\uri\Desktop\Curso_Python\PRACT_8
luego el sig comando que contine el nombre del archivo actual y -r(reporte) y(yes)
    pylint 3_1_Buscar_Errores_Pylint.py -r y
Nos mostrara los errores estructurales del codigo.

NOTA:
para instalar librerias que MARCAN ERROR cmd 
METODO 1
agrgar en variables de entorno, la ruta donde se encuentra python y python scripts, con algun nombre para cada una
    C:\Users\uri\AppData\Local\Programs\Python\Python310
    C:\Users\uri\AppData\Local\Programs\Python\Python310\Scripts
luego usar el comando, intentar instalar en el usuario no en el administrador
     python -m pip install nombre_libreria
METODO 2
si no se puede importarla en un archivo aqui
        import pylint
click secundario sobre pylint que se mostrara en rojo y luego instalar libreria
luego abrir CMD y ejecutar el comando
    pip install pylint        
'''
numero1 = 500
print(Numero1)
