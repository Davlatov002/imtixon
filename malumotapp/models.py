from django.db import models

# Create your models here.

class Malumot(models.Model):
    nomi = models.CharField(max_length=250)
    malumot = models.TextField()
    
