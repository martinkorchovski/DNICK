from django.contrib import admin

from .models import *
from django.contrib import messages
from django.db.models import Count

import random


# Register your models here.
class PekarAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser and obj:
            ostanati_pekari = list(Pekar.objects.exclude(id=obj.id))
            if ostanati_pekari:
                for torta in obj.torta_set.all():
                    torta.pekar = random.choice(ostanati_pekari)
                    torta.save()

        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs.annotate(broj_torti=Count('torta')).filter(broj_torti__lt=5)
        return qs


class TortaAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        torti = Torta.objects.filter(pekar=obj.pekar)

        if torti.count() > 10:
            messages.error(request, "Pekarot veke ima 10 torti!")
            return

        vkupna_cena = 0
        for torta in torti:
            vkupna_cena += torta.cena
        vkupna_cena += obj.cena

        if vkupna_cena > 10000:
            messages.error(request, "Vkupnata cena nadminuva 10000!")
            return

        if Torta.objects.filter(ime=obj.ime).exists():
            messages.error(request, "Veke postoi torta so toa ime!")
            return

        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj:
            return obj.pekar.user == request.user
        return True


admin.site.register(Torta, TortaAdmin)
admin.site.register(Pekar, PekarAdmin)

