from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TuristickiVodic(models.Model):
    ime = models.CharField(max_length=100)
    prezime = models.CharField(max_length=100)
    tel_kontakt = models.CharField(max_length=100)
    email = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ime} {self.prezime}"

class Patuvanje(models.Model):
    mesto = models.CharField(max_length=100)
    cena = models.IntegerField(default=10)
    vremetraenje = models.IntegerField(default=10)
    slika = models.ImageField(upload_to="images", null=True, blank=True)
    vodic = models.ForeignKey(TuristickiVodic, on_delete=models.CASCADE)

    def __str__(self):
        return self.mesto
