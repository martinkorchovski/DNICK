from django.forms import ModelForm
from .models import Nastan


class NastanForm(ModelForm):
    class Meta:
        model = Nastan
        fields = ["ime", "datum", "lokacija", "opis", "slika",]
