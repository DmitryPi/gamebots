import uuid as uuid_lib

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


class Product(TimeStampedModel):
    # choices
    class Currency(models.TextChoices):
        RUB = "₽", _("Ruble")
        DOLLAR = "$", _("Dollar")
        EURO = "€", _("Euro")

    # fields
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    title = models.CharField(_("Title"), max_length=55)
    slug = models.CharField(_("Slug"), max_length=55, default="")
    description = models.TextField(_("Description"), blank=True, default="")
    price = models.FloatField(_("Price"), default=0.0)
    currency = models.CharField(
        max_length=2, choices=Currency.choices, default=Currency.RUB
    )
    image = models.ImageField(
        _("Poster"), blank=True, default="", upload_to="products/"
    )

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return f"{self.title} : {self.price}"


class Order(TimeStampedModel):
    # choices
    class Status(models.TextChoices):
        FAILED = "FAILED", _("Failed")
        PENDING = "PENDING", _("Pending")
        SUCCESS = "SUCCESS", _("Success")

    # relations
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # fields
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    quantity = models.IntegerField(default=1)
    status = models.CharField(
        max_length=55, choices=Status.choices, default=Status.PENDING
    )

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return f"{self.uuid}"
