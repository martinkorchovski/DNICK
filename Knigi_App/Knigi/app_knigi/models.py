from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Avtor(models.Model):
    ime_prezime = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ime_prezime

class Kupuvac(models.Model):
    ime_prezime = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ime_prezime

class Kniga (models.Model):
    naslov = models.CharField(max_length=100)
    opis = models.TextField()
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    slika = models.ImageField(upload_to="images")
    avtor = models.ManyToManyField(Avtor)

    def __str__(self):
        return self.naslov
