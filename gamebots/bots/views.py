from django.shortcuts import get_object_or_404, render  # noqa skip
from django.views.generic import DetailView, ListView

from .models import Bot


class BotListView(ListView):
    model = Bot
    queryset = Bot.objects.all()
    template_name = "pages/home.html"


class BotDetailView(DetailView):
    model = Bot

    def get_object(self, *args, **kwargs):
        obj = get_object_or_404(
            Bot.objects.prefetch_related(), slug=self.slug_url_kwarg
        )
        return obj

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context
