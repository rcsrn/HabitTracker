from django.shortcuts import render
from django.contrib.auth.views import LoginView , LogoutView
from .forms import CustomLoginForm
# forms registro
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm


class CustomLoginView(LoginView):
    template_name = 'login.html' 
    form=CustomLoginForm
class CustomLogoutView(LogoutView):
    next_page = 'home'

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('home') 
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form': form})
