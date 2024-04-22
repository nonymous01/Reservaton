from  django import forms
from django.contrib.auth.forms import UserCreationForm


class AuthUser(UserCreationForm):
    email = forms.EmailField(
        label="entrer un e-mail",
        required=True,
        widget=forms.TextInput(attrs={'autocomplete': 'email'}),
        #help_text="Required. 150 characters or fewer. Lettersand @/./+/-/_ only.",
    )
    password1 = forms.CharField(
        label="entrer un mot de passe",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}), 
    )

    password2 = forms.CharField(
        label="confirmation de mot de passe",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}), 
    )
#class meta pour personnaliser les chants du formulaire
    class Meta(UserCreationForm.Meta):
        fields=UserCreationForm.Meta.fields +("password1","password2")


    def __init__(self, *args, **kwargs):
        super(AuthUser, self).__init__(*args, **kwargs)
        # Ajoutez le placeholder pour chaque champ ici
        self.fields['username'].widget.attrs['placeholder'] = 'Nom d\'utilisateur'
        self.fields['password1'].widget.attrs['placeholder'] = 'Mot de passe'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmer le mot de passe'
        self.fields['email'].widget.attrs['placeholder'] = 'Adresse e-mail'
