from django.db import models

# Create your models here.

class Smell(models.Model):
    smell = models.CharField(max_length=50)
    updated_datetime = models.DateField()