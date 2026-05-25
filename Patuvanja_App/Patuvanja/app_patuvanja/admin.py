import random

from django.contrib import admin
from django.contrib import messages

from .models import *
from django.db.models import Count


# Register your models here.
class TuristickiVodicAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser and obj:
            ostanati_vodici = list(TuristickiVodic.objects.exclude(id=obj.id))
            if ostanati_vodici:
                for patuvanje in obj.patuvanje_set.all():
                    patuvanje.vodic = random.choice(ostanati_vodici)
                    patuvanje.save()

        return request.user.is_superuser

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs.annotate(broj_dest=Count('patuvanje')).filter(broj_dest__lt=3)
        return qs


class PatuvanjeAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        patuvanja = Patuvanje.objects.filter(vodic=obj.vodic)

        if patuvanja.count() >= 5:
            messages.error(request, "Vodicot ne smee da ima poveke od 5 destinacii!")
            return

        vkupna_cena = 0;
        for patuvanje in patuvanja:
            vkupna_cena += patuvanje.cena
        vkupna_cena += obj.cena

        if vkupna_cena >= 50000:
            messages.error(request, "Vkupnata cena ne smee da nadminuva 50000!")
            return

        if Patuvanje.objects.filter(mesto=obj.mesto).exists():
            messages.error(request, "Veke postoi patuvanje so toa ime!")
            return

        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj:
            return obj.vodic.user == request.user
        return True


admin.site.register(Patuvanje, PatuvanjeAdmin)
admin.site.register(TuristickiVodic, TuristickiVodicAdmin)
