from errno import EDEADLK
from django.db import models
from django.forms import CharField

# Create your models here.
class Familias(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    ciudad = models.CharField(max_length=50)