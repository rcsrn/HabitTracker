from django import forms
from django.contrib.auth.forms import AuthenticationForm
# registro
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    appellido
    descripcion

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user
