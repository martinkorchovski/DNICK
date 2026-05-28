from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Agent(models.Model):
    ime_prezime = models.CharField(max_length=100)
    tel_broj = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    broj_prodazbi = models.IntegerField(default=0)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.ime_prezime


class Karakteristika(models.Model):
    ime = models.CharField(max_length=100)
    cena = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f"{self.ime} - {self.cena}$"


class Nedviznost(models.Model):
    ime = models.CharField(max_length=100)
    lokacija = models.CharField(max_length=100)
    povrsina = models.IntegerField(default=0)
    datum = models.DateField()
    slika = models.ImageField(upload_to='images')
    dali_e_prodadena = models.BooleanField(default=False)
    dali_e_rezervirana = models.BooleanField(default=False)
    agenti = models.ManyToManyField(Agent)
    karakteristiki = models.ManyToManyField(Karakteristika)
    opis = models.TextField(null=True, blank=True)

    def vkupna_cena(self):
        vkupno = 0;
        for karakteristika in self.karakteristiki.all():
            vkupno += karakteristika.cena
        return vkupno

    def __str__(self):
        return self.ime
