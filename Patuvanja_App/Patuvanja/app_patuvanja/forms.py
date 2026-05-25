from django.forms import ModelForm
from .models import Patuvanje


class PatuvanjaForm(ModelForm):
    class Meta:
        model = Patuvanje
        fields = ["slika", "mesto", "cena", "vremetraenje"]

    def __init__(self, *args, **kwargs):
        super(PatuvanjaForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'