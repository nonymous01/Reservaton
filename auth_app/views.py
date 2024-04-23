from django.contrib import messages
from django.shortcuts import render, redirect
from .form import SingUpForm,ConnexionForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .models import Utilisateur
def inscription(request):
    if request.method=="POST":
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Inscription réussie. Veuillez vous connecter.")
            return redirect('connexion')
    else:
        form= SingUpForm()
    return render(request,"auth_app/inscription.html",{"form":form})



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .form import ConnexionForm

def connexion(request):
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse("home")  # Redirigez vers la page d'accueil après la connexion
    else:
        form = ConnexionForm()
    return render(request, "auth_app/connexion.html", {"form": form})
