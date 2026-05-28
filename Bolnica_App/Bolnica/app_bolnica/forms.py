from django import forms
from .models import Pregled, Pacient


class PregledForm(forms.ModelForm):
    class Meta:
        model = Pregled
        fields = ['opis_simptomi', 'status', 'termin', 'zabeleska', 'patient']
