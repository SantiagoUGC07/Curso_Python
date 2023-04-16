import unittest
import ModuloUnittest

class ProbarCambiaTexto(unittest.TestCase):#esta clase va a heredar las funciones de unittest
    def test_mayusculas(self):#la funcion debe contener al inicio nombre de test para funcionar
        palabra = 'buen dia'#esta palabra sera la que usemos para ver como funciona en ModuloUnittest
        resultado = ModuloUnittest.todo_Mayusculas(palabra)#llamamos al ModuloUnittest Y SU FUNCION todo_Mayusculas
        self.assertEqual(resultado, 'BUEN DIA')
        '''
        assertEqual: sirve para comprobar el resultado por el valor deseado en este caso 'BUEN DIA'
        '''
if __name__ == '__main__':#todos lo programas tienen una funcion main(principal) y comienza con esa funcion
    unittest.main()#python no tiene funcion main por eso se coloca esto, para proteger el codigo.

'''
LA PRUEBA DA OK
'''

''' 
en caso que sean distintos aparecen asi
AssertionError: 'BUEN DIA' != 'buen dia'
- BUEN DIA
+ buen dia
'''