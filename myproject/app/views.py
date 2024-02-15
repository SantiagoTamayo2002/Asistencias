from django.shortcuts import render
from .models import Estudiante, Docente


def home(request):
    return render(request, 'app/home/home.html')

def estudiante(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'app/home/estudiantes.html', {'estudiantes': estudiantes})

def docente(request):
    docentes = Docente.objects.all()
    return render(request, 'app/home/profesores.html', {'docentes': docentes})

def tomar_asistencia(request):
    estudiantes = Estudiante.objects.all()
    docente = Docente.objects.first()  # Obtén el primer docente, puedes modificar esto según tus necesidades
    context = {
        'estudiantes': estudiantes,
        'docente': docente,
    }
    return render(request, 'app/home/tomarLista.html' , context)

def curso(request):
    return render(request, 'app/home/paralelos.html')






