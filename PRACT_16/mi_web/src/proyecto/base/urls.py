from django.urls import path
from . import views
#se llama la funcion lista_penditentes dentro de views, que se genero en views.py
urlpatterns = [path('', views.lista_pendientes, name='pendientes')]#se coloca '' un espacio bacio para buscar en la carpeta destino

