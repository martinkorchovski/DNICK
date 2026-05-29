from django.shortcuts import render, redirect

from .forms import NastanForm
from .models import *


# Create your views here.
def index(request):
    nastani = Nastan.objects.filter(user=request.user)
    context = {'nastani': nastani}
    return render(request, 'index.html', context)


def add(request):
    if request.method == "POST":
        form = NastanForm(request.POST, request.FILES)
        if form.is_valid():
            nastan = form.save(commit=False)
            nastan.user = request.user
            nastan.save()

            bendovi_str = request.POST.get('bendovi', '')
            band_names = [b.strip() for b in bendovi_str.split(',')]
            for band_name in band_names:
                bend = Bend.objects.filter(ime__iexact=band_name).first()
                if bend:
                    nastan.bendovi.add(bend)
            return redirect('index')
    form = NastanForm()
    context = {'form': form}
    return render(request, 'add.html', context)
