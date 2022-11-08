from django.shortcuts import render  # noqa skip
from django.views.generic import DetailView, ListView

from .models import Bot


class BotListView(ListView):
    model = Bot
    template_name = "pages/home.html"
    queryset = Bot.objects.all()


class BotDetailView(DetailView):
    model = Bot
