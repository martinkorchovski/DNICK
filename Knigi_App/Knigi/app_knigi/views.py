from django.shortcuts import render, redirect

from .forms import KnigaForm
from .models import *

# Create your views here.
def index(request):
    knigi = Kniga.objects.all()
    context = {'knigi': knigi}
    return render(request, 'index.html', context)

def edit(request, id):
    kniga = Kniga.objects.get(id=id)
    if request.method == 'POST':
        form = KnigaForm(request.POST, instance=kniga)
        if form.is_valid():
            form.save()
            return redirect('index')
        return None
    else:
        form = KnigaForm(instance=kniga)
    context = {'form': form, 'kniga': kniga}
    return render(request, 'edit.html', context)
