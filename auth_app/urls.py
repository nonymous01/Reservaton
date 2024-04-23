from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path("inscription/",inscription,name="inscription"),
    path('connexion',connexion,name="connexion")
]
