from django.forms import ModelForm
from .models import Kniga

class KnigaForm(ModelForm):
    class Meta:
        model = Kniga
        fields = ["naslov", "cena", "opis"]