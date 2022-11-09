from django.shortcuts import get_object_or_404, render  # noqa skip
from django.views.generic import DetailView, ListView

from .models import Bot


class BotListView(ListView):
    model = Bot
    queryset = Bot.objects.all()
    template_name = "bots/bot-list.html"


class BotDetailView(DetailView):
    model = Bot
    template_name = "bots/bot-detail.html"
    slug_url_kwarg = "bot_slug"
