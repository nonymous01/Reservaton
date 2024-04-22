from django.shortcuts import render,redirect
from .form import AuthUser
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import Utilisateur
from django.core.mail import send_mail


def sendmail(request):
    send_mail(
        "Anonymous",
        "Here is the message.",
        "pct.anonymous0@gmail.com",
        ["13159596youssef@gmail.com"],
        fail_silently=False,
    )
    return HttpResponse("success")
def sendmfail(request):
    subject = 'Sujet de l\'e-mail'
    message = 'Contenu de l\'e-mail'
    sender_email = 'pct.anonymous0@gmail.com'
    recipient_list = ['13159596youssef@gmail.com']

    send_mail(subject, message, sender_email, recipient_list)
def inscription(request):
    if request.method == 'POST':
        form = AuthUser(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.email = form.cleaned_data['email']
            user = form.save()
            print(f"Utilisateur créé : nom: {user.username} password :{user.password} email: {user.email}")
            return redirect ('connexion')
    else:
        form = AuthUser()
    return render(request, 'auth_app/inscription.html', {'form': form})
            
# pour la connexion
def connexion(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user= authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        
        else:
            messages.error(request, "nom ou mot de pass incorect")
    return render(request, 'auth_app/connexion.html')

#pour la deconnexion
@login_required
def deconnexion(request):
    logout(request)
    return redirect('connexion')

@login_required
def profile(request):
    return render(request, 'auth_app/deconnexion.html')


def liste_utilisateurs(request):
    utilisateurs = Utilisateur.objects.all()
    print(utilisateurs)
    return render(request, 'auth_app/listes.html', {'utilisateurs': utilisateurs})

def infouser(request):
    return render(request, 'auth_app/infouser.html')
