from django.urls import resolve, reverse

from ..models import Bot


def test_bot_list():
    assert reverse("bots:bot-list") == "/"
    assert resolve("/").view_name == "bots:bot-list"


def test_bot_detail(bot: Bot):
    rev = reverse("bots:bot-detail", kwargs={"bot_slug": bot.slug})
    res = resolve(f"/bots/{bot.slug}/").view_name
    assert rev == f"/bots/{bot.slug}/"
    assert res == "bots:bot-detail"
