from django.urls import path
from grando import views
from .views import index,cursos,alumnos,profesores,formulario,alumnonuevo,profesornuevo,buscar

urlpatterns = [
    path("", views.index, name="index"),
    path("cursos/", views.cursos, name="cursos"),
    path("alumnos/", views.alumnos, name="alumnos"),
    path("profesores/", views.profesores, name="profesores"),
    path("cursonuevo/", views.formulario, name="formulario"),
    path("alumnonuevo/", views.alumnonuevo, name="alumnonuevo"),
    path("profesornuevo/", views.profesornuevo, name="profesornuevo"),
    path("busqueda/", views.busqueda, name="busqueda"),
    path("buscar/", views.buscar, name="buscar")
    

]