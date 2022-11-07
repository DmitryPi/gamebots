from factory import Faker, SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyFloat

from gamebots.users.tests.factories import UserFactory

from ..models import Order, Product


class ProductFactory(DjangoModelFactory):
    title = Faker("sentence", nb_words=3, locale="ru_RU")
    description = Faker("text", locale="ru_RU")
    price = FuzzyFloat(70.0, 1000.0)
    currency = Product.Currency.RUB
    image = ""

    class Meta:
        model = Product


class OrderFactory(DjangoModelFactory):
    user = SubFactory(UserFactory)
    product = SubFactory(ProductFactory)
    quantity = 1
    status = Order.Status.PENDING

    class Meta:
        model = Order
