
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('inscription/', inscription,name="inscription"),
    path('connexion/',connexion,name="connexion"),
    path("deconnexion/", deconnexion,name="deconnexion"),
    path("profile",profile,name="profile"),
    path('list',liste_utilisateurs,name="liste_utilisateurs"),
    path("sendmail/",sendmail, name="sendmail"),
    path("infouser/",infouser,name='infouser'),

]
