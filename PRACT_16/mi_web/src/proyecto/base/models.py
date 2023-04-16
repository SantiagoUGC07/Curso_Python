from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tarea(models.Model):
    usuario = models.ForeignKey(User, #lo usurios puden modificar las tareas, esto es una relacion de uno a varios, foreingkey es una clave externa, y podemos asociar diferentes registros a usuarios que se repita.
    #ese mismo usuario tendra la misma clave para las diferentes tareas que genere.
                                on_delete=models.CASCADE,#sirve para eliminar las tareas que genero el usuario, cuando el usuario se elimine
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


