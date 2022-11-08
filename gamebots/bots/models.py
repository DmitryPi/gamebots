from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils import FieldTracker
from model_utils.models import TimeStampedModel

from gamebots.core.utils import get_unique_slug


class Bot(TimeStampedModel):
    title = models.CharField(_("Title"), max_length=55)
    title_sm = models.CharField(_("Title short"), max_length=10, blank=True)
    description = models.TextField(_("Description"), blank=True, default="")
    slug = models.SlugField(_("Slug"), unique=True, max_length=55)
    tracker = FieldTracker(fields=["title"])

    class Meta:
        verbose_name = _("Bot")
        verbose_name_plural = _("Bots")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug or self.title != self.tracker.previous("title"):
            self.slug = get_unique_slug(Bot, self.title)
        return super().save(*args, **kwargs)


class Feature(TimeStampedModel):
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

    class Meta:
        verbose_name = _("Feature")
        verbose_name_plural = _("Features")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
