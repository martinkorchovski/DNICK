from django.contrib import admin

from .models import *

# Register your models here.
class AvtorAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser

class KnigaAdmin(admin.ModelAdmin):
    exclude = ('avtor',)

    def has_add_permission(self, request):
        return Avtor.objects.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        super().save_model(request.obj.form.change)
        if not change:
            obj.avtor.add(Avtor.objects.get(user=request.user))

    def get_search_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ["opis"]
        return []

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        return obj.avtor.filter(user=request.user).exists()

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(avtor__user=request.user, opis__isnull=False).exclude(opis='')


admin.site.register(Kniga)
admin.site.register(Avtor)
admin.site.register(Kupuvac)
