from django.test import TestCase

from ..models import Bot, Feature, Question
from .factories import BotFactory, FeatureFactory, QuestionFactory


class TestBot(TestCase):
    def setUp(self):
        self.batch_size = 10
        self.objects = BotFactory.create_batch(size=self.batch_size)

    def test_create(self):
        assert len(self.objects) == self.batch_size

    def test_update(self):
        new_title = "new title"
        for obj in self.objects:
            obj.title = new_title
            obj.save()
        for obj in self.objects:
            assert obj.title == new_title

    def test_delete(self):
        for obj in self.objects:
            obj.delete()
        qs = Bot.objects.all()
        assert not len(qs)

    def test_fields(self):
        for obj in self.objects:
            assert obj.title
            assert obj.slug
            assert obj.description


class TestFeature(TestCase):
    def setUp(self):
        self.batch_size = 10
        self.objects = FeatureFactory.create_batch(size=self.batch_size)

    def test_create(self):
        assert len(self.objects) == self.batch_size

    def test_update(self):
        new_title = "new title"
        for obj in self.objects:
            obj.title = new_title
            obj.save()
        for obj in self.objects:
            assert obj.title == new_title

    def test_delete(self):
        for obj in self.objects:
            obj.delete()
        qs = Feature.objects.all()
        assert not len(qs)

    def test_fields(self):
        for obj in self.objects:
            assert obj.bot.slug
            assert obj.title
            assert obj.description
            assert obj.status == Feature.Status.published


class TestQuestion(TestCase):
    def setUp(self):
        self.batch_size = 10
        self.objects = QuestionFactory.create_batch(size=self.batch_size)

    def test_create(self):
        assert len(self.objects) == self.batch_size

    def test_update(self):
        new_question = "new question"
        for obj in self.objects:
            obj.title = new_question
            obj.save()
        for obj in self.objects:
            assert obj.title == new_question

    def test_delete(self):
        for obj in self.objects:
            obj.delete()
        qs = Question.objects.all()
        assert not len(qs)

    def test_fields(self):
        for obj in self.objects:
            assert obj.bot.slug
            assert obj.question
            assert obj.answer
            assert obj.status == Question.Status.published
