from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Umetnik(models.Model):
    UMETNICKI_STIL_CHOICES = (
        ["impressionism", "Impressionism"],
        ["pop_art", "Pop Art"],
        ["graffiti", "Graffiti"],
    )

    ime_prezime = models.CharField(max_length=100)
    umetnicki_stil = models.CharField(max_length=20, choices=UMETNICKI_STIL_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ime_prezime

class Izlozba(models.Model):
    naslov = models.CharField(max_length=100)
    datum_pocetok = models.DateField()
    datum_kraj = models.DateField()
    opis = models.TextField()
    lokacija = models.CharField(max_length=100)

    def __str__(self):
        return self.naslov

class UmetnickoDelo(models.Model):
    naslov = models.CharField(max_length=100)
    datum_sozdavanje = models.DateField()
    slika = models.ImageField(upload_to="images")
    umetnik = models.ForeignKey(Umetnik, on_delete=models.CASCADE, null=True, blank=True)
    izlozba = models.ForeignKey(Izlozba, on_delete=models.SET_NULL, null=True,blank=True)

    def __str__(self):
        return self.naslov


