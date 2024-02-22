from django.contrib import admin

from grando.models import Cursos,Alumnos,Profesores,Entregas
# Register your models here.

admin.site.register(Cursos)
admin.site.register(Alumnos)
admin.site.register(Profesores)
admin.site.register(Entregas)