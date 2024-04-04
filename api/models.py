from django.db import models

# Create your models here.

class Student(models.model):
    name = models.models.CharField(max_length=50)
    lastname = models.models.CharField(max_length=50)
