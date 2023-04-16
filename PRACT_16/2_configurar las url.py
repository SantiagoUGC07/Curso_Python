'''
******** PARA CONECTAR EL SERVIDOR A LA CARPETA APPS***************
1.- abrir la carpeta proyecto que se encuentra dentro de la sig ruta
    C:\Users\uri\Desktop\Curso_Python\PRACT_16\mi_web\src\proyecto
2.- una vez ahi abrir la terminalen pycharm yendo a la barra de tareas en:
    view->tool windows->terminal
3.- insertar el sig comando en la terminal, para crear una app en el sitio web. se crea una carpeta con el nombre de base
    python manage.py startapp base
4.- luego correr el servidor
    python manage.py runserver
5.- para conectar la app (carpeta base) al proyecto donde esta el server. nos dirigimos al archivo settings.py que esta en la carpeta proyecto.
    en el apartado installed apps colocamos la direccion de la carpeta(base).apps(nombre de la clase que se encuentra la carpeta base en el archivo apps.py)
    se coloca al final de los demas
    INSTALLED_APPS = [
        .
        .
        'base.apps.BaseConfig',
    ]
********************CONECTAR LAS URL******************
6.- ahora para conectar las url. primero crear un archivo (urls.py) en la carpeta (base), y importar las vistas para configurarlas
    Ingresar las sig. lineas de codigo
    from django.urls import path
    from . import views
    #se llama la funcion lista_penditentes dentro de views, que se generara en views.py
    urlpatterns = [path('', views.lista_pendientes, name='pendientes')]#se coloca '' un espacio bacio para buscar en la carpeta destino

7.- en el archivo views.py que esta en la carpeta base ingresar, para conectar las url con la vistas
    from django.http import HttpResponse
    # Create your views here.
    def lista_pendientes(pedido):
        return HttpResponse('Lista de pendientes')

8.- par acontinuar en el archivo (urls.py) que esta en la carpeta proyecto ingresar la libreria include (from django.urls import path, include) 
    y la linea "path('',include('base.urls'))," dentro del apartado url patterns, quedaria algo asi. el metodo include agregara el archivo .py y en el
    apartado urlpatterns con la linea que se agrego se llama al achivo urls.py asi podemos manejar los archivos de la carpeta base desde la carpeta proyecto-

    from django.contrib import admin
    from django.urls import path, include
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('',include('base.urls')),
    ]
*************************GENERAR TABLAS Y CONEXION A DB***********************
9.- las tablas se generan en el archivo models.py, aqui generamos la tabla de usuario, agregamos una libreria y luego el usuario
    from django.contrib.auth.models import User
    class Tarea(models.Model):
    usuario = models.ForeignKey(User, #lo usurios puden modificar las tareas, esto es una relacion de uno a varios, foreingkey es una clave externa, y podemos asociar diferentes registros a usuarios que se repita.
    #ese mismo usuario tendra la misma clave para las diferentes tareas que genere.
                                on_delete=models.CASCADE(),#sirve para eliminar las tareas que genero el usuario, cuando el usuario se elimine
                                null=True, #el usuario puede estar vacioa
                                blank=True #un registro puede estar vacio
                                )
    titulo = models.CharField(max_length=200)# el maximo de los caractes
    descripcion = models.TextField(null=True, #el usuario puede estar vacioa
                                blank=True)#un registro puede estar vacio
    completo = models.BooleanField(default=False)#para las tareas el campo este no completo
    creado = models.DateTimeField(auto_now_add=True)#para generar la hora y fecha de la creacion de la tarea
    def __str__(self):
        return self.titulo#si pedimos que se imprima una tarea, se imprime el titulo de la tarea
    class Meta:
        ordering = ['completo']
*******************************PARA MIGRAR LAS TABLAS AL SERV.***********************************
10.- para migrar las tablas a la base de datos se abre la terminal en la carpeta proyecto yendo a view->tool windows->terminal 
    y se inserta el comando. lo que generara una carpeta llamada migrations, con un archivo con el nombre 0001.initial.py con los atributos que generamos en el paso 9
    python manage.py makemigrations
11.- ahora para migrar la tabla al sitio se ejecuta el comando en la terminal en la carpeta proyecto yendo a view->tool windows->terminal
    python manage.py migrate
12.- para visualizar en servidor ir al archivo admin.py que esta en la carpeta base, y colocar los siguientes comandos, que sirven
    para registrar las tablas en el admin y asi poderlos visualizar.
    from .models import Tarea
    # Register your models here.
    admin.site.register(Tarea)#se llama a la tarea que se encuenta en models.py
13.-  correr el servidor en la terminal con el comando. y yendo a view->tool windows->terminal
    python manage.py runserver
14.- para visualizar usuar el siguiente url del admin
    http://127.0.0.1:8000/admin/
*****************************************CONFIGURAR LAS VISTAS************************************
'''