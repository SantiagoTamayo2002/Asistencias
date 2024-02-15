from django.contrib import admin
from django.urls import path
from .views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('estudiante/', estudiante, name="estudiante"),
    path('docente/', docente, name="docente"),
    path('tomarLista/', tomar_asistencia, name="tomarLista"),
    path('curso/', tomar_asistencia, name="paralelos"),
]