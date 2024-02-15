from django.urls import path
from app.views import home, estudiante, docente, tomar_asistencia

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('estudiantes/', estudiante, name="estudiantes"),
    path('profesores/', docente, name="profesores"),
    path('tomarLista/', tomar_asistencia, name="tomarLista"),
    path('curso/', tomar_asistencia, name="paralelos"),

    
]
