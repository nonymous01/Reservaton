from django import forms
from django.contrib.auth.hashers import make_password
from .models import Utilisateur

class SingUpForm(forms.ModelForm):
    class Meta:
        model=Utilisateur
        fields=['username', 'email', 'telephone', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Nom d’utilisateur'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'telephone': forms.NumberInput(attrs={'placeholder': 'Téléphone'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}),
        }

        def save(self, commit=False):
            user= super().save(commit=False)
            user.password= make_password(self.cleaned_data["password"])
            if commit:
                user.save()
            return user
        
class ConnexionForm(forms.ModelForm):
    class Meta:
        model=Utilisateur
        fields=['email', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}),
        }

        def save(self, commit=False):
            user= super().save(commit=False)
            user.password= make_password(self.cleaned_data["password"])
            if commit:
                user.save()
            return user