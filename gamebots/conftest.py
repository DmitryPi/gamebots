import pytest

from gamebots.bots.models import Bot, Feature, Question
from gamebots.bots.tests.factories import BotFactory, FeatureFactory, QuestionFactory
from gamebots.users.models import User
from gamebots.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> User:
    return UserFactory()


@pytest.fixture
def bot(db) -> Bot:
    return BotFactory()


@pytest.fixture
def feature(db) -> Feature:
    return FeatureFactory()


@pytest.fixture
def question(db) -> Question:
    return QuestionFactory()
