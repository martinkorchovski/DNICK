from django.shortcuts import render, redirect

from .forms import TortaForm
from .models import *

# Create your views here.
def index(request):
    torti = Torta.objects.all()
    context = {'torti': torti}
    return render(request, 'index.html', context)

def add(request):
    if request.method == 'POST':
        form = TortaForm(request.POST, request.FILES)
        if form.is_valid():
            torta = form.save(commit=False)
            torta.pekar = Pekar.objects.get(user=request.user)
            torta.save()
            return redirect('index')
    form = TortaForm()
    context = {'form': form}
    return render(request, 'add.html', context)