from django.shortcuts import render  # noqa skip
from django.views.generic import DetailView, ListView

from .models import Bot


class BotListView(ListView):
    model = Bot
    template_name = "pages/home.html"


class BotDetailView(DetailView):
    model = Bot
