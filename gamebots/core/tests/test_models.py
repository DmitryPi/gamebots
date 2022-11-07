from django.test import TestCase

from .factories import OrderFactory, ProductFactory


class TestProduct(TestCase):
    def setUp(self):
        pass

    def test_test(self):
        product = ProductFactory()
        print(product)


class TestOrder(TestCase):
    def setUp(self):
        pass

    def test_test(self):
        order = OrderFactory()
        print(order)
