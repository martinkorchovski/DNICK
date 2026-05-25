from email.policy import default

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pekar(models.Model):
    ime = models.CharField(max_length=100)
    prezime = models.CharField(max_length=100)
    tel_broj = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ime} {self.prezime}"

class Torta(models.Model):
    ime = models.CharField(max_length=100)
    cena = models.IntegerField(default=50)
    opis = models.TextField()
    tezina = models.IntegerField(default=2)
    slika = models.ImageField(upload_to='images')
    pekar = models.ForeignKey(Pekar, on_delete=models.CASCADE)

    def __str__(self):
        return self.ime

