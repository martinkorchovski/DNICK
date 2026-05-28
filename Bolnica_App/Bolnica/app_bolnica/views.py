from django.shortcuts import render, redirect
from .models import *
from django.utils import timezone
# from datetime import date
from .forms import PregledForm


# Create your views here.
def index(request):
    kardiolozi = Lekar.objects.filter(specijalnost='kardiolog')
    dermatolozi = Lekar.objects.filter(specijalnost='dermatolog')
    nevrolozi = Lekar.objects.filter(specijalnost='nevrolog')

    context = {
        'kardiolozi': kardiolozi,
        'dermatolozi': dermatolozi,
        'nevrolozi': nevrolozi,
    }

    return render(request, 'index.html', context)


def lekar_profil(request, id):
    lekar = Lekar.objects.get(id=id)

    denes = timezone.now()
    pregledi = Pregled.objects.filter(glaven_lekar=lekar)
    pacieti = Pacient.objects.all()

    minati_pregledi = pregledi.filter(termin__date__lt=denes.date())
    denesni_pregledi = pregledi.filter(termin__date=denes.date())
    idni_pregledi = pregledi.filter(termin__date__gt=denes.date())

    form = PregledForm()

    if request.method == 'POST':
        form = PregledForm(request.POST)
        if form.is_valid():
            pregled = form.save(commit=False)
            pregled.glaven_lekar = lekar
            pregled.tip = lekar.specijalnost
            pregled.save()
            return redirect('lekar', id=id)

    context = {
        'lekar': lekar,
        'minati_pregledi': minati_pregledi,
        'denesni_pregledi': denesni_pregledi,
        'idni_pregledi': idni_pregledi,
        'form': form,
        'pacienti': pacieti,
    }
    return render(request, 'lekar_profil.html', context)
