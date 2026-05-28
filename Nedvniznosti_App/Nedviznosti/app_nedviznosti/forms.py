from django.forms import ModelForm
from .models import Nedviznost


class NedviznostiForm(ModelForm):
    class Meta:
        model = Nedviznost
        fields = ["ime", "opis", "karakteristiki", "lokacija", "povrsina", "datum", "slika", "dali_e_prodadena",
                  "dali_e_rezervirana"]
