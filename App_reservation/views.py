from django.shortcuts import render,redirect
from .form import AuthUser
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import Utilisateur



def register(request):
    if request.method == 'POST':
        form = AuthUser(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.email = form.cleaned_data['email']
            user = form.save()
            print(f"Utilisateur créé : nom: {user.username} password :{user.password} email: {user.email}")
            return redirect ('logins')
    else:
        form = AuthUser()
    return render(request, 'register.html', {'form': form})
            
# pour la connexion
def logins(request):
    if request.method == 'POST':
        username = request.POST["email"]
        password = request.POST["password"]
        print("email",username, "password", password)
        user= authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, "email ou mot de pass incorect")
    return render(request, 'login.html')

#pour la deconnexion
@login_required
def deconnexion(request):
    logout(request)
    return redirect('connexion')

# @login_required
# def profile(request):
#     return render(request, 'deconnexion.html')


def liste_utilisateurs(request):
    utilisateurs = Utilisateur.objects.all()
    print(utilisateurs)
    return render(request, 'auth_app/listes.html', {'utilisateurs': utilisateurs})

def infouser(request):
    return render(request, 'auth_app/infouser.html')