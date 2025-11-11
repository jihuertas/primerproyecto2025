from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=60)
    edad = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self) -> str:
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE)
    cuerpo = models.TextField()

    def __str__(self) -> str:
        return f"({self.id}) {self.titulo}"



