from django.contrib import admin
from .models import *
from django.db.models import Q


# Register your models here.
class LekarAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return request.user.is_superuser


class PacientAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return request.user.is_superuser


class PregledAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return Lekar.objects.filter(user=request.user).exists()

    def save_model(self, request, obj, form, change):
        if not change:
            obj.glaven_lekar = Lekar.objects.get(user=request.user)
        else:
            old_obj = Pregled.objects.get(id=obj.id)
            if old_obj.status == 'vo_tek' and obj.status == 'zavrsen':
                obj.glaven_lekar.broj_pregledi += 1
                obj.glaven_lekar.save()
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if obj:
            lekar_qs = Lekar.objects.filter(user=request.user)
            if lekar_qs.exists():
                lekar = lekar_qs.first()
                return obj.glaven_lekar == lekar
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and obj.status != 'zakazan':
            return False
        return super().has_delete_permission(request, obj)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        lekar_qs = Lekar.objects.filter(user=request.user)
        if not lekar_qs.exists():
            return qs.none()
        lekar = lekar_qs.first()
        return qs.filter(
            Q(glaven_lekar=lekar) |
            Q(pregledDoktori__lekar=lekar)
        ).distinct()


admin.site.register(Lekar, LekarAdmin)
admin.site.register(Pregled, PregledAdmin)
admin.site.register(Pacient, PacientAdmin)
admin.site.register(PregledDoktori)
