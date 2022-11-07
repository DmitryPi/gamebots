from django.test import TestCase

from ..models import Order, Product
from .factories import OrderFactory, ProductFactory


class TestProduct(TestCase):
    def setUp(self):
        self.batch_size = 10
        self.objects = ProductFactory.create_batch(size=self.batch_size)

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
        qs = Product.objects.all()
        assert not len(qs)

    def test_fields(self):
        for obj in self.objects:
            assert obj.uuid


class TestOrder(TestCase):
    def setUp(self):
        self.batch_size = 10
        self.objects = OrderFactory.create_batch(size=self.batch_size)

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
        qs = Order.objects.all()
        assert not len(qs)

    def test_fields(self):
        for obj in self.objects:
            assert obj.uuid
            assert obj.user.username
