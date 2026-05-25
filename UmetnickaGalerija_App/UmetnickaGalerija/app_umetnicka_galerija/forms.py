from django.forms import ModelForm
from .models import Izlozba

class IzlozbaForm(ModelForm):
    class Meta:
        model = Izlozba
        fields = ["naslov", "datum_pocetok", "datum_kraj", "lokacija", "opis"]

    def __init__(self, *args, **kwargs):
        super(IzlozbaForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'