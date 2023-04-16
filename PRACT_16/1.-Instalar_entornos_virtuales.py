#ENTORNOS VIRTUALES.
'''
Nos sirven para tener distintas versiones de librerias o modulos
intaladas en diferentes carpetas para proyectos en especifico.

para crear un entorno virtual se requiere instalar virtualenv
abrir CMD como administrador colocar los sig comandos en orden siguiente,
con la nomeclatura (py versionpython -m pip install modulo a instalar)
    py -3.10 -m pip install --upgrade pip
    py -3.10 -m pip install virualenv
    py -3.10 -m pip install --upgrade virtualenv

para visualizar los modulos instalados en python
py -3.10 -m pip freeze

pasos para crear entornos en una carpeta
1.- se crean las carpetas
2.- abrir cmd como administrador
3.- colocarse en la carpeta con comando CD en el CMD  en este caso se usa
    cd  C:\Users\uri\Desktop\Curso_Python\PRACT_16\Mis_entornos\Proyecto_1
4.- dentro de la carpeta en el CMD, usar el comando (py -3.10 -m virtualenv nombredelproyecto)
    py -3.10 -m virtualenv p1
5.- se genera una carpeta con el nombre "p1" donde se encuentra el entorno virtual
6.- para activar el ENV se usa el siguiente comando en el CMD .\nombredelespacio\Scripts\activate
     .\p1\Scripts\activate
7.- se cambia la carpeta y aparece algo como: (p1) C:\Users\uri\Desktop\Curso_Python\PRACT_16\Mis_entornos\Proyecto_1>
8.- ahora para visutalizar los modulos o librerias intalados en la carpeta se usa el comando,
en este caso no se una al inicio py -3.10 -m ya que estamos dentro del entorno virtual y apareceran las librerias de python 3.10
    pip freeze
9.- no aparecera ninguna ya que no se tienen librerias intaladas en este entorno virtual
10.- instalar alguna libreria para revisar usando el comando.
    pip install pyjokes
11.- ahora para visutalizar los modulos o librerias intalados en la carpeta se usa el comando
    pip freeze
12.- ahora si se muestra una libreria instalada. la de pyjokes
13.- repetir los pasos del 1 al 6 pero ahora para crear un entorno virtual en la carpeta Proyecto_2
y en esta instalaremos pyjokes 4.0
14.- para instalar la version de pyjokes 4.0 se usa el sig comando.
    pip install pyjokes==0.4.0
15.- ahora tenemos dos versiones distintas de pyjokes instaladas en las carpetas de p1 y p2
16.- para desactivar un entorno usar el comando en el CMD en este caso dentro de:
(p2) C:\Users\uri\Desktop\Curso_Python\PRACT_16\Mis_entornos\Proyecto_2>
    deactivate
17.- una vez colocado vuelve a aparecer la ruta normal en el CMD.
C:\Users\uri\Desktop\Curso_Python\PRACT_16\Mis_entornos\Proyecto_2>
**************************************************************************************************************
.
AHORA SE REQUIERE CREAR UN ENTORNO VIRTUAL PARA LA WEB E
INSTALAR DJANGO PARA CONTINUAR CON EL PROYECTO DE TAREAS WEB.

1.- Para instalar Django primero crear el ENV de la web en este caso se usaron los sig comando dentro del cmd
    cd C:\Users\uri\Desktop\Curso_Python\PRACT_16\mi_web
    py -3.10 -m virtualenv web
    .\web\Scripts\activate

2.- una vez en (web) C:\Users\uri\Desktop\Curso_Python\PRACT_16\mi_web>
usar el comando
    pip install django
3.- crear desde el cmd una carpeta en la ruta (web) C:\Users\uri\Desktop\Curso_Python\PRACT_16\mi_web>
con el siguiente comando. se le colocara src que es source y es para las rutas
    mkdir src
4.- entrar a la carptera src con el sig comando
    cd src
5.- dentro de la carpeta src crear el proyecto con el sig. comando. django-admin startproject nombreproyecto
     django-admin startproject proyecto
6.- dentro de la carpeta src se creara un archivo llamado manage.py que es donde se administra todo
7.- ingresar a la carpeta proyecto con el sig. comando, para indicar el servidor donde se ejecutara el programa.
    cd proyecto
8.- para correr el servidor usar el siguiente comando. dentro de la carpeta proyecto
    python manage.py runserver
9.- ahora se genera un archivo dentro de la carpeta db.sqlite3 y en CMD pide aplicar las migraciones para el proyecto
asi como la url donde se ejecutara el sitio web localmente. que es la sig. y si se coloca en el navegador se muestra.
    http://127.0.0.1:8000/
10.- para salir de la ejecucion del servidor usar CTRL + C y generar la migracion del aplicativo en el CMD
11.- para generar la migracion de los archivos pendientes se usa el siguiente comando
    python manage.py migrate
12.- ahora correr el servidor con el comando para visualizar por medio de los links
    python manage.py runserver
13.- ahora podemos ejecutar el servidor con la barra admin para ingresar con el usuario y pass
    http://127.0.0.1:8000/admin
14.- para generar el usuario y pass se hace desde la consola usar CTRL + C para salir de la ejecucion y usar el sig
comando para el usuario y pass
    python manage.py createsuperuser
15.- te pedira llenar unos datos
    usuario: uriel
    email address: se puede dejar en blanco
    password: Wer&
16.- volver a correr el server para visualizarlo por medio del link
    python manage.py runserver
17.- 13.- ahora podemos ejecutar el servidor e insertar nuestro usuario y pass
    http://127.0.0.1:8000/admin
18.- dentro del admin se pueden administrar los usuarios y otras configuraciones.
'''

