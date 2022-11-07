from django.utils.text import slugify
from factory import Faker, SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyFloat

from gamebots.users.tests.factories import UserFactory

from ..models import Order, Product
from ..utils import get_unique_slug


def model_slug_test_generator(cls, test_slug: str, create=5) -> None:
    for i in range(create):
        slug = get_unique_slug(cls, test_slug)
        obj = cls.objects.create(title=test_slug, slug=slug)
        res_slug = f"{slugify(test_slug)}-{i}" if i > 0 else slugify(test_slug)
        assert "@" not in res_slug
        assert obj.slug == res_slug


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
