from django.urls import path

from .views import BotDetailView, BotListView

app_name = "bots"

urlpatterns = [
    path("", view=BotListView.as_view(), name="bot-list"),
    path("bots/<slug:bot_slug>/", view=BotDetailView.as_view(), name="bot-detail"),
]
