from django.shortcuts import render, redirect

from .forms import PatuvanjaForm
from .models import *


# Create your views here.
def index(request):
    patuvanja = Patuvanje.objects.all()
    context = {'patuvanja': patuvanja}
    return render(request, 'index.html', context)


def add(request):
    if request.method == "POST":
        form = PatuvanjaForm(request.POST, request.FILES)
        if form.is_valid():
            patuvanje = form.save(commit=False)
            patuvanje.vodic = TuristickiVodic.objects.get(user=request.user)
            patuvanje.save()
            return redirect('index')
    form = PatuvanjaForm()
    context = {'form': form}
    return render(request, 'add.html', context)