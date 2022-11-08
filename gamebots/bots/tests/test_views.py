import pytest
from django.contrib.auth.models import AnonymousUser, User
from django.test import Client, RequestFactory
from django.urls import reverse

from ..models import Bot
from ..views import BotListView
from .factories import BotFactory


class TestBotListView:
    def test_response(self, user: User, rf: RequestFactory):
        request = rf.get(reverse("bots:bot-list"))
        request.user = user
        response = BotListView.as_view()(request)
        assert response.status_code == 200
        assert response.charset == "utf-8"

    def test_response_anon(self, user: User, rf: RequestFactory):
        request = rf.get(reverse("bots:bot-list"))
        request.user = AnonymousUser
        response = BotListView.as_view()(request)
        assert response.status_code == 200
        assert response.charset == "utf-8"

    @pytest.mark.django_db
    def test_response_context(self, bot_ten: list[BotFactory], client: Client):
        response = client.get(reverse("bots:bot-list"))
        assert len(response.context["bot_list"]) == 10
        for i in response.context["bot_list"]:
            assert isinstance(i, Bot)
