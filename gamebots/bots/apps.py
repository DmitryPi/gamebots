from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BotsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "gamebots.bots"
    verbose_name = _("Bots")

    def ready(self):
        try:
            import gamebots.bots.signals  # noqa F401
        except ImportError:
            pass
