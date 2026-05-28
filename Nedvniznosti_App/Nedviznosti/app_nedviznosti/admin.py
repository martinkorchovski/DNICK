from django.contrib import admin
from .models import *
from django.utils import timezone


# Register your models here.
class AgentAdmin(admin.ModelAdmin):
    list_display = ('ime',)

    def has_add_permission(self, request):
        return request.user.is_superuser


class KarakteristikaAdmin(admin.ModelAdmin):
    list_display = ('ime', 'cena')

    def has_add_permission(self, request):
        return request.user.is_superuser


class NedviznostiAdmin(admin.ModelAdmin):
    list_display = ('ime', 'lokacija', 'povrsina')

    def save_model(self, request, obj, form, change):
        if change and obj.dali_e_prodadena:
            stara = Nedviznost.objects.get(id=obj.id)
            if not stara.dali_e_prodadena:
                for agent in obj.agenti.all():
                    agent.broj_prodazbi += 1
                    agent.save()

        super().save_model(request, obj, form, change)
        agent = Agent.objects.get(user=request.user)
        obj.agenti.add(agent)

    def has_add_permission(self, request):
        return Agent.object.filter(user=request.user).exists()

    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return True
        return obj.karakteristiki.count() == 0

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        return obj.agenti.filter(user=request.user).exists()

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs.filter(datum=timezone.now().date())
        return qs.filter(agenti__user=request.user)


admin.site.register(Nedviznost, NedviznostiAdmin)
admin.site.register(Karakteristika, KarakteristikaAdmin)
admin.site.register(Agent, AgentAdmin)
