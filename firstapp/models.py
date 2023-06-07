from django.db import models
from django.db import connection

# Create your models here.

class Person(models.Model): #одна модель-одна таблица. #makemigrations - создать модель, migrate - создать таблицу

    name = models.CharField(max_length=20)
    age = models.IntegerField()
    objects = models.Manager()