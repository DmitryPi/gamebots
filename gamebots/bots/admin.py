from django.contrib import admin  # noqa skip

from .models import Bot, Feature


@admin.register(Bot)
class BotAdmin(admin.ModelAdmin):
    pass


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    pass
