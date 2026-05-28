from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Lekar(models.Model):
    SPECIJALNOST_CHOICES = (
        ["kardiolog", "Kardiolog"],
        ["dermatolog", "Dermatolog"],
        ["nevrolog", "Nevrolog"],
    )

    ime_prezime = models.CharField(max_length=100)
    specijalnost = models.CharField(max_length=20, choices=SPECIJALNOST_CHOICES)
    slika = models.ImageField(upload_to="images")
    institucija = models.CharField(max_length=100)
    broj_pregledi = models.IntegerField(default=0)
    email = models.EmailField()
    tel_broj = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ime_prezime


class Pacient(models.Model):
    POL_CHOICES = [
        ('maski', 'Maski'),
        ('zenski', 'Zenski'),
        ('drugo', 'Drugo'),
    ]

    ime_prezime = models.CharField(max_length=100)
    datum_ragjanje = models.DateField()
    pol = models.CharField(max_length=20, choices=POL_CHOICES)
    email = models.EmailField()
    institucija = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.ime_prezime


class Pregled(models.Model):
    TIP_CHOICES = [
        ('kardioloski', 'Kardioloski'),
        ('dermatoloski', 'Dermatoloski'),
        ('nevroloski', 'Nevroloski'),
    ]

    STATUS_CHOICES = [
        ('vo_tek', 'Vo tek'),
        ('zakazan', 'Zakazan'),
        ('zavrsen', 'Zavrsen'),
    ]

    tip = models.CharField(max_length=20, choices=TIP_CHOICES)
    opis_simptomi = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    termin = models.DateTimeField()
    zabeleska = models.TextField()
    glaven_lekar = models.ForeignKey(Lekar, on_delete=models.CASCADE)
    patient = models.ForeignKey(Pacient, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.tip} on {self.termin.strftime('%Y-%m-%d %H:%M')}"


class PregledDoktori(models.Model):
    pregled = models.ForeignKey(Pregled, on_delete=models.CASCADE)
    lekar = models.ForeignKey(Lekar, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('pregled', 'lekar')

    def __str__(self):
        return f"{self.lekar.ime_prezime} asistira {self.pregled}"
