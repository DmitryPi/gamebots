from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from ..models import Bot, Feature, Question


class BotFactory(DjangoModelFactory):
    title = Faker("sentence", nb_words=3)
    description = Faker("text", locale="ru_RU")

    class Meta:
        model = Bot


class FeatureFactory(DjangoModelFactory):
    bot = SubFactory(BotFactory)
    title = Faker("sentence", nb_words=3, locale="ru_RU")
    description = Faker("text", locale="ru_RU")

    class Meta:
        model = Feature


class QuestionFactory(DjangoModelFactory):
    bot = SubFactory(BotFactory)
    question = Faker("sentence", nb_words=5, locale="ru_RU")
    answer = Faker("text", locale="ru_RU")

    class Meta:
        model = Question
