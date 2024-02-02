from django.shortcuts import render
from .models import Estudiante, Docente

def ejemplo_vista(request):
    # Crear una instancia de Estudiante
    estudiante = Estudiante(nombre='Juan', apellido='Pérez', numero_cedula='123456789')
    respuesta_estudiante = estudiante.responder_lista()

    # Crear una instancia de Docente
    docente = Docente(nombre='Profesor', apellido='Gómez', numero_cedula='987654321')
    respuesta_docente = docente.tomar_lista()

    return render(request, 'app/home.html', {'respuesta_estudiante': respuesta_estudiante, 'respuesta_docente': respuesta_docente})
