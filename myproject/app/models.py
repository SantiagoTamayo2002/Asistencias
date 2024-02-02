from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    numero_cedula = models.CharField(max_length=20)


class Estudiante(Persona):
    def responder_lista(self):
        # Implementa el comportamiento deseado al responder a la lista
        return f"{self.nombre} {self.apellido} está respondiendo a la lista."
    

class Docente(Persona):
    def tomar_lista(self):
        # Implementa el comportamiento deseado al tomar la lista
        return f"{self.nombre} {self.apellido} está tomando la lista."

