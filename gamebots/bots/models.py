from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils import FieldTracker

from gamebots.core.utils import get_unique_slug


class Bot(models.Model):
    title = models.CharField(_("Title"), max_length=55)
    title_sm = models.CharField(_("Title short"), max_length=10, blank=True)
    slug = models.SlugField(_("Slug"), unique=True, max_length=55)
    tracker = FieldTracker(fields=["title"])

    class Meta:
        verbose_name = _("Game")
        verbose_name_plural = _("Games")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug or self.title != self.tracker.previous("title"):
            self.slug = get_unique_slug(Bot, self.title)
        return super().save(*args, **kwargs)


class Feature(models.Model):
    # relations
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE)
    # fields
    title = models.CharField(_("Title"), max_length=100)
    description = models.TextField(_("Description"), blank=True, default="")
    image = models.ImageField(_("Poster"), blank=True, default="", upload_to="posters/")
    video = models.URLField(max_length=255)

    class Meta:
        verbose_name = _("Game")
        verbose_name_plural = _("Games")

    def __str__(self):
        return self.title
