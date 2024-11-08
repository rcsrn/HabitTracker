from django.shortcuts import render
from django.contrib.auth.views import LoginView , LogoutView
from .forms import CustomLoginForm
# forms registro
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.views.generic import CreateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages


class CustomLoginView(LoginView):
    template_name = 'login.html' 
    form=CustomLoginForm
    
    # Si ingresan datos incorrectos, mandamos un mensaje de error
    def form_invalid(self, form):
        messages.error(self.request, "Nombre de usuario o contraseña incorrectos.")
        return super().form_invalid(form)


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return render(request, 'home.html')

def home(request):
    if request.user.is_authenticated:
        usuario = request.user
        contexto = {'usuario': usuario}
        return render(request, 'home.html', contexto)
    else:
        return render(request, 'home.html')

def habito(request):
    if request.user.is_authenticated:
        usuario = request.user
        contexto = {'usuario': usuario}
        return render(request, 'habito.html', contexto)
    else:
     return render(request, 'home.html')

class registro(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = "registro.html"

    def form_valid(self, form):
        '''
        En esta parte, si el form es valido lo guardamos y usamos authenticate e iniciamos sesión
        '''
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario,password=password)
        login(self.request, usuario)
        return redirect('/')
