from django.db import models

class Usuario(models.Model):
    Nombre = models.CharField(max_length=45)
    Edad = models.IntegerField()
    Genero = models.CharField(max_length=10)
    Preferencias_Contenido = models.CharField(max_length=45)
    Correo_Electronico = models.EmailField()
    Password = models.CharField(max_length=45)

    def __str__(self):
        return self.Nombre
