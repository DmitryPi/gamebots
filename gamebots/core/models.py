import uuid as uuid_lib

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils import FieldTracker
from model_utils.models import TimeStampedModel

from gamebots.core.utils import get_unique_licensekey, get_unique_slug


class Product(TimeStampedModel):
    # choices
    class Currency(models.TextChoices):
        RUB = "₽", _("Ruble")
        DOLLAR = "$", _("Dollar")
        EURO = "€", _("Euro")

    # fields
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    title = models.CharField(_("Title"), max_length=55)
    slug = models.SlugField(_("Slug"), unique=True, max_length=55)
    description = models.TextField(_("Description"), blank=True, default="")
    price = models.FloatField(_("Price"), default=0.0)
    currency = models.CharField(
        max_length=2, choices=Currency.choices, default=Currency.RUB
    )
    image = models.ImageField(
        _("Poster"), blank=True, default="", upload_to="products/"
    )
    tracker = FieldTracker(fields=["title"])

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return f"{self.title} : {self.price}"

    def save(self, *args, **kwargs):
        if not self.slug or self.title != self.tracker.previous("title"):
            self.slug = get_unique_slug(Product, self.title)
        return super().save(*args, **kwargs)


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


class LicenseKey(TimeStampedModel):
    # choices
    class Status(models.TextChoices):
        INACTIVE = "INACTIVE", _("Inactive")
        ACTIVE = "ACTIVE", _("Active")

    # fields
    key = models.CharField(_("Key"), unique=True, max_length=55)
    status = models.CharField(
        max_length=55, choices=Status.choices, default=Status.INACTIVE
    )

    class Meta:
        verbose_name = _("LicenseKey")
        verbose_name_plural = _("LicenseKeys")

    def __str__(self):
        return f"{self.key}"

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = get_unique_licensekey()
        return super().save(*args, **kwargs)
