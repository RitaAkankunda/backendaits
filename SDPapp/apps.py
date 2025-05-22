from django.apps import AppConfig
from django.db.models.signals import post_migrate

class SdpappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "SDPapp"

    def ready(self):
        from SDPapp.signals import ensure_default_departments
        post_migrate.connect(ensure_default_departments, sender=self)
