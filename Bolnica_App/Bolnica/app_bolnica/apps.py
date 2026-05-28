from django.apps import AppConfig


class AppBolnicaConfig(AppConfig):
    name = 'app_bolnica'

    def ready(self):
        from . import signals
