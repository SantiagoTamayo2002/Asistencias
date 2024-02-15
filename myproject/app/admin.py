from django.contrib import admin
from .models import Persona, Docente, Estudiante

# Register your models here.
admin.site.register(Persona)
admin.site.register(Docente)
admin.site.register(Estudiante)
