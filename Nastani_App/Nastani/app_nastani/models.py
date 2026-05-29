from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Bend(models.Model):
    ime = models.CharField(max_length=100)
    drzava = models.CharField(max_length=100)
    godina = models.IntegerField(default=2020)
    broj_nastapi = models.IntegerField(default=0)

    def __str__(self):
        return self.ime


class Nastan(models.Model):
    ime = models.CharField(max_length=100)
    datum = models.DateTimeField()
    slika = models.ImageField(upload_to="images")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bendovi = models.ManyToManyField(Bend)
    na_otvoreno = models.BooleanField(default=False)
    lokacija = models.CharField(max_length=100, null=True, blank=True)
    opis = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.ime
