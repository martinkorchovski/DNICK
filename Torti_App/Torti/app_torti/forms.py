from django.forms import ModelForm
from .models import Torta


class TortaForm(ModelForm):
    class Meta:
        model = Torta
        fields = ["ime", "cena", "tezina", "opis", "slika"]

    def __init__(self, *args, **kwargs):
        super(TortaForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
