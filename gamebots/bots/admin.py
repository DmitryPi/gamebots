from django.contrib import admin

from .models import Bot, Feature, Question


@admin.register(Bot)
class BotAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    pass
