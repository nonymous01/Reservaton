from django.urls import path
from django.contrib import admin
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',register, name="register"),
    path('logins/',logins,name="logins"),
    path("infouser/",infouser,name='infouser'),
]
