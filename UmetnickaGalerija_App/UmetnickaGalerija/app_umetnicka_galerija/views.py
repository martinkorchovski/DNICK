from django.shortcuts import render, redirect

from .forms import IzlozbaForm
from .models import *

# Create your views here.
def index(request):
    izlozbi = Izlozba.objects.all()
    for izlozba in izlozbi:
        izlozba.slika = izlozba.umetnickodelo_set.first()
    context = {'izlozbi': izlozbi}
    return render(request, 'index.html', context)

def add(request):
    if request.method == "POST":
        form = IzlozbaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = IzlozbaForm()
    context = {'form': form}
    return render(request, 'add.html', context)