from django.contrib import admin
from .models import *


# Register your models here.
class BendAdmin(admin.ModelAdmin):
    list_display = ('ime', 'drzava')


class NastanAdmin(admin.ModelAdmin):
    list_display = ('ime', 'datum')
    exclude = ("user",)

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        super().save_model(request, obj, self, change)

    def has_delete_permission(self, request, obj=None):
        if obj and obj.user == request.user and obj.bendovi.count() == 0:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user and obj.bendovi.count() == 0:
            return True
        return False


admin.site.register(Bend, BendAdmin)
admin.site.register(Nastan, NastanAdmin)
