from django.shortcuts import render, redirect
from .models import *
from .forms import NedviznostiForm


# Create your views here.
def index(request):
    nedviznosti = Nedviznost.objects.filter(dali_e_prodadena=False, povrsina__gt=100)
    context = {'nedviznosti': nedviznosti}
    return render(request, 'index.html', context)


def edit(request, id):
    nedviznost = Nedviznost.objects.get(id=id)
    karakteristiki = Karakteristika.objects.all()
    if request.method == 'POST':
        form = NedviznostiForm(request.POST, request.FILES, instance=nedviznost)
        if form.is_valid():
            form.save()
            return redirect('index')
        return None
    else:
        form = NedviznostiForm(instance=nedviznost)
    context = {'nedviznost': nedviznost, 'form': form, 'site_karakteristiki': karakteristiki}
    return render(request, 'edit.html', context)
