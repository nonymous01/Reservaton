from django.db import models


class Utilisateur(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(default="youssef@gmail.com",unique=True)
    password = models.CharField(max_length=100)


class Client(models.Model):
    class Alergies(models.TextChoices):
        ALIMENTAIRES = 'alimentaires', 'Alimentaires'
        ANIMAL = 'animal', 'Animal'
    user= models.ForeignKey(Utilisateur,on_delete=models.CASCADE,default=None)
    first_name=models.CharField(max_length=100, blank=False)
    last_name=models.CharField(max_length=100, blank=False)
    ncni=models.CharField(max_length=100,blank=False, null=True)
    alergie = models.CharField(max_length=20, choices=Alergies.choices, blank=True)
    Toute_demande= models.CharField(max_length=500,blank=False, null=True)
    telephone= models.CharField(max_length=100,blank=False, null=True)
    Nombre_de_personnes= models.IntegerField(blank=False, null=True)
    status= models.BooleanField(default=False,blank=False)



    