from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Client(models.Model):
    class Alergies(models.TextChoices):
        ALIMENTAIRES = 'alimentaires', 'Alimentaires'
        ANIMAL = 'animal', 'Animal'
    user= models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    ncni=models.CharField(max_length=100,blank=False, null=True)
    alergie = models.CharField(max_length=20, choices=Alergies.choices, blank=True)
    Toute_demande= models.CharField(max_length=500,blank=False, null=True)
    telephone= models.CharField(max_length=100,blank=False, null=True)
    Nombre_de_personnes= models.IntegerField(blank=False, null=True)
    status= models.BooleanField(default=False,blank=False)


class Utilisateur(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(default="youssef@gmail.com",unique=True)
    password = models.CharField(max_length=100)

