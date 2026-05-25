from django.contrib import admin

from .models import *
from django.utils import timezone

# Register your models here.
class IzlozbaAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs.filter(datum_kraj__gte=timezone.now().date())
        umetnik = Umetnik.objects.filter(user=request.user).first()
        return qs.filter(umetnickodelo__umetnik=umetnik)


class UmetnikAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser


class UmetnickoDeloAdmin(admin.ModelAdmin):
    exclude = ('umetnik',)

    def has_add_permission(self, request):
        return Umetnik.objects.filter(user=request.user).exists()

    def save_model(self, request, obj, form, change):
        if not change:
            obj.umetnik = Umetnik.objects.get(user=request.user)
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        return obj.umetnik.user == request.user


admin.site.register(Umetnik, UmetnikAdmin)
admin.site.register(UmetnickoDelo, UmetnickoDeloAdmin)
admin.site.register(Izlozba, IzlozbaAdmin)
