from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import HabitForm

def crear_habito(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habito = form.save(commit=False)
            habito.id_usuario = request.user  # Asocia el hábito al usuario actual
            habito.save()
            return redirect('dashboard')  
    else:
        form = HabitForm()
    return render(request, 'crear_habito.html', {'form': form})

def dashboard (request):
    pass