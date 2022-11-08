import random
import re
import string

from django.utils.text import slugify
from transliterate import translit


def get_unique_slug(cls, title: str) -> str:
    """If title in ru unicode - it will transliterate,
    otherwise it continues as it is."""
    title = translit(title, "ru", reversed=True)  # fix ru unicode titles
    slug = slugify(title)
    unique_slug = slug
    num = 1
    while cls.objects.filter(slug=unique_slug).exists():
        unique_slug = f"{slug}-{num}"
        num += 1
    return unique_slug


def capitalize_str(s: str) -> str:
    """Capitalize string words"""
    return " ".join([w.capitalize() for w in s.split(" ")]).strip()


def capitalize_slug(slug: str) -> str:
    """Turn slug into sentence and capitalize words"""
    return re.sub(
        r"\d", "", " ".join([w.capitalize() for w in slug.split("-")])
    ).strip()


def get_unique_licensekey(n=24) -> str:
    """Generate random integer-based licensekey"""
    res = "".join(random.choices(string.digits, k=n))
    return res
