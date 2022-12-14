from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from model_utils import FieldTracker
from model_utils.models import TimeStampedModel

from gamebots.core.utils import get_unique_slug


class Bot(TimeStampedModel):
    title = models.CharField(_("Title"), max_length=55)
    subtitle = models.CharField(_("Subtitle"), max_length=200, blank=True)
    description = models.TextField(_("Description"), blank=True, default="")
    slug = models.SlugField(_("Slug"), unique=True, max_length=55, blank=True)
    poster = models.ImageField(
        _("Poster"), blank=True, default="", upload_to="posters/"
    )
    tracker = FieldTracker(fields=["title"])

    class Meta:
        verbose_name = _("Bot")
        verbose_name_plural = _("Bots")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("bots:bot-detail", kwargs={"bot_slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug or self.title != self.tracker.previous("title"):
            self.slug = get_unique_slug(Bot, self.title)
        return super().save(*args, **kwargs)


class Feature(TimeStampedModel):
    # choices
    class Status(models.TextChoices):
        draft = "draft", _("Draft")
        published = "published", _("Published")

    # relations
    bot = models.ForeignKey(
        Bot,
        on_delete=models.CASCADE,
        related_name="%(class)ss",
        related_query_name="%(class)s",
    )
    # fields
    title = models.CharField(_("Title"), max_length=100)
    description = models.TextField(_("Description"), blank=True, default="")
    image = models.ImageField(_("Poster"), blank=True, default="", upload_to="posters/")
    video = models.URLField(max_length=255)
    status = models.CharField(
        _("Status"), max_length=55, choices=Status.choices, default=Status.published
    )

    class Meta:
        verbose_name = _("Feature")
        verbose_name_plural = _("Features")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


class Question(TimeStampedModel):
    # choices
    class Status(models.TextChoices):
        draft = "draft", _("Draft")
        published = "published", _("Published")

    # relations
    bot = models.ForeignKey(
        Bot,
        on_delete=models.CASCADE,
        related_name="%(class)ss",
        related_query_name="%(class)s",
    )
    # fields
    question = models.CharField(_("Question"), max_length=255)
    answer = models.TextField(_("Answer"), blank=True, default="")
    status = models.CharField(
        _("Status"), max_length=55, choices=Status.choices, default=Status.published
    )

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
